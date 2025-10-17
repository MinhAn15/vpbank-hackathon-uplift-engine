<!-- .github/copilot-instructions.md for vpbank-hackathon-uplift-engine -->
# Uplift Engine — AI agent playbook (concise)

Purpose: give AI coding agents immediate, actionable knowledge to be productive in this repo and during the hackathon.

- Quick context
  - Project: "Uplift Engine" — a Causal AI platform to optimize bank promotion campaigns (VPBank Hackathon 2025).
  - Workspace snapshot currently contains only `README.md`. Expect future folders: `/research`, `/data`, `/src`, `/docs`.

- What to do first
  - Open `README.md` for product intent and constraints.
  - Run a repo-wide search for `aws`, `s3`, `lambda`, `sagemaker`, `notebooks`, `package.json`, `requirements.txt` before large changes.

- Productivity rules (project-specific)
  - Preserve business-first tone: docs and README should emphasize ROI, uplift impact, and why choices matter.
  - Avoid adding heavy infra without minimal runnable examples. If you add services, include a small manifest (`requirements.txt` or `package.json`) and a one-paragraph "How to run locally" in that folder.
  - Use environment variables for all configuration (e.g., `AWS_REGION`, `S3_BUCKET`, `MODEL_S3_PATH`). Do not add credentials to the repo.

- Integrations & patterns to expect
  - Serverless + SageMaker oriented architecture (API Gateway + Lambda for real-time scoring; SageMaker or local model training; S3 for artifacts; Step Functions for pipeline orchestration).
  - Feature Store pattern: avoid training-serving skew; keep features consistent between offline and online code paths.

- Minimal examples to include when creating new code
  - Python service stub: `/src/lambda/app.py`, `/src/lambda/requirements.txt`, `/src/lambda/README.md` (show pwsh commands for Windows devs if helpful).
  - Example data: `/data/sample_data.csv` with columns: `customer_id,age,income,number_of_transactions,treatment,conversion`.
  - Notebooks: `/src/notebooks/1.0-data-simulation.ipynb`, `/src/notebooks/2.0-uplift-model-training.ipynb` (keep cells small and reproducible).

- The hackathon "winning formula" (short)
  - Emphasize product + business impact first (problem, targeted ROI). Then show technical depth (uplift/causal models), architecture (scalable on AWS), and a demo or metrics.

- Rapid roadmap (what agents can scaffold now)
  1. Add `/research` notes (e.g., `02_uplift_modeling.md`) summarizing key literature and chosen algorithms (`causalml`, `econml`).
  2. Add `/data/sample_data.csv` (simulated dataset) and a short notebook to generate it.
  3. Add a minimal training notebook using `pandas` + `causalml` or `econml` with `requirements.txt`.
  4. Add a `/src/lambda` stub that loads a pickled model from `MODEL_S3_PATH` (env var) and returns a JSON uplift score.

- Roles & files to help the team (explicit)
  - Team Lead: `research/01_problem_domain.md`, `docs/presentation.pdf`, ROI calculations in `docs/roi.xlsx`.
  - ML Scientist: `src/notebooks/*.ipynb`, `research/02_uplift_modeling.md`.
  - Cloud Engineer: `src/lambda/*`, `infra/` (optional), QuickSight dashboard notes in `docs/`.

- Safety & verification
  - Never commit secrets. Use env vars and document them.
  - For any runnable change, add a README with exact steps and a short pwsh command example for local runs on Windows.

- When merging or updating this file
  - If an upstream `.github/copilot-instructions.md` exists, merge conservatively: keep any concrete agent rules and extend with the hackathon playbook above.

If you want, I can now: create the recommended folder skeleton (`/research`, `/data`, `/src/notebooks`, `/src/lambda`) with example files and a `requirements.txt` for a minimal Python prototype.
