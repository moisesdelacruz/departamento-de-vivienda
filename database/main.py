import psycopg2, psycopg2.extras
from viviendo import Viviendo
from solicitud import Solicitud
from family import Family
from user import User
from tracing import Tracing

connection = psycopg2.connect(database='viviendo_db',user='moises',
    password='christinagrimmie', host='localhost')

class ViviendoModel(Viviendo):

    conn = connection

class SolicitudModel(Solicitud):

    conn = connection

class FamilyModel(Family):

    conn = connection

class UserModel(User):

	conn = connection

class TracingModel(Tracing):

	conn = connection
