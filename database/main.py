import psycopg2, psycopg2.extras
from viviendo import Viviendo
from solicitud import Solicitud
from family import Family
from user import User

connection = psycopg2.connect(database='viviendo_db',user='postgres',
    password='demilovato', host='localhost')

class ViviendoModel(Viviendo):

    conn = connection

class SolicitudModel(Solicitud):

    conn = connection

class FamilyModel(Family):

    conn = connection

class UserModel(User):

	conn = connection