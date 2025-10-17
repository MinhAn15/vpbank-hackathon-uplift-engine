import joblib
import pandas as pd
import json
import os

# Attempt to load model from package-relative path
MODEL_PATH = os.environ.get('MODEL_PATH', os.path.join(os.path.dirname(__file__), '..', 'uplift_model.pkl'))
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model from {MODEL_PATH}: {e}")
    model = None


def lambda_handler(event, context):
    if not model:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Model is not loaded."})
        }

    try:
        body = json.loads(event.get('body', '{}'))
        # Expect features: age, income, number_of_transactions
        customer_features = pd.DataFrame([{
            'age': body.get('age'),
            'income': body.get('income'),
            'number_of_transactions': body.get('number_of_transactions')
        }])

        uplift_score = model.predict(customer_features)
        uplift_value = float(uplift_score[0])

        recommendation = 'TARGET' if uplift_value > 0.05 else 'DO_NOT_TARGET'

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "customerId": body.get('customerId', 'N/A'),
                "upliftScore": uplift_value,
                "recommendation": recommendation
            })
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
