FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code 
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]