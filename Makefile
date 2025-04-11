dev:
	uv run uvicorn prisma_python_sample.main:app --reload

test:
	uv run pytest
