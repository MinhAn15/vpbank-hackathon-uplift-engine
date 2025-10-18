AWS deployment steps — minimal MVP (S3 + Lambda + API Gateway)

Prerequisites
- AWS account with permissions to create S3 buckets, IAM roles, Lambda functions, and API Gateway.
- AWS CLI configured locally (optional but helpful).

1) Create S3 bucket and upload model
- Console: S3 -> Create bucket (e.g. `vpbank-hackathon-uplift-model-store`)
- Upload `src/uplift_model.pkl` to the bucket. Note the key (e.g. `models/uplift_model.pkl`).

2) Create IAM role for Lambda
- IAM -> Roles -> Create role -> Lambda
- Attach AmazonS3ReadOnlyAccess (or a scoped policy allowing GetObject on the model key).
- Note the Role ARN.

3) Create Lambda function
- Lambda -> Create function -> Author from scratch
  - Runtime: Python 3.11 (or 3.10)
  - Role: choose the role created above
- In Function code:
  - Upload a ZIP with `app.py` and the necessary dependencies, or use a Lambda Layer for heavy deps (joblib, pandas, scikit-learn).
  - Alternatively, for a simple demo, package `app.py` and include `uplift_model.pkl` in the deployment package (small models only).
- Set environment variables:
  - MODEL_S3_BUCKET = your-bucket-name
  - MODEL_S3_KEY = models/uplift_model.pkl

4) Test Lambda in Console
- Create a test event with body JSON:
  {
    "body": "{\"customerId\":1, \"age\":35, \"income\":50000, \"number_of_transactions\":12}"
  }
- Run the test and verify the JSON response contains `upliftScore` and `recommendation`.

5) Create API Gateway HTTP API trigger
- In Lambda console, Add trigger -> API Gateway -> Create an HTTP API
- Note the endpoint URL after creation.

6) Demo flow
- Call the endpoint URL with POST and the same JSON payload as above.
- Expect a 200 JSON response like: { "customerId": 1, "upliftScore": 0.08, "recommendation": "TARGET" }

Packaging tips
- For larger dependencies (pandas, scikit-learn), use a Lambda Layer or build a deployment package on Amazon Linux to ensure binary compatibility.
- Alternative: Host the model in S3 and have Lambda download it on cold start (this file shows exactly that approach).

Security notes
- Use least-privilege IAM policies (limit GetObject to the exact S3 key).
- Do not bake credentials into code; use IAM roles.

Post-deploy
- Update `docs/demo_commands.md` with the endpoint URL so the demo uses the real AWS endpoint.
