
Solución de la Actividad de Recuperación - VetBio Red
Este proyecto es la solución para la actividad de recuperación de la asignatura Programación Back End de la carrera de Analista Programador. El objetivo principal fue modelar la base de datos de una red veterinaria llamada VetBio Red utilizando Django ORM y crear un comando de gestión para generar datos de prueba.

Estructura del Proyecto
El proyecto sigue una estructura estándar de Django:

vet_project/: El directorio raíz del proyecto que contiene la configuración principal.

vetbio/: La aplicación principal del proyecto donde se encuentra la lógica de negocio.

models.py: Contiene los modelos de la base de datos (Tutor, Mascota, Servicio, Atencion y DetalleAtencion).

management/commands/seed_vetbio.py: Un comando de gestión personalizado para poblar la base de datos con datos de prueba generados por la librería Faker.

Características Principales
Modelado de datos: Se han definido cinco modelos con sus atributos y relaciones, cumpliendo con las especificaciones del documento.

Reglas de negocio: Las reglas de negocio, como la validación de fechas de nacimiento y el cálculo automático de montos, están implementadas directamente en los modelos para asegurar la integridad de los datos.

Comando de gestión: El comando seed_vetbio permite limpiar la base de datos y generar automáticamente 10 tutores, entre 1 y 3 mascotas por tutor, 5 servicios básicos y 30 atenciones completas con sus detalles, facilitando las pruebas y demostraciones.

Guía de Uso
Sigue estos pasos para configurar y ejecutar el proyecto localmente:

1. Clonar el repositorio
Si aún no lo has hecho, clona este repositorio en tu máquina local.

Bash

git clone https://github.com/Juannix999/vetbio.git
2. Instalación de dependencias
Instala las librerías necesarias, Django y Faker.

Bash

pip install django faker
3. Migraciones
Aplica las migraciones para crear las tablas correspondientes a los modelos en tu base de datos. Asegúrate de estar en el directorio raíz del proyecto (vet_project).

Bash

python manage.py makemigrations vetbio
python manage.py migrate
4. Generación de datos de prueba
Ejecuta el comando de gestión para poblar la base de datos con los datos de ejemplo.

Bash

python manage.py seed_vetbio
Contacto
Para cualquier duda o comentario, puedes contactar al autor del proyecto.
