
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

## 4 Migraciones de base de datos

Es necesario ejecutar los scripts para realizar la migración de la base de datos.
En la raíz del proyecto encontramos dos archivos *reset_migraciones.sh* y *re_migrations.sh*
Hay que cambiar las rutas para que apunten al lugar donde tienes el entorno virtual instalado.

**No recuerdo cual de los dos ejecuté**

Este es mi **reset_migraciones.sh**:

```
echo "Iniciando script"
echo "******** Borrando migraciones core Django ********"
find /home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages/django/contrib -path "*/migrations/*.py" -not -name "__init__.py" -delete
find /home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages/django/contrib -path "*/migrations/*.pyc" -delete
echo "**************************************************"
echo

echo "******** Borrando migraciones core Django: captcha ********"
find /home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages/captcha -path "*/migrations/*.py" -not -name "__init__.py" -delete
find /home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages/captcha -path "*/migrations/*.pyc" -delete
echo "**************************************************"
echo

echo "******** Borrando migraciones Gauss ********"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
echo "**************************************************"
echo

echo "******** Ejecutando: python manage.py makemigrations --empty \$app ********"
for app in 'auth' 'contenttypes' 'sessions' 'sites' 'messages' 'staticfiles' 'admin' 'bancos' 'autenticar' 'entidades' 'mensajes' 'my_templatetags' 'calendario' 'contabilidad' 'actas' 'documentos' 'lopd' 'vestuario' 'apariencia' 'compraventa' 'web' 'kronos' 'captcha' 'gauss_conf' 'formularios' 'gtelegram' 'horarios' 'cupo' 'convivencia' 'absentismo' 'registro' 'reparaciones' 'actividades' 'tutorados' 'programaciones' 'estudios' 'competencias_clave' 'vut' 'domotica' 'reuniones' 'moscosos' 'inspeccion_educativa' 'federaciones' 'faqs' 'corsheaders' 'webpage'
do
  python manage.py makemigrations --empty $app
done
echo "**************************************************"
echo

echo "******** Ejecutando: python manage.py makemigrations ********"
python manage.py makemigrations
echo "**************************************************"
echo

echo "******** Ejecutando: python manage.py makemigrations ********"
python manage.py migrate
echo "**************************************************"
echo
echo "Script finalizado"

```

Y este mi **re_migrations.sh**:

```
# Borramos las migraciones de las app del core de Django
#find ../venv/lib/python3.10/site-packages/django/contrib -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find ../venv/lib/python3.10/site-packages/django/contrib -path "*/migrations/*.pyc" -delete


find /home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages/django/contrib -path "*/migrations/*.py" -not -name "__init__.py" -delete
find /home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages/django/contrib -path "*/migrations/*.pyc" -delete

/home/david/.pyenv/versions/3.7.17/envs/gaussApp/lib/python3.7/site-packages

# Borramos las migraciones de las app de Gauss
#find ../ -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find ../ -path "*/migrations/*.pyc" -delete

for app in bancos autenticar entidades mensajes calendario contabilidad actas documentos lopd vestuario apariencia compraventa web formularios gtelegram horarios cupo convivencia absentismo registro reparaciones actividades tutorados programaciones estudios competencias_clave vut domotica reuniones webpage
do
    rm -Rf ./$app/migrations/
done

# Generamos
for app in bancos autenticar entidades mensajes calendario contabilidad actas documentos lopd vestuario apariencia compraventa web formularios gtelegram horarios cupo convivencia absentismo registro reparaciones actividades tutorados programaciones estudios competencias_clave vut domotica reuniones webpage
do
    python manage.py makemigrations $app
done

python manage.py migrate --fake-initial

```


## 5 Formación

He realizado algún curso en *Udemy*:
Por ejemplo: https://www.udemy.com/course/python-django-the-practical-guide/

Este curso tiene una lección resumen que puede servir como punto de partida para empezar: *Optional: Django Summary & Quick Introduction* 


