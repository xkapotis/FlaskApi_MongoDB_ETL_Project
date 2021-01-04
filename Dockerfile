FROM  python:3.8

WORKDIR /app
COPY . .  

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["FlaskApi_Load_To_MongoAtlas.py"]