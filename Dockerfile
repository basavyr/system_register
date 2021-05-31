FROM python:latest
COPY . .
CMD ["tests/test_pipeline.py"]
ENTRYPOINT ["python3"]