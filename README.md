# ins-life-exp-pred-aws

# Deployment

## Preparation

Run `insurance_life_expectancy_pred.ipynb` to generate the joblib file.

## Running without Docker

Install flask:

```bash
pip install flask
```

Run the service:

```bash
python ins_life_exp_pred_app.py
```

Test it from python:

```python
data = {'const': 1.0,
 'Year': 2011.0,
 'Adult Mortality': 464.0,
 'Alcohol': 6.0,
 'Percentage expenditure': 63.75053034,
 'Hepatitis B': 94.0,
 'BMI': 29.9,
 'Under-five deaths': 42.0,
 'Polio': 93.0,
 'Diphtheria': 93.0,
 'HIV/AIDS': 13.3,
 'Thinness 5-9 years': 6.7,
 'Income composition of resources': 0.452,
 'Schooling': 10.1,
 'Status_Developing': 1.0,
 'Continent_Asia': 0.0,
 'Continent_Europe': 0.0,
 'Continent_North America': 0.0,
 'Continent_Oceania': 0.0,
 'Continent_South America': 0.0}

# Testing the code 
import requests
url = 'http://localhost:3333/predict'
response = requests.post(url, json=data)
result = response.json()

# Testing the code after deploying in AWS
import requests
url = 'http://ins-serving-env.eba-7xyhhmuc.eu-west-2.elasticbeanstalk.com/predict'
response = requests.post(url, json=data)
result = response.json()
```

## Managing dependencies with Pipenv

Install `pipenv`:

```bash
pip install pipenv
```

Install the depencencies from the [Pipfile](Pipfile):

```bash
pipenv install
```

Enter the pipenv virtual environment:

```bash
pipenv shell
```

And run the code:

```bash
python ins_life_exp_pred_app.py
```

Alternatively, you can do both steps with one command:

```bash
pipenv run python ins_life_exp_predd_app.py
```

Now you can use the same code for testing the model locally.


## Running with Docker

Build the image (defined in [Dockerfile](Dockerfile))

```bash
docker build -t ins-service:v01 .
```

Run it:

```bash
docker run -it -p 3333:3333 ins-service:v01
```