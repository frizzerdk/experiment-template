# Template Experiment Makefile
# Usage: make <target>

# Variables
UV_RUN = uv run
PYTHON = $(UV_RUN) python
PYTEST = $(UV_RUN) pytest

.PHONY: install sync setup pytest python clean

install:
	uv sync

sync:
	$(PYTHON) scripts/sync_template.py
	@echo "✅ Template synced"

pytest:
	$(PYTEST) $(ARGS)

python:
	$(PYTHON) $(ARGS)

clean:
	rm -rf outputs/artifacts/*
	rm -rf outputs/models/*
	rm -rf outputs/plots/*
	rm -rf src/*.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	@echo "✅ Cleaned up"

setup: install sync


