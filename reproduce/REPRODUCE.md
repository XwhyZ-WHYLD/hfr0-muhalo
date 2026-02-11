# Reproduction Guide

Tested on:

- Ubuntu 22.04
- Python 3.11
- Wired network
- API latency < 20ms

Steps:

1. git clone https://github.com/XwhyZ-WHYLD/hfr0-muhalo
2. cd hfr0-muhalo
3. pip install -r requirements.txt
4. python scripts/run_truthfulqa.py --config configs/default.yaml
5. python scripts/ablation.py

Expected output checksum:
truthfulqa_seed42_2026-02-11.json
SHA256: 9f7a...

