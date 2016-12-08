class Tracing(object):

	conn = None

	def __init__(self):
		self.cursor = self.conn.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS tracing (
			tracing_id BIGSERIAL PRIMARY KEY,
			viviendo_id BIGINT NOT NULL,
			date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
		)""")

		self.conn.commit()

	def create(self, request, *args, **kwargs):
		self.cursor.execute("""INSERT INTO tracing (viviendo_id)
			VALUES (%(viviendo_id)s)""", request)
		self.conn.commit()
		return True

	def list(self, request, *args, **kwargs):
		if kwargs.get('viviendo_id'):
			self.cursor.execute("SELECT * FROM tracing WHERE viviendo_id=%s" %(kwargs.get('viviendo_id')))
		else:
			self.cursor.execute("SELECT * FROM tracing")
		return self.cursor.fetchall()