FROM python:latest
COPY . .
CMD ["src/pipeline.py"]
ENTRYPOINT ["python3"]