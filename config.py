from dotenv import load_dotenv
import os

load_dotenv()
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'postgresql://flask_test_1g1t_user:YlMmAiMQdJbyWPoZDlzx5JUExfLUgp29@dpg-csl5usrtq21c73f7fnf0-a.oregon-postgres.render.com/flask_test_1g1t'
    DEBUG = True