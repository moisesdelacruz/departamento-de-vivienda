import psycopg2, psycopg2.extras
from viviendo import Viviendo
from solicitud import Solicitud
from family import Family

connection = psycopg2.connect(database='viviendo_db',user='moises',
    password='christinagrimmie', host='localhost')

class ViviendoModel(Viviendo):

    conn = connection

class SolicitudModel(Solicitud):

    conn = connection

class FamilyModel(Family):

    conn = connection
