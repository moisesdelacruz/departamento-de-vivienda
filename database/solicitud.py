class Solicitud(object):

    conn = None

    def __init__(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS solicitud (
            solicitud_id BIGSERIAL PRIMARY KEY,
            viviendo_id BIGINT NOT NULL,
            housing_conditions VARCHAR(45),
            housing_direction VARCHAR(45),
            phone_number NUMERIC(15),
            residence_constancia BOOLEAN DEFAULT FALSE,
            copy_ci BOOLEAN DEFAULT FALSE,
            medical_reports BOOLEAN DEFAULT FALSE,
            housing_in_risk BOOLEAN DEFAULT FALSE,
            firefighters_constancy BOOLEAN DEFAULT FALSE,
            health_case BOOLEAN DEFAULT FALSE,
            copy_register_of_the_big_mision_vivienda BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

            UNIQUE("viviendo_id"),
            FOREIGN KEY ("viviendo_id") REFERENCES "viviendo"("viviendo_id")
        )""")

        self.conn.commit()

    def create(self, request, *args, **kwargs):
        self.cursor.execute("""INSERT INTO solicitud (viviendo_id,
            housing_conditions, housing_direction,
            phone_number, residence_constancia, copy_ci,
            medical_reports, housing_in_risk,
            firefighters_constancy, health_case,
            copy_register_of_the_big_mision_vivienda)
            VALUES (%(viviendo_id)s, %(housing_conditions)s, %(housing_direction)s,
            %(phone_number)s, %(residence_constancia)s, %(copy_ci)s,
            %(medical_reports)s, %(housing_in_risk)s,
            %(firefighters_constancy)s, %(health_case)s,
            %(copy_register_of_the_big_mision_vivienda)s)""", request)
    	self.conn.commit()
        return True

    def list(self, request, *args, **kwargs):
        self.cursor.execute("SELECT * FROM solicitud")
    	return self.cursor.fetchall()

    def retrive(self, request, *args, **kwargs):
        self.cursor.execute("SELECT * FROM solicitud WHERE viviendo_id=%s" %(request))
    	return self.cursor.fetchall()

    def update(self, request, *args, **kwargs):
        self.cursor.execute("""UPDATE solicitud SET housing_conditions=%(housing_conditions)s,
            housing_direction=%(housing_direction)s,
            phone_number=%(phone_number)s,
            residence_constancia=%(residence_constancia)s,
            copy_ci=%(copy_ci)s,
            medical_reports=%(medical_reports)s,
            housing_in_risk=%(housing_in_risk)s,
            firefighters_constancy=%(firefighters_constancy)s,
            health_case=%(health_case)s,
            copy_register_of_the_big_mision_vivienda=%(copy_register_of_the_big_mision_vivienda)s
            WHERE viviendo_id=%(viviendo_id)s""", request)
        self.conn.commit()
        return True

    def createOrUpdate(self, request, *args, **kwargs):
        self.cursor.execute("""UPDATE solicitud SET housing_conditions=%(housing_conditions)s,
          housing_direction=%(housing_direction)s,
          phone_number=%(phone_number)s,
          residence_constancia=%(residence_constancia)s,
          copy_ci=%(copy_ci)s,
          medical_reports=%(medical_reports)s,
          housing_in_risk=%(housing_in_risk)s,
          firefighters_constancy=%(firefighters_constancy)s,
          health_case=%(health_case)s,
          copy_register_of_the_big_mision_vivienda=%(copy_register_of_the_big_mision_vivienda)s WHERE viviendo_id=%(viviendo_id)s;
        INSERT INTO solicitud (viviendo_id,
                      housing_conditions, housing_direction,
                      phone_number, residence_constancia, copy_ci,
                      medical_reports, housing_in_risk,
                      firefighters_constancy, health_case,
                      copy_register_of_the_big_mision_vivienda)
               SELECT %(viviendo_id)s, %(housing_conditions)s, %(housing_direction)s,
                %(phone_number)s, %(residence_constancia)s, %(copy_ci)s,
                %(medical_reports)s, %(housing_in_risk)s,
                %(firefighters_constancy)s, %(health_case)s,
                %(copy_register_of_the_big_mision_vivienda)s
               WHERE NOT EXISTS (SELECT 1 FROM solicitud WHERE viviendo_id=%(viviendo_id)s);""", request)
        self.conn.commit()
        return True

    def delete(self, request, *args, **kwargs):
        self.cursor.execute("DELETE FROM solicitud WHERE viviendo_id=%s" %(request))
        self.conn.commit()
        return True
