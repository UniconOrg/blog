# Unicon Blog

## Instalacion

### DB
crea una db de postgrers con el comando

```bash
docker compose up db -d
```

Esto creara una DB con la conexion

```bash
postgresql://postgres:secret@localhost:5441/unicon-blog
```

### Instalacion de dependencias

Instala poetry

```bash
pip3 install poetry
poetry install --no-root
```

### Ejecuta las migracion 

```bash
cd src
python manage.py migrate
```

Si es necesario hacer nuevas migraciones

```bash
cd src
python manage.py makemigrations
```

## Ejecucion

Para ejecutar tu servicio sera con

```
cd src
python manage.py runserver 0.0.0.0:8002
```