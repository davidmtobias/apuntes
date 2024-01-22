# Python: Instalación de paquetes y entornos

## pip

Herramienta básica para instalar paquetes. 

``pip3 install requests`` > Instala el paquete **requets**

Nota: En Ubuntu 23 da problemas porque esta instalación se realiza con ``apt get install python3-requests``. Me recomienda crear ambientes virtuales


``pip3 list``  > Lista todos los paquetes instalados

``pip3 uninstall requests`` > Desinstala el paquete **requets**

``pip3 install requests==2.18.1`` > Instala versión específica

``pip3 install requests==2.18.*`` > Última versión compatible con la 2.18

``pip3 install requests==2.*`` > Última versión compatible con la 2

``pip3 install 'requests==2.18.1'`` > Si tengo instalado **zsh**, pongo comillas. 

``pip3 install requests~=2.18.1`` > Con tilde elige la que más se parezca a lo pedido



## Entornos virtuales. 1 versión de Python
**De momento solo tengo una versión de Python**

Son empaquetados de librerías. 


### Venv

En la carpeta que elija como base de mi proyecto, escribo esta sentencia y crea toda una estructura del intérprete de python con sus librerías. Crea un subcarpeta llamada **env**, donde estará el entorno virtual. Puedo darle otros nombre en lugar de **env**.


``python3 -m venv env`` 

Para **activar** el entorno virtual tengo que ejectuar, desde la carpeta base de mi proyecto:

``source env/bin/activate``

Nota: Ahora en mi entorno puedo instalar y desintalar con pip3.

Para **desactivar** ambiente virtual

``deactivate``

Para eliminarlo por completo:
``rm -r env``



### Pipenv (venv + pip3)

Instalación de *Pipenv*:

``pip3 install pipenv``

Nota: En ubuntu 23 ``sudo apt-get install python3-pipenv``

Una vez instalado pipenv, para instalar el paquete **requests**

``pipenv install requests`` 

Nota: En la carpeta del proyecto creará dos archivos **pipfile** y **pipfile.lock**. Estos dos archivos contendrán todas las dependencias del proyecto.

``pipenv uninstall requests`` > Desinstala y actualiza pipefile


**¿Dónde esta la carpeta 'env' de antes?**

``pipenv --venv``

*/home/david/.local/share/virtualenvs/package-LTdZVCTL*

Nota: Se hace así de manera práctica para liberar carga en nustro proyecto por si lo tenemos que compartir con otros desarrolladores. 

**¿Cómo selecciono un intérprete u otro?**

1) En VSCODE refrescando abajo el desplegable.

2)  Teclear en la carpeta del proyecto

``pipenv shell`` > Lanza el ambiente virtual de la carpeta donde estoy.

``exit`` > Salir del ambiente virtual.


``pipenv install`` > Instala todas las dependencias definidas en **pipfile**.

``pipenv install --ignore-pipfile`` > Instala todas las dependencias definidas en **pipfile.lock** (versiones exactas)

Nota: Esta orden creará el ambiente y las dependencias requeridas

### Gestión de dependencias

``pipenv graph`` > Ver dependencias
``pipenv uninstall requests``
``pipenv graph`` > Siguen estando las dependencias de **requests**

``pipenv install requests==2.10.*``

``pipenv update --outdated`` > Lista todos los paquetes que pueden ser actualizados potencialmente
``pipenv update`` > Actualiza todos
``pipenv update requests`` > Actualiza solo el paquete **requests**




## Administrar multiples versiones de Python

Fuente: https://www.freecodecamp.org/espanol/news/administrar-multiples-versiones-de-python-y-entornos-virtuales/

**Ahora doy un paso más y tengo múltiples versiones de Python**: Diferentes instalaciones de Python en la misma máquina, por ejemplo, 2.7 y 3.4. Necesito la 3.7.2

**Entornos virtuales**: entornos independientes aislados que pueden tener tanto una versión específica de Python como de cualesquiera paquetes específicos de proyecto instalados en ellos, sin afectar a otros proyecto

**3 herramientas:**

* **venv**: Solo una versión de python con diferentes entornos virtuales. **(pipenv = venv + pip3)**. *Ver apuntes arriba*. Desde Python 3.3+ el paquete venv está incluido. Es ideal para crear entornos virtuales ligeros.

* **pyvenv**: script obsoleto para multiples versiones de python. Envoltorio venv, script obsoleto en 3.8. Hasta Python 3.6 un script llamado pyvenv también se incluyó como envoltorio de  venv, pero ya es obsoleto. Se eliminará por completo en Python 3.8.

* **pyenv-virtualenv**: Para Python 2

* **pyenv (OPCIÓN ELEGIDA)**: múltiples versiones de python en 3.3+ con o sin entornos virtuales.


Para **indicar una versión** de Python con **venv**:

``python3.6 -m venv example-three-six``

Cuando el entorno está activo, cualquier paquete puede ser instalado ahí mediante pip de manera normal
Se recomienda hacer esto para actualizar pip:

``pip install --upgrade pip``

**Instalando dependencias:** con *requirements.txt* 

``pip install -r requirements.txt`` > Instala las dependencias


## Pyenv 
Instalar: https://github.com/pyenv/pyenv-installer

``pyenv versions``
``python3 --version``
``pyenv install 3.7.2``


**Creo un entorno virtual** específico:

``pyenv virtualenv 3.7.17 miEntorno`` > Creo un entorno virtual sobre la version
``pyenv versions`` > Veo todo, versiones y entornos virtuales. No es como *rvm* que tengo gemsets por separado.

**Elimino un entorno virtual**
``pyenv versions`` > listo todos y elijo el que quiero eliminar
``pyenv uninstall 3.12.0/envs/djangoCourse``

**Activo**, en el directorio del proyecto, el entorno creado:

``pyenv local gaussApp`` > Aplicamos el entorno virtual al directorio. Activa la versión y crea *.python-version*.

Para **instalar paquetes** puedo usar *pip3*:

``python -m pip install Django``



Nota: Abro terminal
``python3 --version`` > Python 3.11.4 (la global del sistema)

``python --version`` > error

Voy a carpeta Gauss con *.python-version* 3.7.2

``python3 --version`` > Python 3.7.2 
``python --version`` > Python 3.7.2 



### Prolema: '_tkinter'
Trato de instalar Python 12 con:

``pyenv install 3.12``

*Error:*
``` 
ModuleNotFoundError: No module named '_tkinter'
WARNING: The Python tkinter extension was not compiled and GUI subsystem has been detected. Missing the Tk toolkit?
Installed Python-3.12.0 to /home/david/.pyenv/versions/3.12.0 
```

*Solución*:

``sudo apt update``
``sudo apt install tk-dev``

```
Set the TCL_LIBRARY and TK_LIBRARY environment variables. You can do this in your shell configuration file (e.g., ~/.bashrc or ~/.zshrc) or set them temporarily for your session. Replace <path_to_tcl> and <path_to_tk> with the actual paths

export TCL_LIBRARY="<path_to_tcl>/lib"
export TK_LIBRARY="<path_to_tk>/lib"
```

Para ver el path de las librerías creo un archivo **path.py**

```
import tkinter
root = tkinter.Tk()
print(root.tk.exprstring('$tcl_library'))
print(root.tk.exprstring('$tk_library'))
```

*output*: ``python3 path.py``

/usr/share/tcltk/tcl8.6
/usr/share/tcltk/tk8.6

Copio este código en: *.bash_profile*, *.bash_rc*, *.profile* ty en *.zshrc*:

```
# Set the TCL_LIBRARY and TK_LIBRARY environment variables. You can do this in your shell configuration file (e.g., ~/.bashrc or ~/.zshrc) or set them temporarily for your session. Replace <path_to_tcl> and <path_to_tk> with the actual paths
#export TCL_LIBRARY="/usr/share/tcltk/tcl8.6/lib"
#export TK_LIBRARY="/usr/share/tcltk/tk8.6/lib"
```



# Instalación Gauss:

``pyenv install 3.7.17``  > instalo la versions de Python

``pyenv virtualenv 3.7.17 gaussApp`` > Creo un entorno virtual sobre la version
``pyenv versions`` > Veo todo, versiones y entornos virtuales. No es como *rvm* que tengo gemsets por separado.

``git clone https://github.com/jjmartinr01/gauss3.git gauss3``

``cd gauss``

``pyenv local gaussApp`` > Aplicamos el entorno virtual al directorio. Activa la versión y crea *.python-version*.

``pip install -r requirements.txt`` > Instalamos dependencias


**Para célery añadir**_

``importlib-metadata==4.13.0``

**Mezcla con pipenv**:

``pipenv shell`` > para lanzar el ambiente virtual de la carpeta donde estoy

``pipenv --venv`` > Puedo ver dónde **pyenv** guarda el entorno virtual. Si detecta que el entorno ha sido creado con **pyenv** lo respetará.


``pip install -r requirements.txt`` > Instala las dependencias

``` 
Nota: Da problemas **paho-mqtt**
instalo: ``pip install --upgrade setuptools``
Me deja con un warning. Gracias al setuptools, lo solventa aunque haya errores
```

# Django. Curso Udemy


## Instalación

Profesor: Maximilian Schwarzmüller

Instalación:
``python -m pip install Django``

Crear nuevo proyecto:
``django-admin startproject django_course_site``

VisualStudio code extensión:
* *Python (Microsoft)*, 
* *Pylance (Microsoft)*

En vscode aparecen líneas en amaraillo, porque no es capaz de encontrar las referencias. Le indico el intérprete que debe coger:

**shift+ctrl+p** > Python interpreter y selecciono "djangoCourse"

Files tree:
*settings.py*
*urls.py*

## Apps

Una aplicación para cada modelo aproximadamente.

Start app:
``python manage.py startapp meetups``


# Django, Vue.js, Tailwind, Axios integration

## Entorno virtual para python para Django

Creo el entorno el entorno virtual para Django
``pyenv virtualenv 3.12.0 django5vite`` > Creo un entorno virtual sobre la version
``pyenv versions`` > Veo todo, versiones y entornos virtuales. No es como *rvm* que tengo gemsets por separado.

``pyenv activate django5vite`` > Activamos el entorno virtual

Instalción de Pip-tools (pip-compile general requeriments.txt)
``pip3 install pip-tools``

Instalación Django
``python -m pip install Django``

## Creación proyecto Django

Crear nuevo proyecto:
``django-admin startproject django5vite``
``cd django5vite``
``pyenv local django5vite`` > Aplicamos el entorno virtual al directorio. Activa la versión y crea *.python-version*.

Dependecias: (aconsejable)
Creo *requirements.in*:
```
# requirements.in
Django
django-vite
python-decouple
```
``pip-compile requirements.in`` > genera el fichero *requirements.txt* con dependencias anidadas
``pip-sync`` > Instala lo que hay en *requirements.txt*

Nota: Dependencias: (avoid) Una forma de volcar las dependencias que voy instalando. Solo registra las directas
``pip freeze > requirements.txt``
``pip install -r requirements.txt``


Opcional: Instalamos Django Rest Framework
``pip install djangorestframework``
``pip install django-cors-headers``

Nota: También puedo añadir **djangorestframework** en *requirements.in* y 
``pip-compile requirements.in`` 
``pip-sync``

Configuramos Django Rest Framework:


## Instalamos Vue y Tailwindcss

Instalamos Vue y Vite (Vite va de serie). Dentro de la carpeta del proecto *djangoVueApp*. El nombre del proyecto será **frontend**.
``npm create vue@latest`` > 

Instalamos Tailwindcss y algunas cosas más (with VIte)
``npm install -D tailwindcss postcss postcss-import postcss-simple-vars autoprefixer cross-env dotenv``

Cambiamos la entrada *scripts* de *package.json*:


```
  "scripts": {
    "dev": "cross-env TAILWIND_MODE=watch vite -d",
    "build": "cross-env TAILWIND_MODE=build vite build"
  },
```

Nota: en package.json quitamos lo siguiente porque los plugins no se pueden cargar dinámicamente.

```
  "private": true,
  "type": "module",
```

``npm install axios``

Configuramos axios en main.js
```
// CSS
// vite can only build js files, So we use this imports as entrypoint for any .css files
import './assets/tailwind.css'; //Tailwind
import './assets/main.css'      //Css tradicional

// Javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8010'

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
```

Configuramos **frontend/vite.config.js**:

```
import { defineConfig, loadEnv } from 'vite';
import { resolve, join } from 'path';
import vue from '@vitejs/plugin-vue';

const postcssConfig = {
  plugins: [
    require('postcss-import')(),
    require('postcss-simple-vars')(),
    require('tailwindcss/nesting')(),
    require('tailwindcss')(),
    require('autoprefixer')(),
  ],
};

export default defineConfig((mode) => {
  const env = loadEnv(mode.mode, process.cwd(), '');

  const INPUT_DIR = './src';
  const OUTPUT_DIR = './dist/vite';

  return {
    plugins: [vue()],
    resolve: {
      alias: {
        '@': resolve(INPUT_DIR),
        'vue': 'vue/dist/vue.esm-bundler.js',
      },
    },
    root: resolve(INPUT_DIR),
    base: '/static/vite', //url para dev
    css: {
      postcss: postcssConfig,
    },
    server: {
      host: env.DJANGO_VITE_DEV_SERVER_HOST,
      port: env.DJANGO_VITE_DEV_SERVER_PORT,
    },
    build: {
      manifest: true,
      emptyOutDir: true,
      outDir: resolve(OUTPUT_DIR),
      rollupOptions: {
        input: {
          main: join(INPUT_DIR, '/src/main.js'),
        },
      },
    },
  };
});

```

Configuramos **frontend/tailwind.config.js**:

```
/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /* Process all JavaScript files in django apps. */
    '../**/*.{js,jsx,ts,tsx,vue}',
    '../**/templates/**/*.html',
    '../**/*.py',

    /* Ignore any JavaScript in node_modules folder. */
    '!**/node_modules',

    /* Process all JavaScript files in vite_app src. */
    'src/**/*.{js,jsx,ts,tsx,vue}',
  ],
};
```

Tailwind
Creamos **src/assets/tailwind.css**

```
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```
<!-- 
En **src/assets/main.css**:
En la primera línea importamos: ``@import './tailwind.css'`` -->

Creamos en la base del proyecto *.env.development*

```
# Django
PORT=8002
HOST=0.0.0.0
DEBUG=true
SECRET_KEY="change-me-8y1prljc&k=xs=xd6uxbkxgy5qp@15ua#evgotkw-7@s*iz+&i"

# Django-vite
##########################################
# Para cambiar y ver las assets compiladas, poner dev_mode a false
# Acordarse de recompilar con python3 manage.py collectstati
# dev_mode >  #True > django-vite pone localhost:5175 en las urls de las assets
DJANGO_VITE_DEV_MODE=true
###########################################

DJANGO_VITE_DEV_SERVER_PORT=5175
DJANGO_VITE_DEV_SERVER_HOST=0.0.0.0
DJANGO_VITE_STATIC_URL_PREFIX="vite"
```


Complementamos settings.py:

```
"""
Django settings for django5vite project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

#from decouple import config
from decouple import Config, RepositoryEnv
config = Config(RepositoryEnv('.env.development'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-c2%^xm-=ix6ff!w7j$t9$fh%b9*tjcc0b1q@dhzlaqlf%vw(s6'
SECRET_KEY = config("SECRET_KEY")

# No cambiar hasta pasar a producción.
# Si quiero servir assets compiladas cambiar DJANGO_VITE_DEV_MODE
DEBUG = config("DEBUG", default=True, cast=bool) 

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_vite',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django5vite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django5vite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Add the build.outDir from vite.config.js to STATICFILES_DIRS
# so that collectstatic can collect your compiled vite assets.
# Usado también por 'django.contrib.staticfiles' para la compilación al vuelo de assets no incluidas en las apps
STATICFILES_DIRS = [
    BASE_DIR / "frontend/src/dist",
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# legacy django-vite settings

DJANGO_VITE = {
    "default": {
        "dev_mode": config("DJANGO_VITE_DEV_MODE", default=False, cast=bool),
        "dev_server_port": config("DJANGO_VITE_DEV_SERVER_PORT", default="5173"),
        "manifest_path": STATIC_ROOT / config("DJANGO_VITE_STATIC_URL_PREFIX", default="vite") / "manifest.json",
        "static_url_prefix": config("DJANGO_VITE_STATIC_URL_PREFIX", default="vite"), 
    }
}

# En modo NO desarrollo (pero pruebas en local, nunca en PRODUCCIÓN)
# 1. Quito la app django.contrib.staticfiles para que las assets se recojan de STATIC_ROOT
# Nota: en urls.py añadir > + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# 2. Añado el prefijo STATIC_URL porque django.contrib.staticfiles lo añadía directamente
#
# dev_mode = true > url localhost en assets
# dev_mode = false > url static en las assets
# poniendo 'django.contrib.staticfiles' > no tira de STATIC_ROOT
# quitando 'django.contrib.staticfiles' > tira de STATIC_ROOT 

if not config("DJANGO_VITE_DEV_MODE", default=False, cast=bool):
    INSTALLED_APPS.remove('django.contrib.staticfiles')
    DJANGO_VITE["default"]["static_url_prefix"] = STATIC_URL + DJANGO_VITE["default"]["static_url_prefix"]
    
```

Configuramos ursl.py

```
"""
URL configuration for django5vite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="index",),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

En vez de crear una aplicación, jugamos con la principal por defecto
Añadimos templates/base.html
Añadimos templates/index.html
Añadimos apps.py
Añadimos la aplicación 'django5vite' en INSTALLED_APP de settings.py

## Creamos las primera aplicación

``django-admin startapp api`` > api es el nombre de la aplicación
``python3 manage.py startapp api`` > Prácticamente lo mismo que la anterior.

Añadimos la aplicación en *settings.py*:

```
INSTALLED_APPS = [
    ...
    'api.apps.ApiConfig',
    'rest_framework',
]
```

Creamos superuser:
``python3 manage.py createsuperuser``

