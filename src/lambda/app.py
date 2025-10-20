import joblib
import pandas as pd
import json
import os
import boto3


# Lambda-friendly model loader: pull from S3 if env vars present, else load local fallback
MODEL_S3_BUCKET = os.environ.get('MODEL_S3_BUCKET')
MODEL_S3_KEY = os.environ.get('MODEL_S3_KEY')
LOCAL_MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'uplift_model.pkl')


def load_model():
    # If S3 variables provided, download to /tmp and load
    if MODEL_S3_BUCKET and MODEL_S3_KEY:
        s3 = boto3.client('s3')
        tmp_path = '/tmp/uplift_model.pkl'
        try:
            s3.download_file(MODEL_S3_BUCKET, MODEL_S3_KEY, tmp_path)
            return joblib.load(tmp_path)
        except Exception as e:
            print(f"Failed to download/load model from s3://{MODEL_S3_BUCKET}/{MODEL_S3_KEY}: {e}")
            # fall through to local load

    # Try local packaged model
    try:
        return joblib.load(LOCAL_MODEL_PATH)
    except Exception as e:
        print(f"Error loading local model from {LOCAL_MODEL_PATH}: {e}")
        return None


# load once during cold start
model = load_model()


def lambda_handler(event, context):
    global model
    if model is None:
        # attempt reload in case env vars were set after cold start
        model = load_model()

    if model is None:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Model is not loaded."})
        }

    try:
        body = json.loads(event.get('body', '{}')) if isinstance(event, dict) else json.loads(event)
        # Expect features: age, income, number_of_transactions
        # Accept both snake_case and camelCase ids for flexibility in demos
        customer_id = body.get('customerId') or body.get('customer_id') or 'N/A'
        customer_features = pd.DataFrame([{
            'age': body.get('age'),
            'income': body.get('income'),
            'number_of_transactions': body.get('number_of_transactions')
        }])

        # handle different model interfaces
        try:
            uplift_score = model.predict(customer_features)
        except Exception:
            # some uplift models expect numpy arrays
            uplift_score = model.predict(customer_features.values)

        uplift_value = float(uplift_score[0])

        recommendation = 'TARGET' if uplift_value > 0.05 else 'DO_NOT_TARGET'

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "customerId": customer_id,
                "upliftScore": uplift_value,
                "recommendation": recommendation
            })
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
