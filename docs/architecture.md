# Architecture Diagram — Uplift Engine

This document accompanies `docs/architecture.drawio` and explains what to include in the diagram and how to export it.

## Required components and flows

1. Data Flow
   - Kinesis Data Streams -> S3 Data Lake -> AWS Glue -> SageMaker Feature Store

2. MLOps Training Pipeline (orchestrated with Step Functions)
   - AWS Step Functions: Glue Job -> SageMaker Training Job -> SageMaker Model Registry

3. Real-time Inference
   - Client App -> API Gateway -> Lambda -> (SageMaker Online Feature Store) -> SageMaker Endpoint -> Client App

4. Analytics
   - S3 Data Lake & SageMaker Offline Store -> Amazon Athena -> Amazon QuickSight

## How to create the visual diagram
- Install the "Draw.io Integration" extension in VS Code (or use draw.io online).
- Open `docs/architecture.drawio` and draw the AWS icons for each service. Label each icon clearly.
- Use solid arrows for data flow and dashed arrows for control/orchestration triggers.

## Exporting the diagram
- After finishing, export the diagram as PNG and save it to `docs/architecture.png`.

## Commit & Push (pwsh)
Run these in the VS Code terminal (pwsh):

```powershell
git add docs/architecture.drawio docs/architecture.png
git commit -m "feat(arch): Add system architecture diagram for Uplift Engine"
git push
```

## Presentation tip
When presenting, narrate the system: "This is an Event-Driven, Serverless architecture optimized for <100ms per personalization request. We use SageMaker Feature Store to eliminate training-serving skew."