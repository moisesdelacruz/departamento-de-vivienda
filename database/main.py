import psycopg2, psycopg2.extras
import os
from viviendo import Viviendo
from solicitud import Solicitud
from family import Family
from user import User
from tracing import Tracing

DB_NAME = os.getenv('DB_NAME') or 'viviendo_db'
DB_USER = os.getenv('DB_USER') or 'viviendo_user'
DB_PASS = os.getenv('DB_PASS') or 'viviendo_pass'
DB_HOST = os.getenv('DB_HOST') or 'localhost'

connection = psycopg2.connect(database=DB_NAME, user=DB_USER,
    password=DB_PASS, host='localhost')

models = ['Viviendo', 'Solicitud', 'Family', 'User', 'Tracing']

for model in models:
    conn = connection
    locals()[model+'Model'] = type('"'+model+'Model'+'"',
        (eval(model),), {'conn': conn})
