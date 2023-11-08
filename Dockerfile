FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "model.bin", "dv.bin", "diamond_pred.py", "./"] 

RUN pipenv install --system --deploy

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--port=9696", "diamond_pred:app" ]