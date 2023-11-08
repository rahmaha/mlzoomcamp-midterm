<h2 align="center">Diamond Price Prediction</h2>

<!-- ABOUT THE PROJECT -->

## About The Project

This is project for midterm in MLZoomcamp. The project is about predict diamond price based on some features. For this project, I use from Kaggle:

[https://www.kaggle.com/datasets/joebeachcapital/diamonds](https://www.kaggle.com/datasets/joebeachcapital/diamonds)

The dataset contain some features such as carat, cut, color, and others. You can find details description of each features in the above. Also, the dataset already downloaded and you can found it at `data/diamonds.csv`.

The aim of this project is to predict the price of diamonds based on the characteristics of the diamond such as color, cut and etc. This will be useful for customers who plan to buy diamonds at a jewelry store according to their wishes such as the color they want, the carat of the diamond or other things, so they can prepare an estimate for their money.

- For EDA and model training (and selection), can be found in `diamonds_price-prediction.ipynb`,
- Training of the final model is in the `train.py` script.
- And the deployment for model is in the `diamond_pred.py`. The model deployed as web service using Flask in a Docker container on AWS Elastic Beanstalk.

<!-- How to run the project -->

## How to run the project

1. First, you can clone the repo using the following command:

```sh
   git clone https://github.com/rahmaha/mlzoomcamp-midterm.git
```

or click at the `code button` and chose download zip

2. To run the project, you need to have python, jupyter notebook and pipenv in your computer/laptop. This project also has a few of packages that needed that detailed in Pipfile/Pipfile.lock. To install all these packages, you can use pipenv to create separete environtment for this project. Make sure you already installed it or if not you can run this command:

```sh
   pip install pipenv
```

Then open terminal and go to the path of folder which contain this project (Pipfile/Pipfile.lock), and then run this command to install all packages needed:

```sh
   pipenv install
```

3. Now that you already installed it, you can start using this new virtual environtment for this project, run this following command to activate it:

```sh
   pipenv shell
```

4. Next is run the scripts like you normally do.

<!-- How to submit request to the web service-->

## How to submit request to the web service

The diamond_pred.py script was deployed in the docker containter at AWS Elastic Beanstalk. Now, to submit request to web service to predict diamonds price you can make new script in python or jupyter notebook and give this following code:

```import requests

host = "mlzoomcamp-midterm-env.eba-znmnabvm.ap-southeast-1.elasticbeanstalk.com"
url = f"http://{host}/diamonds_pred"

diamond = {'carat': 0.27,
           'cut': "Premium",
           'color': 'I',
           'clarity': 'SI1'}

response = requests.post(url, json=diamond).json()
print('Estimated diamond price: ', response.get('predicted_price'))
```

or if you feel lazy, you can just run `test.py` script. It has same code in it. And it will return estimated of diamond price.

Above, is just an example. You can try different combination between 'carat', 'cut', 'color' and 'clarity'.

- Carat: is a measure of diamond weight. One carat is equivalent to 0.2 grams.
- Cut: refers to how a rough diamond is shaped into a finished diamond
- Color: refers to the color of the diamond. Colorless diamonds are considered better than diamonds with a yellow tint. diamonds contains diamonds of 7 different colors, represented by different letters. “D” - “F” diamonds are considered colorless, while “G” - “J” diamonds have a very faint color.
- Clarity: refers to how clear a diamond is. Clarity contains 8 ordered levels, from “I1” (the worst) to “IF” (the best).

Below are the table that contain of diffent types for cut, color and clarity:

|    cut    | color | clarity |
| :-------: | :---: | :-----: |
|   Ideal   |   E   |   SI2   |
|  Premium  |   I   |   SI1   |
|   Good    |   J   |   VS1   |
| Very Good |   H   |   VS2   |
|   Fair    |   F   |  VVS2   |
|           |   G   |  VVS1   |
|           |   D   |   I1    |
|           |       |   IF    |

- cut has 5 types,
- color has 7 types
- clarity has 8 types

`Notes:` Make sure to copy the same as in the table if you want to try different type of diamonds
