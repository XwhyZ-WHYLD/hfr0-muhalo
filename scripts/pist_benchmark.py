"""Pist benchmark: HDI warm-up and synthetic drift evaluation."""

import json
import random
from pathlib import Path

from hfr0 import HDIDetector


def run_benchmark(seed: int = 42, num_steps: int = 200):
    random.seed(seed)
    detector = HDIDetector(window=20, tau=2.5)
    records = []

    for step in range(num_steps):
        base = 50 if step < num_steps // 2 else 80
        jitter = random.gauss(0, 10)
        delta = max(1, base + jitter)
        alarm = detector.update(int(delta))
        records.append({"step": step, "delta_ns": int(delta), "alarm": alarm})

    return {
        "seed": seed,
        "num_steps": num_steps,
        "hdi_threshold": detector.tau,
        "alarms": sum(r["alarm"] for r in records),
        "records": records[-20:],
    }


def main():
    output_path = Path("results/pist_benchmark_seed42.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary = run_benchmark(seed=42, num_steps=500)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)

    print(f"Wrote benchmark results to {output_path}")


if __name__ == "__main__":
    main()
