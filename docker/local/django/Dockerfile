FROM python:3.10-slim

WORKDIR /app

COPY requirements /app/requirements
RUN pip install --no-cache-dir -r requirements/development.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
