FROM python:latest
COPY . .
ENTRYPOINT ["python3"]
CMD ["tests/test_pipeline.py"]