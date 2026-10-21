"""Generate clearly synthetic Langmuir-like I-V curves for the demo notebook."""

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    voltage = np.linspace(-35.0, 35.0, 121)
    noise_levels = [0.002, 0.004, 0.006, 0.009, 0.015, 0.022, 0.035, 0.05,
                    0.07, 0.10, 0.14, 0.20, 0.27, 0.35, 0.45, 0.55]

    for curve_id, noise_level in enumerate(noise_levels, start=1):
        rng = np.random.default_rng(2026 + curve_id)
        electron_current = 2.5e-6 * np.exp(np.clip((voltage + 10.0) / 18.0, -20, 4))
        ion_current = 1.0e-8 * (voltage + 35.0) - 1.5e-7
        signal = ion_current + electron_current
        noise = rng.normal(0.0, noise_level * np.ptp(signal), size=voltage.size)
        measured_current = signal + noise

        # Add a few deliberately irregular curves to demonstrate screening.
        if curve_id in {13, 15}:
            measured_current[52:60] += 0.35 * np.ptp(signal)
        if curve_id == 16:
            measured_current[::9] *= -0.25

        pd.DataFrame({"voltage_v": voltage, "current_a": measured_current}).to_csv(
            DATA_DIR / f"sample_curve_{curve_id:03d}.csv", index=False
        )

    print(f"Generated {len(noise_levels)} synthetic curves in {DATA_DIR}")


if __name__ == "__main__":
    main()
