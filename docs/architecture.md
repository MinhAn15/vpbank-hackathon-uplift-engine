# Architecture Diagram — Uplift Engine

This document accompanies the architecture visuals. Source of truth for automation is `docs/images/architecture.mmd` (Mermaid) rendered via `docs/images/render-architecture.ps1`. The legacy `docs/architecture.drawio` can be used for alternate editing if needed.

## Required components and flows

1. Data Flow
   - Kinesis Data Streams -> S3 Data Lake -> AWS Glue -> SageMaker Feature Store

2. MLOps Training Pipeline (orchestrated with Step Functions)
   - AWS Step Functions: Glue Job -> SageMaker Training Job -> SageMaker Model Registry

3. Real-time Inference
   - Client App -> API Gateway -> Lambda -> (SageMaker Online Feature Store) -> SageMaker Endpoint -> Client App

4. Analytics
   - S3 Data Lake & SageMaker Offline Store -> Amazon Athena -> Amazon QuickSight

## How to create/update the visual diagram
Preferred (Mermaid CLI)
- Edit `docs/images/architecture.mmd`.
- Render PNG (pwsh):
   - From repo root, run `docs/images/render-architecture.ps1 -Transparent` (requires Mermaid CLI; the script prints the exact command it runs).
   - Output: `docs/images/architecture.png`.

Alternate (Draw.io)
- Install the "Draw.io Integration" extension in VS Code (or use draw.io desktop).
- Open `docs/architecture.drawio` and edit. Export as PNG to `docs/architecture.png`.

## Exporting the diagram
- Mermaid: run the PowerShell script as above.
- Draw.io: export PNG and save to `docs/architecture.png`.

## Commit & Push (pwsh)
Run these in the VS Code terminal (pwsh):

```powershell
git add docs/architecture.drawio docs/architecture.png
git commit -m "feat(arch): Add system architecture diagram for Uplift Engine"
git push
```

## Presentation tip
When presenting, narrate the system: "This is an Event-Driven, Serverless architecture optimized for <100ms per personalization request. We use SageMaker Feature Store to eliminate training-serving skew."