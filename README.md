# Aplicación para el Departamento de Redes Populares del Ministerio del Poder Popular de Habita y Vivienda.

## Desarollada en python 2.7

### Descargar como zip:
click aquí: https://gitlab.com/moisesdelacruz/departamento_de_vivienda/repository/archive.zip?ref=master

### Instalacion > dependencias del sistema
```sh
  sudo apt-get install python-pip

  sudo apt-get update
  
  sudo apt-get install libpq-dev python-dev
```

### Instalacion
```sh
  git clone https://gitlab.com/moisesdelacruz/departamento_de_vivienda.git

  cd departamento_de_vivienda/

  pip install -r requirements.txt

```

### Crear Superusuario
```sh
  python manage.py createsuperuser
```

### Ejecucion
````sh
  python manage.py run
```

### Configurar base de datos > postgresql
- Instalar Postgresql: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
- crear base de datos: viviendo_db
- ir a database/main.py y configurar el usuario de postgresql
