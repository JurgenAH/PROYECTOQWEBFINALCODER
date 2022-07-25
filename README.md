# PROYECTOQWEBFINALCODER

LINK SCREENSHOTS https://drive.google.com/file/d/1aGJvkzmVBzIslFoiiaAXvOVQ2ReayRah/view

LINK VIDEO https://youtu.be/PFCFEjo0MEM

INTEGRANTES 
ALMIRALLA HERANDEZ JURGEN: (LOGIN Y REGISTRO)
CONSTANTINO MELENDEZ JUAN: (CONTACTO Y BLOG)
ESPINOSA RODRIGUEZ ARANZA: (INICIO Y ABOUT US)

Proyecto de página web creada para la publicacion de noticias de los videojuegos

Documentos
Este proyecto fue programado con lenguaje Python y utilizando framework Django.

Se descarga plantilla de bootstrap, la cual se modifica y adapta para el proyecto a presentar.

Se realizan herencias de padre a hijo renderizando las vistas en la plantilla utilizada.

Inicio
Encontraremos una primera vista general de la página web

Archivos py:
models.py
Aquí encontramos el modelado de los objetos que se utilizaron para el proyecto y base de datos

forms.py
Se crearon los formularios necesarios para poder cargar datos en nuestra base de datos desde la página web

views.py
Son las vistas creadas a partir de nuestros modelos y formularios para navegar por la web

urls.py
Ubicación de las rutas utilizadas en el proyecto

Pasos para crear este proyecto.

Creamos las aplicaciones que ocuparemos que en este caso seran "CONTACTO, ABOUT US Y BLOG"
Dentro del este proyecto se crea su aplicación (python -m django startapp App), y se registra dentro de settings en: INSTALLED_APPS.

Se desarrollan los modelos y sus atributos.

Se crean los formularios de dichos modelos (o clases) en un archivo forms.py dentro de la App del proyecto.

Se descarga la plantilla bootstrap elegida y se adapta

Se programan las views del proyecto y se realiza CRUD.

Se cargan las plantillas html para visualizar nuestro proyecto en la web, dentro de la carpeta “templates” de la aplicación .

Se configuran las rutas  dentro de la aplicación 

Se configuran las rutas dentro del proyecto 

Se prueba el funcionamiento del framework utilizando: python manage.py runserver con éxito. Se cargan datos de prueba en todos los formularios, guardado correctamente.

Se crea un usuario: python manage.py createsuperuser para utilizar el administrador de la aplicación. Se ingresa correctamente al admin de la página web con el usuario y clave creados.

Dentro del archivo “admin.py” de la aplicación se crean los sitios de nuestros modelos para poder administrarlos .

Se confirma dentro del sitio de administración de Django que los modelos y sus datos se visualizan correctamente.

Se configura login, logout y registro

Se realizan pruebas en la página web y sitio de administración, se confirma su completo y correcto funcionamiento.


