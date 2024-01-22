
# Instalación Gauss

Notas para la instalación de Gauss en local.

## 1 Instalación de la aplicación 

Utilizamos *pyenv*, gestor de versiones y entornos virtuales de Python.

``pyenv install 3.7.17``  > instalo la versions de Python

``pyenv virtualenv 3.7.17 gaussApp`` > Creo un entorno virtual sobre la version
``pyenv versions`` > Veo todo, versiones y entornos virtuales. No es como *rvm* que tengo gemsets por separado.

``git clone https://github.com/jjmartinr01/gauss3.git gauss3``

``cd gauss``

``pyenv local gaussApp`` > Aplicamos el entorno virtual al directorio. Activa la versión y crea *.python-version*.

**Copiamos el arhivo requirements.txt en la raiz del proyecto**

``pip install -r requirements.txt`` > Instalamos dependencias necesarias

**Celery** es una herramienta que permite a la aplicación Gauss ejecutar procesos en background. Para su instalación añadimos  lo siguiente en el *requirements.txt* 

``importlib-metadata==4.13.0``

y volvemos a ejecutar:

``pip install -r requirements.txt``

**Para célery añadir**


``pipenv --venv`` > Puedo ver dónde **pyenv** guarda el entorno virtual. Si detecta que el entorno ha sido creado con **pyenv** lo respetará.

**Error paho-mqtt:**

``` 
Nota: Da problemas **paho-mqtt**
instalo: ``pip install --upgrade setuptools``
Me deja con un warning. Gracias al setuptools, lo solventa aunque haya errores
```

## 2 Settings

Toda aplicación Django tiene un archivo **settings.py** de configuración. Te lo paso por email y hay que colocarlo en la carpeta: **gauss**.

**El settings que te he enviado por correo tiene extensión *txt*, cámbiala a *py*. Si no, no se podía enviar por email.**

He realizado alguna modificación para adaptarlo a mi entorno en local. Te paso dos, el *settings.py* original que me pasó Juango y el *settings-david.py* que es el que he utilizado yo para mi máquina en local. 

## 3 Instalación de Postgresql

Gauss tira de de Postgresql como base de datos.
Info: https://www.postgresql.org/

## 4 Formación

He realizado algún curso en *Udemy*:
Por ejemplo: https://www.udemy.com/course/python-django-the-practical-guide/

Este curso tiene una lección resumen que puede servir como punto de partida para empezar: *Optional: Django Summary & Quick Introduction* 


