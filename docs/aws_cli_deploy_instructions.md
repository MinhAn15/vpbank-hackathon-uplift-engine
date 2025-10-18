AWS CLI deploy instructions — safe run

This repository includes `deploy/aws_deploy.ps1`, a convenience script to deploy a minimal MVP to AWS for demo purposes. Please read carefully before running.

Before you run
- Ensure you have the AWS CLI installed and configured with credentials for an account/project you control.
- Review the script carefully. It will create resources (S3 bucket, IAM role, Lambda, API Gateway). You are responsible for resource naming and cost control.
- Prefer to run in a separate sandbox account or with resource tags that identify the hackathon project.

How to run (PowerShell)
1. Open PowerShell in the repo root.
2. Review and optionally update parameters in the script header.
3. Run the script (example):

```powershell
.
\deploy\aws_deploy.ps1 -BucketName vpbank-hackathon-uplift-model-store -Region ap-southeast-1 -LambdaName uplift-engine-demo -ModelKey models/uplift_model.pkl
```

After running
- The script will print the API endpoint URL. Update `docs/demo_commands.md` with the endpoint so the demo uses the live URL.
- Clean up resources after the hackathon to avoid charges: delete Lambda, API, IAM role, and S3 bucket.

Security reminder
- The script attaches basic Lambda execution and S3 read roles for convenience. In production, replace these with least-privilege policies scoped to the exact S3 key.
- Never commit AWS credentials to the repo.
