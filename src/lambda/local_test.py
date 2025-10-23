import json
from app import lambda_handler


if __name__ == "__main__":
    body = {
        "customerId": 10002,
        "age": 42,
        "income": 27000000,
        "number_of_transactions": 12,
    }
    event = {"body": json.dumps(body, ensure_ascii=False)}
    res = lambda_handler(event, None)
    print(json.dumps(res, ensure_ascii=False))
