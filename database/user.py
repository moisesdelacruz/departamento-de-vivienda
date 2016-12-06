class User(object):

    conn = None

    def __init__(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS account (
            user_id BIGSERIAL PRIMARY KEY,
            username VARCHAR(45) NOT NULL UNIQUE,
            first_name VARCHAR(45),
            last_name VARCHAR(45),
            cedula INTEGER NOT NULL UNIQUE,
            is_superuser BOOLEAN DEFAULT FALSE,
            permission VARCHAR(45) NOT NULL,
            password VARCHAR(60) NOT NULL
        )""")

        self.conn.commit()

    def create(self, request, *args, **kwargs):
        self.cursor.execute("""INSERT INTO account (username,
            first_name, last_name, cedula, permission, is_superuser, password)
            VALUES (%(username)s, %(first_name)s, %(last_name)s,
                %(cedula)s, %(permission)s, %(is_superuser)s, %(password)s)""", request)
    	self.conn.commit()
        return True

    def list(self, *args, **kwargs):
        self.cursor.execute("SELECT * FROM account")
    	return self.cursor.fetchall()

    def retrive(self, request, *args, **kwargs):
        if not kwargs.get('field'):
            raise ValueError('You must specify a "field" attribute to perform the search.')
        field = kwargs.get('field')
        self.cursor.execute("SELECT * FROM account WHERE %s='%s'" %(field, request))
        return self.cursor.fetchall()

    def update(self, request, *args, **kwargs):
        self.cursor.execute("""UPDATE account SET
            username=%(username)s,
            first_name=%(first_name)s,
            last_name=%(last_name)s,
            cedula=%(cedula)s,
            permission=%(permission)s,
            is_superuser=%(is_superuser)s,
            password=%(password)s
            WHERE user_id=%(user_id)s""", request)
        self.conn.commit()
        return True

    def delete(self, request, *args, **kwargs):
        self.cursor.execute("DELETE FROM account WHERE user_id=%s" %(request))
        self.conn.commit()
        return True