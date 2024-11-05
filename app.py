from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config.from_object(f'config.DevelopmentConfig')
db = SQLAlchemy(app)

class Sum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)
    result = db.Column(db.Integer)

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.result = num1 + num2

with app.app_context():
    db.create_all()

@app.route('/negative-sum/<string:num_1>/<string:num_2>',methods=['POST'])
def negative_sum(num_1,num_2):
    with Session(db.engine) as session:
        with session.begin():
            new_sum = Sum(num1=int(num_1),num2=int(num_2))
            session.add(new_sum)
            session.commit()
    return jsonify({"sum":num_1+num_2}), 200
