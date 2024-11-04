from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
ma = Marshmallow(app)

class Numbers(ma.Schema):
    num_1 = fields.Integer(required=True)
    num_2 = fields.Integer(required=True)

    class meta():
        fields = ("num1", "num2")

number_schema = Numbers()


@app.route('/negative-sum',methods=['POST'])
def negative_sum():
    numbers = number_schema.load(request.json)
    num_1 = numbers['num_1']
    num_2 = numbers['num_2']
    sum = num_1 + num_2
    return jsonify({"sum":sum})

if __name__ == '__main__':
    app.run(debug=True)
