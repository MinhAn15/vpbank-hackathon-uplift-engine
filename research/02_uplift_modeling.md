# Uplift Modeling — approach and choices

Goal: maximize incremental profit by targeting persuadables. Avoid spend on sure things and lost causes.

Algorithms we will evaluate:
- Tree-based uplift: Uplift Random Forest, CatBoost Uplift
- Meta-learners: DR-Learner / X-Learner with calibrated propensity
- Causal forests (EconML): CausalForestDML, OrthoForest

Metrics:
- AUUC / Qini, Profit@K (VND), Incremental Conversion

Data correctness:
- Treatment/control parity, time-aware splits, point-in-time features

References:
- causalml (Uber) — practical uplift methods
- econml (MSR) — double ML and causal forests
