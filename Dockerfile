FROM python:3.10

RUN pip install pipenv gunicorn

ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app

COPY /Insurance_Life_Expectancy .

RUN pipenv install --deploy --system 

EXPOSE 3333

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:3333", "ins_life_exp_pred_app:app"] 