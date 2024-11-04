from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/negative-sum/<string:num_1>/<string:num_2>',methods=['POST'])
def negative_sum(num_1,num_2):
    sum = int(num_1) + int(num_2)
    return jsonify({"sum":sum}), 200

if __name__ == '__main__':
    app.run(debug=True)
