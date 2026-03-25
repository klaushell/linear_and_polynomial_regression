.PHONY: help run install clean venv venv-activate test setup info

PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

help:
	@echo "Available commands:"
	@echo "  make help          - Show this help"
	@echo "  make run           - Run linear_regression.py"
	@echo "  make install       - Install dependencies (uses venv if present)"
	@echo "  make clean         - Remove Python cache files"
	@echo "  make venv          - Create virtual environment"
	@echo "  make venv-activate - Print activation command"
	@echo "  make test          - Install deps and run the script"
	@echo "  make setup         - Create venv and install dependencies"
	@echo "  make info          - Show project info"

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run: install
	$(PY) linear_regression.py

setup: install
	@echo "Setup complete. Activate with: source $(VENV)/bin/activate"

test: install run

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

venv-activate:
	@echo "Run: source $(VENV)/bin/activate"

info:
	@echo "Project: Linear & polynomial regression (Tips or Iris)"
	@echo "Script: linear_regression.py"
	@echo "Datasets: tips (total_bill -> tip), iris (sepal -> petal length)"
