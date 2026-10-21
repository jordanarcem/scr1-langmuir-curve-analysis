# Langmuir Probe Curve Analysis — SCR-1 Project

Portfolio version of a university team project on computational analysis of Langmuir-probe I–V curves. The machine-learning workflow combines curve-quality indicators with Isolation Forest, PCA, K-means, and Random Forest.

> **Data note:** this repository contains only generated demonstration curves. It does not include SCR-1 measurements, laboratory records, theses, or the original report. The sample curves are for software demonstration and are not experimental results or physically validated measurements.

## Contents

- `notebooks/langmuir_curve_ml_demo.ipynb` — cleaned, output-free notebook with the analysis workflow.
- `scripts/generate_sample_data.py` — reproducibly generates example I–V curves.
- `data/` — generated CSV examples (synthetic).

## Run

```bash
python -m pip install -r requirements.txt
python scripts/generate_sample_data.py
jupyter notebook notebooks/langmuir_curve_ml_demo.ipynb
```

Run the notebook from the repository root so it can find `data/`. Its reports and plots are written to `results/`.

## Workflow

1. Load and validate I–V curves; bin and smooth voltage/current measurements.
2. Extract statistical and curve-shape features and estimate preliminary physical indicators.
3. Assign transparent heuristic quality labels for exploratory analysis.
4. Explore patterns with PCA and K-means, flag unusual curves with Isolation Forest, and compare heuristic labels with a Random Forest using cross-validation when sample counts permit.
5. Export feature/classification tables and diagnostic plots.

The quality labels are screening aids, not a substitute for expert review or validated plasma diagnostics. The demonstration data do not support scientific conclusions about the SCR-1.

## Project context

Developed as part of a computational physics course project at Instituto Tecnológico de Costa Rica. The public notebook is a curated, anonymized demonstration based on the team's workflow; identifying details and experimental inputs/outputs have been removed.
