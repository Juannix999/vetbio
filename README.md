# VetBio Red — Proyecto Django (VetBio)

Proyecto de práctica para la materia de Programación Back End: modelado de una red veterinaria con Django, reglas de negocio en los modelos y comandos para poblar datos de prueba.

## Qué tiene de interesante
- Modelos: Tutor, Mascota, Servicio, Atencion, DetalleAtencion.
- Reglas de negocio implementadas en los modelos (validaciones y cálculos).
- Comando `seed_vetbio` que genera datos de ejemplo con Faker.
- API REST mínima con Django REST Framework (endpoints para tutores, servicios, mascotas y atenciones).
- Señales para recalcular `Atencion.monto_total` cuando cambian los detalles.

## Stack
- Python 3 + Django 5.2
- SQLite (por defecto para desarrollo)
- Django REST Framework
- Faker (para datos de prueba)

## Ejecutar localmente (rápido)
Desde la raíz del repo:

```bash
# clonar
git clone https://github.com/Juannix999/vetbio.git
cd vetbio

# crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# instalar dependencias
pip install -r requirements.txt

# migraciones
python manage.py makemigrations
python manage.py migrate

# generar datos de ejemplo
python manage.py seed_vetbio

# crear superusuario (opcional, para el admin)
python manage.py createsuperuser

# ejecutar servidor
python manage.py runserver
```

Notas:
- `vet_project/settings.py` lee `DJANGO_SECRET_KEY` y `DJANGO_DEBUG` desde variables de entorno; si no están definidas, usa valores por defecto apropiados para desarrollo.

## Endpoints (API)
Con el servidor en marcha, los endpoints disponibles son (ejemplos):

- Admin UI: http://127.0.0.1:8000/admin/
- API base: http://127.0.0.1:8000/api/
  - GET /api/tutores/
  - GET /api/servicios/
  - GET /api/mascotas/
  - GET /api/atenciones/  (cada atención incluye `detalles` con `monto_linea`)

Puedes usar `curl`, Postman o la interfaz de browsable API que viene con DRF.

## Tests
Ejecuta:

```bash
python manage.py test
```

Los tests incluyen validaciones clave (fecha de nacimiento no futura) y el cálculo de `monto_total` tras crear detalles.

## Seguridad y limpieza del repositorio
- He añadido `.gitignore` para evitar subir `db.sqlite3` en adelante.
- Si quieres eliminar `db.sqlite3` del historial del repositorio (recomendado para no compartir datos/binarios en commits anteriores), sigue la sección "Eliminar db.sqlite3 del historial" más abajo.

## Cómo eliminar db.sqlite3 del historial (pasos seguros, locales)
IMPORTANTE: Esto reescribe el historial Git y requiere forzar push al remoto. Todos los colaboradores deberán volver a clonar o sincronizar después. Haz una copia de seguridad antes de continuar.

Opción recomendada: git-filter-repo (más rápido y moderno)

```bash
# 1) Haz una rama de backup y súbela
git checkout --orphan temp-branch
git commit --allow-empty -m "backup before filter"
git branch -m backup-before-filter
git push origin backup-before-filter

# 2) Instala git-filter-repo (si no lo tienes). En muchas distros:
# pip install git-filter-repo

# 3) Clona el repo en un directorio nuevo (recomendado)
git clone --mirror https://github.com/Juannix999/vetbio.git
cd vetbio.git

# 4) Ejecuta filter-repo para eliminar db.sqlite3
git filter-repo --path db.sqlite3 --invert-paths

# 5) Fuerza el push de las ramas y tags limpias al remoto
git push --force --all
git push --force --tags

# 6) Limpia caches locales si es necesario
# (En el clon local normal)
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

Alternativa con BFG Repo-Cleaner:

```bash
# Clona espejo
git clone --mirror https://github.com/Juannix999/vetbio.git
cd vetbio.git

# Ejecuta BFG para eliminar el archivo
bfg --delete-files db.sqlite3

# Limpiar y forzar push
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

Consecuencias y recomendaciones:
- Reescribir el historial cambia los SHAs de todos los commits; después del push forzado, cualquier clon antiguo quedará desincronizado. Los colaboradores deberán volver a clonar.
- Asegúrate de avisar y coordinar con cualquier otra persona que tenga acceso al repositorio.
- Después de limpiar el historial, haz una release o crea una etiqueta para marcar el punto de referencia limpio.

Si quieres, yo te guío paso a paso y puedo generar los comandos exactos para tu entorno o crear un script bash que haga las operaciones (tú deberás ejecutarlo localmente porque requiere credenciales y un push forzado).

## Siguientes pasos recomendados (para portfolio)
- Añadir CI (GitHub Actions) que ejecute tests en cada push.
- Añadir Dockerfile / docker-compose para demo reproducible.
- Fijar versiones en `requirements.txt` (p. ej. `pip freeze > requirements.txt`).
- Actualizar README con screenshots o response samples de la API para que reclutadores vean resultados sin ejecutar nada.

---

Si quieres que actualice el README con tus datos personales (nombre, contacto, link a demo o captura) dilo y lo incluyo. También puedo preparar el script para eliminar `db.sqlite3` del historial y darte las indicaciones exactas para ejecutarlo localmente (lo ejecuto desde tu máquina si me das permiso para que lo haga por ti; de lo contrario te doy los pasos).