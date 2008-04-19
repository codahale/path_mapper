all: test

# Removes all pyc, pyo, *~ files.
clean:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '._*' -exec rm -f {} +

# Runs all unit tests.
test: clean
	@python tests/alltests.py

benchmark: clean
	@python benchmarks/run.py