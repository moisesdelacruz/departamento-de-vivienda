class Viviendo(object):

	conn = None

	def __init__(self):
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS viviendo (
			viviendo_id BIGSERIAL PRIMARY KEY,
			ci INTEGER UNIQUE,
			first_name VARCHAR(45),
			last_name VARCHAR(45),
			direction TEXT,
			birthday DATE,
			sex VARCHAR(45),
			estado_civil VARCHAR(45),
			work BOOLEAN DEFAULT FALSE,
			entry DECIMAL(10,4),
			postulation VARCHAR(45),
			discapacity BOOLEAN DEFAULT FALSE,
			discapacity_desc TEXT,
			created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
		)""")

		self.conn.commit()

	def create(self, request, *args, **kwargs):
		self.cursor.execute("""INSERT INTO viviendo (ci, first_name, last_name,
			direction, birthday, sex, estado_civil, work, entry, postulation,
			discapacity, discapacity_desc) VALUES (%(ci)s, %(first_name)s,
			%(last_name)s, %(direction)s, %(birthday)s, %(sex)s, %(estado_civil)s,
			%(work)s, %(entry)s, %(postulation)s, %(discapacity)s,
			%(discapacity_desc)s)""", request)
		self.conn.commit()
		return True

	def list(self, request, *args, **kwargs):
		self.cursor.execute("SELECT * FROM viviendo")
		return self.cursor.fetchall()

	def retrive(self, request, *args, **kwargs):
		if not kwargs.get('field'):
			raise ValueError('You must specify a "field" attribute to perform the search.')
		field = kwargs.get('field')
		self.cursor.execute("SELECT * FROM viviendo WHERE %s=%s" %(field, request))
		return self.cursor.fetchall()

	def update(self, request, *args, **kwargs):
		self.cursor.execute("""UPDATE viviendo SET ci=%(ci)s,
			first_name=%(first_name)s,
			last_name=%(last_name)s,
			direction=%(direction)s,
			birthday=%(birthday)s,
			sex=%(sex)s,
			estado_civil=%(estado_civil)s,
			work=%(work)s,
			entry=%(entry)s,
			postulation=%(postulation)s,
			discapacity=%(discapacity)s,
			discapacity_desc=%(discapacity_desc)s
			WHERE viviendo_id=%(id)s""", request)
		self.conn.commit()
		return True

	def delete(self, request, *args, **kwargs):
		self.cursor.execute("DELETE FROM viviendo WHERE ci=%s" %(request))
		self.conn.commit()
		return True
