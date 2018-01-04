# Aplicación para el Departamento de Redes Populares del Ministerio del Poder Popular de Habita y Vivienda.

## Desarollada en python 2.7

### Descargar como zip:
click aquí: https://github.com/moisesdelacruz/departamento-de-vivienda/archive/master.zip

### Install on Linux

```sh
  git clone https://github.com/moisesdelacruz/departamento-de-vivienda.git

  cd departamento_de_vivienda/

  # build project
  python manage.py build

```

### Install on Windows

* Download or Clone

* Install dependencies of python
  - python-pip
  - libpq-dev
  - python-dev

* Install postgresql
  - Create database
  - Create user with password
  - Alter role from database to user

* Install dependencies of project
  ```sh
    # positioned in the root directory of the project.
    pip install -r requirements.txt
  ```

* Set environment variables
  ```txt
    DB_NAME=<db_name>
    DB_USER=<db_user>
    DB_PASS=<db_password>
    DB_HOST=<db_host>
  ```

### Crear Superusuario
```sh
  python manage.py createsuperuser
```

### Ejecucion
```sh
  python manage.py run
```
