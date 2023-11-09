SHELL = /bin/bash

.PHONY: setup
setup:
	python3 -m venv ./venv && \
	source venv/bin/activate &&  \
	pip3 install -r requirements.txt

# run style formatting
.PHONY: format
format:
	black .

.PHONY: run
run: 
	python3 scripts/process.py

# Cleaning and removing unneccessary files
.PHONY: clean
clean: 
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".trash" | xargs rm -rf
	find . | grep -E ".vscode" | xargs rm -rf
	rm -f .coverage

# list of commands
.PHONY: help
help:
	@echo "Commands:"
	@echo "setup	: create and activate a virtual environment"
	@echo "format   : executes style formatting (optional)."
	@echo "clean    : deletes all unnecessary files "
	@echo "run   	: starts running the process."