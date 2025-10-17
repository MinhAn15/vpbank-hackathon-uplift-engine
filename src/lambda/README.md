Lambda stub for Uplift Engine

How to run locally (development):

1. Ensure `uplift_model.pkl` exists in the project root (or set MODEL_PATH env var to the model location).
2. From the project root with your virtualenv active, you can invoke the handler manually:

```python
from src.lambda.app import lambda_handler

# Example event
event = {
    "body": '{"customerId": "123","age": 30, "income": 50000, "number_of_transactions": 2 }'
}
print(lambda_handler(event, None))
```

Environment variables:
- MODEL_PATH: optional path to the pickled model file.

Notes:
- This is a local development stub. For AWS Lambda deployment, package dependencies accordingly and configure environment variables in the Lambda console or IaC.
