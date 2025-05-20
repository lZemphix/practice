FROM python:3.13.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN ./practice/manage.py makemigrations
RUN ./practice/manage.py migrate
ENTRYPOINT [ "./practice/manage.py", "runserver", "8000" ]
