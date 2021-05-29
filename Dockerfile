FROM python:latest
COPY . .
CMD ["test_pipeline.py"]
ENTRYPOINT ["python3"]