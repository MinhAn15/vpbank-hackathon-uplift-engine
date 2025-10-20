Demo commands — Uplift Engine (pwsh)

Notes
- Replace the URL with the real API Gateway/Lambda endpoint for your demo.
- The model expects a JSON with `customer_id` (or `customerId`), and features: `age`, `income`, `number_of_transactions`.

Example using pwsh (Invoke-RestMethod)

$body = @{
    customer_id = 123456
    age = 35
    income = 50000
    number_of_transactions = 12
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri 'https://api.example/scoring' -Body $body -ContentType 'application/json'

Example using curl (pwsh)

curl -X POST https://api.example/scoring -H 'Content-Type: application/json' -d '{"customer_id":123456,"age":35,"income":50000,"number_of_transactions":12}'

Local test (run against the lambda stub in repo)
- If you want to test locally, run (pwsh):

python - << 'PY'
from src.lambda import app
print(app.lambda_handler({'body': '{"customer_id":1, "age":30, "income":40000, "number_of_transactions":5}'}, None))
PY

Fallback demo (if live API fails)
- Show the Qini plot: `docs/qini_curve.png`.
- Show ROI chart: `docs/roi_bar.png`.
