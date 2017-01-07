import psycopg2, psycopg2.extras
from viviendo import Viviendo
from solicitud import Solicitud
from family import Family
from user import User
from tracing import Tracing

connection = psycopg2.connect(database='viviendo_db',user='postgres',
    password='demilovato', host='localhost')

models = ['Viviendo', 'Solicitud', 'Family', 'User', 'Tracing']

for model in models:
    conn = connection
    locals()[model+'Model'] = type('"'+model+'Model'+'"',
        (eval(model),), {'conn': conn})
