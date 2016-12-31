class Family(object):

	conn = None

	def __init__(self):
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS family (
			family_id BIGSERIAL PRIMARY KEY,
			viviendo_id BIGINT NOT NULL REFERENCES viviendo(viviendo_id),
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
			birth_state VARCHAR(45),
			discapacity BOOLEAN DEFAULT FALSE,
			discapacity_desc TEXT,
			old_age BOOLEAN DEFAULT FALSE,
			created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
		)""")

		self.conn.commit()

	def create(self, request, *args, **kwargs):
		self.cursor.execute("""INSERT INTO family (viviendo_id, ci, first_name,
			last_name, birthday, sex, estado_civil, instructional_level, work,
			occupation, institution, entry, birth_state, discapacity,
			discapacity_desc, old_age)
			VALUES (%(viviendo_id)s, %(ci)s, %(first_name)s, %(last_name)s,
			%(birthday)s, %(sex)s, %(estado_civil)s, %(instructional_level)s,
			%(work)s, %(occupation)s, %(institution)s, %(entry)s, %(birth_state)s,
			%(discapacity)s, %(discapacity_desc)s, %(old_age)s)""", request)
		self.conn.commit()
		return True

	def list(self, *args, **kwargs):
		if kwargs.get('viviendo_id'):
			self.cursor.execute("SELECT * FROM family WHERE viviendo_id=%s" %(kwargs.get('viviendo_id')))
		else:
			self.cursor.execute("SELECT * FROM family")
		return self.cursor.fetchall()

	def retrive(self, request, *args, **kwargs):
		self.cursor.execute("SELECT * FROM family WHERE viviendo_id=%s" %(request))
		return self.cursor.fetchall()

	def update(self, request, *args, **kwargs):
		self.cursor.execute("""UPDATE family SET ci=%(ci)s,
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
			birth_state=%(birth_state)s,
			discapacity=%(discapacity)s,
			discapacity_desc=%(discapacity_desc)s,
			old_age=%(old_age)s
			WHERE family_id=%(id)s""", request)
		self.conn.commit()
		return True

	def delete(self, request, *args, **kwargs):
		self.cursor.execute("DELETE FROM family WHERE family_id=%s" %(request))
		self.conn.commit()
		return True
