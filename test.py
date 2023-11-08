import requests

host = "mlzoomcamp-midterm-env.eba-znmnabvm.ap-southeast-1.elasticbeanstalk.com"
url = f"http://{host}/diamonds_pred"

diamond = {'carat': 0.27,
           'cut': "Premium",
           'color': 'I',
           'clarity': 'SI1'}

response = requests.post(url, json=diamond).json()
print('Estimated diamond price: ', response.get('predicted_price'))
