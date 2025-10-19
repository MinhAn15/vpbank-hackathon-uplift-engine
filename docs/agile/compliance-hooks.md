# Compliance Hooks & Governance

## Approval Gates
- Human Approval in Step Functions before production promotion
- Security/IaC review for infra changes; model bias/ethics checklist

## Controls
- IAM least-privilege, KMS encryption, log retention (14–30 days)
- Model Cards for each version: purpose, data, metrics, limitations
- Do-no-harm guardrails enforced in realtime (hard/soft rules)

## Evidence
- PRs with checks, IaC plans, model evaluation reports stored in repo/S3
- Audit trail via CloudWatch Logs + artifact versioning (S3, Model Registry)
