run:
	uvicorn app_server:app --reload
test:
	pytest tests/