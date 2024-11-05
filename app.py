from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import select
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config.from_object(f'config.DevelopmentConfig')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Sum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)
    result = db.Column(db.Integer)

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.result = num1 + num2
    
class Schema(ma.Schema):
    id = fields.Integer()
    num1 = fields.Integer()
    num2 = fields.Integer()
    result = fields.Integer()

    class Meta():
        fields = ('id','num1','num2','result')

sums_schema = Schema(many=True)

with app.app_context():
    db.create_all()

@app.route('/negative-sum/<string:num_1>/<string:num_2>',methods=['POST'])
def negative_sum(num_1,num_2):
    with Session(db.engine) as session:
        with session.begin():
            new_sum = Sum(num1=int(num_1),num2=int(num_2))
            session.add(new_sum)
            session.commit()
    return jsonify({"sum":int(num_1)+int(num_2)}), 200

@app.route('/filter-by-results/<string:result>',methods=['GET'])
def filter_results(result):
    result = int(result)
    with Session(db.engine) as session:
        with session.begin():
            sums = session.query(Sum).all()
            return sums_schema.jsonify(sums)