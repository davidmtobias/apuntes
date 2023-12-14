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

Nota: Abro terminal
``python3 --version`` > Python 3.11.4 (la global del sistema)

``python --version`` > error

Voy a carpeta Gauss con *.python-version* 3.7.2

``python3 --version`` > Python 3.7.2 
``python --version`` > Python 3.7.2 

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
