FROM python:3.10.12-slim-bullseye                    
ENV PYTHONBUFFERED=1                    
ENV PORT 8080                          
WORKDIR /app
COPY . /app/                           
RUN pip install --upgrade pip
RUN pip install -r requirements.txt    
RUN ./manage.py migrate

CMD gunicorn djangoELT.wsgi:application --bind 0.0.0.0:"${PORT}"

EXPOSE ${PORT}    