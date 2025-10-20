Lambda stub for Uplift Engine

How to run locally (development):

1. Ensure `uplift_model.pkl` exists (default local fallback is `src/uplift_model.pkl`), or set env vars to load from S3:
    - `MODEL_S3_BUCKET`
    - `MODEL_S3_KEY`
2. From the project root with your virtualenv active, you can invoke the handler manually:

```python
from src.lambda.app import lambda_handler

# Example event (supports customerId or customer_id)
event = {
    "body": '{"customer_id": 123, "age": 30, "income": 50000, "number_of_transactions": 2 }'
}
print(lambda_handler(event, None))
```

Environment variables:
- MODEL_S3_BUCKET / MODEL_S3_KEY: optional S3 location to download model on cold start.

Notes:
- This is a local development stub. For AWS Lambda deployment, package dependencies accordingly and configure environment variables in the Lambda console or IaC.
