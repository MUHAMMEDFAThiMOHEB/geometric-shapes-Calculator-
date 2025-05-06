FROM python:3.11-slim
WORKDIR /apps
COPY geometric_cal.py .
CMD ["python", "geometric_cal.py"]