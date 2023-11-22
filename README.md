# App que permite gestionar las ventas privadas de vehículos para "Avila Bikes" creada en Django"
Esta aplicación web es una herramienta que permite gestionar las ventas privadas de vehículos para Avila Bikes. La plataforma proporciona a los usuarios una interfaz intuitiva para explorar y reservar vehículos disponibles. Esta creada con Django y Bootstrap, y utiliza la base de datos, por defecto de Django, SQLite.

## Deployment:
El proyecto se encuentra desplegado en Google Cloud, y esta es la url: 
**https://django-avilapp.oa.r.appspot.com/**

## Funcionalidades Principales
- Inicio de Sesión/Registro de usuarios.
- Visualización de detalles de productos, incluyendo imágenes, descripciones y precios.
- Reserva de vehículos disponibles.
- Envío de e-mail con la confirmación y datos de la reserva. 

## Tecnologías Utilizadas:
-   **Django**: Framework web de alto nivel en Python.
-   **Bootstrap**: Framework de diseño front-end para una interfaz atractiva y responsiva.

## Cómo utilizar el programa
Para utilizar esta app, sigue estos pasos:

1. Clona este repositorio en tu máquina local.

2. Crea un entorno virtual e instala las dependencias del proyecto:
**pip install -r requeriments.txt**

3. Realiza las migraciones de la base de datos:
**python manage.py migrate**

4. Crea un superusuario para acceder al panel de administración:
**python manage.py createsuperuser**

5. Inicia el servidor local:
**python manage.py runserver**

6. Accede a la aplicación desde tu navegador en http://127.0.0.1:8000/

7. Para acceder al panel de administración, ingresa a http://127.0.0.1:8000/admin/ y utiliza las credenciales del superusuario creado.

---
Pagina Principal:
![Captura de pantalla 2023-11-15 152612](https://github.com/paoladenic/django_avila/assets/126211693/a5679a6e-d069-44e1-a086-6f4088dfa8d2)
Login de usuario:
![Captura de pantalla 2023-11-15 152649](https://github.com/paoladenic/django_avila/assets/126211693/0d457a7d-0aad-4eae-8bba-6d86f654137c)
Catálogo:
![Captura de pantalla 2023-11-15 152752](https://github.com/paoladenic/django_avila/assets/126211693/2b16f7ca-23cc-4f76-9189-3be022a79564)



