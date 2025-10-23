# Uplift Engine (VPBank Hackathon 2025)

AI-driven uplift modeling platform to optimize promotion campaigns and maximize ROI by targeting persuadable customers only. Built with a serverless-first AWS architecture and designed for batch, near real-time, and real-time use cases.

## What this repo contains (scaffold)

This is a minimal, runnable skeleton to start fast during the hackathon:

- research/ — Notes and algorithm choices for uplift/causal modeling
- data/ — Sample dataset for quick experiments
- src/lambda/ — Minimal real-time decisioning stub (Lambda-style handler)
- src/notebooks/ — Placeholders for data simulation and training
- docs/ — Documentation and diagram sources

## Quick start (local)

1) Python 3.10+ recommended. Create a virtual env.
2) Install Lambda stub dependencies:
	- In PowerShell: `pip install -r .\src\lambda\requirements.txt`
3) Run the local test script to simulate a decision call:
	- `python .\src\lambda\local_test.py`

Expected output: a JSON decision with an upliftScore and explanation reasons.

## Environment variables (used across components)

- AWS_REGION: AWS region for services (e.g., ap-southeast-1)
- MODEL_S3_PATH: s3://bucket/path/to/model.tar.gz (optional for stub; used when loading a trained model)

## Next steps

- Add notebooks for data simulation and uplift model training
- Replace the Lambda stub logic with a real model call and Rule Engine
- Add architecture.mmd and rendered diagram under docs/

## License

For hackathon use; do not include secrets. Configure everything via environment variables.
