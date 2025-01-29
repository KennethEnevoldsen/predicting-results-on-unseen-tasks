install:
	@echo "--- 🚀 Installing project dependencies ---"
	uv sync


install-uv:
	@echo "--- 🚀 Installing UV ---"	
	curl -LsSf https://astral.sh/uv/install.sh | sh
	# windows:
	# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

lint:
	@echo "--- 🧹 Running linters ---"
	uv run ruff format . 			# running ruff formatting
	uv run ruff check . --fix  	# running ruff linting

lint-check:
	@echo "--- 🧹 Check is project is linted ---"
	# Required for CI to work, otherwise it will just pass
	uv run ruff format . --check						    # running ruff formatting
	uv run ruff check **/*.py 						        # running ruff linting

test:
	@echo "--- 🧪 Running tests ---"
	uv run pytest src/tests

pr:
	@echo "--- 🚀 Running requirements for a PR ---"
	make lint
	make test
