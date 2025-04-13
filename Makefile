dev:
	uv run uvicorn prisma_python_sample.main:app --reload

test:
	uv run pytest

test-plan:
	uv run pytest --collect-only

migrate:
	uv run prisma db push

db-reset:
	rm database.db && make migrate
	