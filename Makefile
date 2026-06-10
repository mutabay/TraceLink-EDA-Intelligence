.PHONY: setup generate ingest analyze report dashboard test lint pipeline clean

setup:
	pip install -e ".[dev]"

generate:
	python scripts/generate_data.py

ingest:
	python -m app.cli ingest

analyze:
	python -m app.cli analyze

report:
	python -m app.cli report

dashboard:
	flask --app app.dashboard.app run --port 5000

test:
	pytest

lint:
	ruff check app/ tests/ && mypy app/

pipeline: generate ingest analyze report
	@echo "Pipeline complete."

clean:
	rm -rf data/demo/ reports/
