<#
PowerShell deploy script for MVP: creates S3 bucket, uploads model, packages Lambda, creates IAM role, creates Lambda function, and wires an HTTP API via API Gateway v2.

USAGE (run from repo root in pwsh and with AWS CLI configured):
.
# 1) Edit the variables below or pass as params
# 2) Run: .\deploy\aws_deploy.ps1 -BucketName vpbank-hackathon-uplift-model-store -Region ap-southeast-1 -LambdaName uplift-engine-demo -ModelKey models/uplift_model.pkl

Note: This script runs AWS CLI commands and requires AWS credentials configured with sufficient permissions.
It attempts sensible defaults but will echo commands before running for review.

#> 
param(
    [string]$BucketName = "vpbank-hackathon-uplift-model-store",
    [string]$Region = "ap-southeast-1",
    [string]$LambdaName = "uplift-engine-demo",
    [string]$ModelKey = "models/uplift_model.pkl",
    [string]$RoleName = "uplift-engine-lambda-role"
)

function Run-Check {
    param($cmd)
    Write-Host "RUNNING: $cmd" -ForegroundColor Cyan
    $res = Invoke-Expression $cmd
    return $res
}

# 0. Validate prerequisites
if (-not (Get-Command aws -ErrorAction SilentlyContinue)) {
    Write-Error "AWS CLI not found. Install and configure AWS CLI before running this script."; exit 1
}
if (-not (Test-Path src\uplift_model.pkl)) {
    Write-Error "Model file src/uplift_model.pkl not found. Ensure the model exists."; exit 1
}

# 1. Ensure bucket exists
Write-Host "Creating S3 bucket (if not exists): $BucketName in $Region"
Run-Check "aws s3api create-bucket --bucket $BucketName --region $Region --create-bucket-configuration LocationConstraint=$Region" 2>$null

# 2. Upload model to S3
Write-Host "Uploading model to s3://$BucketName/$ModelKey"
Run-Check "aws s3 cp src/uplift_model.pkl s3://$BucketName/$ModelKey --region $Region"

# 3. Package Lambda: install dependencies into build/ and zip
$buildDir = "./build_lambda"
if (Test-Path $buildDir) { Remove-Item $buildDir -Recurse -Force }
New-Item -ItemType Directory -Path $buildDir | Out-Null

Write-Host "Installing lambda requirements into $buildDir (may take a few minutes)"
Run-Check "python -m pip install -r src/lambda/requirements.txt -t $buildDir"

# copy lambda source
Copy-Item -Path src/lambda/*.py -Destination $buildDir -Force
Set-Location $buildDir
if (Test-Path lambda_package.zip) { Remove-Item lambda_package.zip -Force }
Write-Host "Zipping lambda package..."
Compress-Archive -Path * -DestinationPath lambda_package.zip
Set-Location -Path ..

# 4. Create IAM role for Lambda
$trustPolicy = @'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }
  ]
}
'@
$trustFile = "./deploy/lambda-trust.json"
$trustPolicy | Out-File -FilePath $trustFile -Encoding ascii
Write-Host "Creating IAM role: $RoleName"
$roleJson = Run-Check "aws iam create-role --role-name $RoleName --assume-role-policy-document file://$trustFile --output json"
$roleArn = (echo $roleJson | ConvertFrom-Json).Role.Arn
Write-Host "Role ARN: $roleArn"

# attach policies (use least privilege in production)
Run-Check "aws iam attach-role-policy --role-name $RoleName --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
Run-Check "aws iam attach-role-policy --role-name $RoleName --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"

# 5. Upload lambda package to S3 (optional) or create function directly
Write-Host "Creating Lambda function: $LambdaName"
$zipPath = Join-Path $buildDir "lambda_package.zip"
$createCmd = "aws lambda create-function --function-name $LambdaName --runtime python3.11 --role $roleArn --handler app.lambda_handler --zip-file fileb://$zipPath --region $Region --timeout 30 --memory-size 512 --environment Variables={MODEL_S3_BUCKET=$BucketName,MODEL_S3_KEY=$ModelKey}"
Run-Check $createCmd

# 6. Create HTTP API (API Gateway v2) and integrate with Lambda
Write-Host "Creating HTTP API (API Gateway v2)"
$apiJson = Run-Check "aws apigatewayv2 create-api --name $LambdaName-API --protocol-type HTTP --region $Region --target arn:aws:apigateway:$Region:lambda:path/2015-03-31/functions/arn:aws:lambda:$Region:$(aws sts get-caller-identity --query Account --output text):function:$LambdaName/invocations --output json"
$apiId = (echo $apiJson | ConvertFrom-Json).ApiId
Write-Host "API created: $apiId"

# Create default stage
Run-Check "aws apigatewayv2 create-stage --api-id $apiId --stage-name prod --auto-deploy --region $Region"

# Give permission to API Gateway to invoke the Lambda
$accountId = Run-Check "aws sts get-caller-identity --query Account --output text"
$lambdaArn = "arn:aws:lambda:$Region:$accountId:function:$LambdaName"
Run-Check "aws lambda add-permission --function-name $LambdaName --statement-id apigw-$apiId --action lambda:InvokeFunction --principal apigateway.amazonaws.com --source-arn arn:aws:execute-api:$Region:$accountId:$apiId/*/* --region $Region"

# 7. Output endpoint URL
$apiEndpoint = "https://$apiId.execute-api.$Region.amazonaws.com/prod"
Write-Host "API endpoint (POST) is: $apiEndpoint" -ForegroundColor Green

Write-Host "Deployment complete. Update docs/demo_commands.md with the endpoint and rehearse the demo."
