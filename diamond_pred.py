import pickle
import numpy as np
from flask import Flask, request, jsonify

dv_path = 'dv.bin'
model_path = 'model.bin'
# load and read file


def load_file(file):
    with open(file, 'rb') as f_in:
        return pickle.load(f_in)


dv = load_file(dv_path)
model = load_file(model_path)


app = Flask("diamonds-predict")


@app.route("/diamonds_pred", methods=['POST'])
def diamonds_pred():
    diamond = request.get_json()
    X_diamond = dv.transform(diamond)
    y_pred = (model.predict(X_diamond))
    get_price = np.expm1(y_pred)
    price = int(get_price.round(0)[0])

    result = {
        "predicted_price": price
    }
    return (jsonify(result))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
