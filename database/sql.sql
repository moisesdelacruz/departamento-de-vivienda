-- Viviendo
CREATE TABLE IF NOT EXISTS viviendo (
  viviendo_id BIGSERIAL PRIMARY KEY,
  ci INTEGER UNIQUE,
  first_name VARCHAR(45),
  last_name VARCHAR(45),
  direction TEXT,
  birthday DATE,
  sex VARCHAR(45),
  estado_civil VARCHAR(45),
  work BOOLEAN DEFAULT FALSE,
  entry DECIMAL(5,2),
  postulation VARCHAR(45),
  discapacity BOOLEAN DEFAULT FALSE,
  discapacity_desc TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- viviendo add
INSERT INTO viviendo (ci, first_name, last_name, direction, birthday, sex,
  estado_civil, work, entry, postulation, discapacity, discapacity_desc)
  VALUES (%(ci)s, %(first_name)s, %(last_name)s, %(direction)s, %(birthday)s, %(sex)s,
    %(estado_civil)s, %(work)s, %(entry)s, %(postulation)s, %(discapacity)s,
    %(discapacity_desc)s);

-- viviendo update
UPDATE viviendo SET ci=%(ci)s,
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
  WHERE ci=%(ci)s

-- solicitud
CREATE TABLE IF NOT EXISTS solicitud (
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

  UNIQUE("solicitud_id"),
        FOREIGN KEY ("viviendo_id") REFERENCES "viviendo"("viviendo_id")
);

-- solicitud add
INSERT INTO solicitud (viviendo_id, housing_conditions, housing_direction,
  phone_number, residence_constancia, copy_ci,
  copy_register_of_the_big_mision_vivienda, housing_in_risk,
  firefighters_constancy, health_case, medical_reports)
  VALUES (%(viviendo_id)s, %(housing_conditions)s, %(housing_direction)s,
    %(phone_number)s, %(residence_constancia)s, %(copy_ci)s,
    %(copy_register_of_the_big_mision_vivienda)s, %(housing_in_risk)s,
    %(firefighters_constancy)s, %(health_case)s, %(medical_reports)s);

-- solicitud update
UPDATE solicitud SET housing_conditions=%(housing_conditions)s,
  housing_direction=%(housing_direction)s,
  phone_number=%(phone_number)s,
  residence_constancia=%(residence_constancia)s,
  copy_ci=%(copy_ci)s,
  copy_register_of_the_big_mision_vivienda=%(copy_register_of_the_big_mision_vivienda)s,
  housing_in_risk=%(housing_in_risk)s,
  firefighters_constancy=%(firefighters_constancy)s,
  health_case=%(health_case)s,
  medical_reports=%(medical_reports)s
  WHERE viviendo_id=%(viviendo_id)s


-- Create or update
CREATE FUNCTION createOrUpdate(key INT) RETURNS VOID AS
$$
BEGIN
    LOOP
        -- first try to update the key
        -- note that "a" must be unique
        UPDATE solicitud SET housing_conditions='casa casa',
          housing_direction='machincuepa',
          phone_number=0416,
          residence_constancia=TRUE,
          copy_ci=TRUE,
          copy_register_of_the_big_mision_vivienda=TRUE,
          housing_in_risk=TRUE,
          firefighters_constancy=TRUE,
          health_case=TRUE,
          medical_reports=TRUE WHERE viviendo_id = key;
        IF found THEN
            RETURN;
        END IF;
        -- not there, so try to insert the key
        -- if someone else inserts the same key concurrently,
        -- we could get a unique-key failure
        BEGIN
            INSERT INTO solicitud(viviendo_id,
              housing_conditions, housing_direction,
              phone_number, residence_constancia, copy_ci,
              copy_register_of_the_big_mision_vivienda, housing_in_risk,
              firefighters_constancy, health_case, medical_reports) VALUES (1,
              'housing_conditions', 'housing_direction',
              0416, TRUE, FALSE,
              FALSE, FALSE,
              FALSE, FALSE, FALSE);
            RETURN;
        EXCEPTION WHEN unique_violation THEN
            -- do nothing, and loop to try the UPDATE again
        END;
    END LOOP;
END;
$$
LANGUAGE plpgsql;

SELECT createOrUpdate(1);

-- Create if no existe form two
UPDATE solicitud SET housing_conditions=%(housing_conditions)s,
  housing_direction=%(housing_direction)s,
  phone_number=%(phone_number)s,
  residence_constancia=%(residence_constancia)s,
  copy_ci=%(copy_ci)s,
  medical_reports=%(medical_reports)s WHERE viviendo_id=%(viviendo_id)s;
  housing_in_risk=%(housing_in_risk)s,
  firefighters_constancy=%(firefighters_constancy)s,
  health_case=%(health_case)s,
  copy_register_of_the_big_mision_vivienda=%(copy_register_of_the_big_mision_vivienda)s,
INSERT INTO solicitud (viviendo_id,
              housing_conditions, housing_direction,
              phone_number, residence_constancia, copy_ci, medical_reports,
              housing_in_risk, firefighters_constancy, health_case,
              copy_register_of_the_big_mision_vivienda)
       SELECT %(viviendo_id)s, %(housing_conditions)s, %(housing_direction)s,
        %(phone_number)s, %(residence_constancia)s, %(copy_ci)s,
        %(copy_register_of_the_big_mision_vivienda)s, %(housing_in_risk)s,
        %(firefighters_constancy)s, %(health_case)s, %(medical_reports)s
       WHERE NOT EXISTS (SELECT 1 FROM solicitud WHERE viviendo_id=1);

-- ----------- --
-- family
CREATE TABLE IF NOT EXISTS family (
  family_id BIGSERIAL PRIMARY KEY,
  viviendo_id BIGINT NOT NULL,
  ci INTEGER UNIQUE,
  first_name VARCHAR(45),
  last_name VARCHAR(45),
  birthday DATE,
  work BOOLEAN DEFAULT FALSE,
  birth_state VARCHAR(45),
  entry DECIMAL(5,2),
  discapacity BOOLEAN DEFAULT FALSE,
  discapacity_desc TEXT,
  old_age BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  
  UNIQUE("family_id"),
                FOREIGN KEY ("viviendo_id") REFERENCES "viviendo"("viviendo_id")
);

-- family add
INSERT INTO family (viviendo_id, ci, first_name, last_name, birthday, work,
  birth_state, entry, discapacity, discapacity_desc, old_age)
  VALUES (%(viviendo_id)s, %(ci)s, %(first_name)s, %(last_name)s,
  %(birthday)s, %(work)s, %(birth_state)s, %(entry)s, %(discapacity)s,
  %(discapacity_desc)s, %(old_age)s);

-- family update
UPDATE solicitud SET viviendo_id
  ci=%(ci)s,
  first_name=%(first_name)s,
  last_name=%(last_name)s,
  birthday=%(birthday)s,
  work=%(work)s,
  birth_state=%(birth_state)s,
  entry=%(entry)s,
  discapacity=%(discapacity)s,
  discapacity_desc=%(discapacity_desc)s,
  old_age=%(old_age)s,
  WHERE viviendo_id=%(viviendo_id)s;


-- User Table
CREATE TABLE IF NOT EXISTS account (
  user_id BIGSERIAL PRIMARY KEY,
  username VARCHAR(45) NOT NULL UNIQUE,
  first_name VARCHAR(45),
  last_name VARCHAR(45),
  cedula INTEGER NOT NULL UNIQUE,
  permission VARCHAR(45) NOT NULL,
  password VARCHAR(60) NOT NULL
);

INSERT INTO account (username, first_name, last_name, cedula, permission, password)
  VALUES (%(username)s, %(first_name)s, %(last_name)s, %(cedula)s, %(permission)s, %(password)s);

UPDATE account SET
  username=%(username)s,
  first_name=%(first_name)s,
  last_name=%(last_name)s,
  cedula=%(cedula)s,
  permission=%(permission)s,
  password=%(password)s,
  WHERE user_id=%(user_id)s;
