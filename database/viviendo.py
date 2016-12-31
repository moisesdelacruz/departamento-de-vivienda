class Viviendo(object):

	conn = None

	def __init__(self):
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS viviendo (
			viviendo_id BIGSERIAL PRIMARY KEY,
			ci INTEGER UNIQUE,
			first_name VARCHAR(45),
			last_name VARCHAR(45),
			birthday DATE,
			sex VARCHAR(45),
			estado_civil VARCHAR(45),
			instructional_level VARCHAR(45),
			work BOOLEAN DEFAULT FALSE,
			occupation VARCHAR(45),
			institution VARCHAR(45),
			entry DECIMAL,
			direction TEXT,
			postulation VARCHAR(45),
			discapacity BOOLEAN DEFAULT FALSE,
			discapacity_desc TEXT,
			created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
		)""")

		self.conn.commit()

	def create(self, request, *args, **kwargs):
		self.cursor.execute("""INSERT INTO viviendo (ci, first_name, last_name,
			birthday, sex, estado_civil, instructional_level, work, occupation,
			institution, entry, direction, postulation,
			discapacity, discapacity_desc) VALUES (%(ci)s, %(first_name)s,
			%(last_name)s, %(birthday)s, %(sex)s, %(estado_civil)s,
			%(instructional_level)s, %(work)s, %(occupation)s, %(institution)s,
			%(entry)s, %(direction)s, %(postulation)s, %(discapacity)s,
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
			birthday=%(birthday)s,
			sex=%(sex)s,
			estado_civil=%(estado_civil)s,
			instructional_level=%(instructional_level)s,
			work=%(work)s,
			occupation=%(occupation)s,
			institution=%(institution)s,
			entry=%(entry)s,
			direction=%(direction)s,
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
