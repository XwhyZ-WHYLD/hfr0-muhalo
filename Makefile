.PHONY: test lint check benchmark

check:
@ruff check .
@pytest -q

lint:
@ruff check .

test:
@pytest -q

benchmark:
@python scripts/pist_benchmark.py
