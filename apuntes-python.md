# Instalación de paquetes

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



## Entornos virtuales

Son empaquetdos de librerías

En la carpeta que elija como base de mi proyecto, escribo esta sentencia y crea toda una estructura del intérprete de python con sus librerías. Crea un subcarpeta llamada **env**, donde estará el entorno virtual.

``python3 -m venv env`` 

Para **activar** el entorno virtual tengo que ejectuar, desde la carpeta base de mi proyecto:

``source env/bin/activate``

Nota: Ahora en mi entorno puedo instalar y desintalar con pip3.

Para **desactivar** ambiente virtual

``deactivate``



#######################
# pipenv (venv + pip3)
#######################
pip3 install pipenv # Puede que en ubuntu 23: sudo apt-get install python3-pipenv

# una vez instalado pipenv
pipenv install requests # para instalar el paquete
# EN la carpeta del proyecto creará dos archivos pipfile y pipfile.lock
pipenv uninstall requests # Desinstala y actualiza pipefile


# ¿Dónde esta la carpeta env de antes?
pipenv --venv
# /home/david/.local/share/virtualenvs/package-LTdZVCTL
# Se hace así de manera práctica para liberar carga en nustro proyecto
# por si lo tenemos que compartir con otros desarrolladores

# Puedo seleccionar un intérprete u otro en VSCODE refrescando abajo el desplegable
# o también puedo teclear en la carpeta del proyecto
pipenv shell # para lanzar el ambiente virtual de la carpeta donde estoy
exit # para salir del ambiente virtual

# Pipfile
# Para instalar todas las dependencias definidas en pipfile
pipenv install
# Para instalar todas las dependencias definidas en pipfile.lock (versiones exactas)
pipenv install --ignore-pipfile
# Esta orden creará el ambiente y las dependencias requeridas


#######################
# pipenv graph : gestionando dependencias
#######################
pipenv graph
pipenv uninstall requests
pipenv graph # Sisguen estando las dependencias de requests

pipenv install requests==2.10.*

pipenv update --outdated # Lista todos los paquetes que pueden ser actualizados potencialmente
pipenv update # Actualiza todos
pipenv update requests # Actualiza solo el paquete requests




#####################
## ¿Cómo administrar multiples versiones de Python

https://www.freecodecamp.org/espanol/news/administrar-multiples-versiones-de-python-y-entornos-virtuales/

Múltiples versiones de Python: Diferentes instalaciones de Python en la misma máquina, por ejemplo, 2.7 y 3.4.

Necesito la 3.7.2

Entornos virtuales: entornos independientes aislados que pueden tener tanto una versión específica de Python como de cualesquiera paquetes específicos de proyecto instalados en ellos, sin afectar a otros proyecto

3 herramientas

venv  => Solo una versión de python con diferentes entornos virtuales. (pipenv = venv + pip3)
/ pyvenv => script obsoleto para multiples versiones de python


pyenv => múltiples versiones de python en 3.3+ con o sin entornos virtuales

pyenv-virtualenv => ython 2

#venv
Desde Python 3.3+ el paquete venv está incluido. Es ideal para crear entornos virtuales ligeros.

python3 -m venv nombre-del-directorio-a-crear => crea un entorno virtual
$ source nombre-dado/bin/activate => para activarlo
$ deactivate => para desactivarlo
$ rm -r nombre-dado => Eliminar por completo después de deactivarlo

Para indicar una versión:
$ python3.6 -m venv example-three-six

Cuando el entorno está activo, cualquier paquete puede ser instalado ahí mediante pip de manera normal
Se recomienda hacer esto para actualizar pip:
pip install --upgrade pip

requirements.txt especificando sus dependencias
pip install -r requirements.txt => instala las dependencias


#pyvenv => envoltorio venv, script obsoleto en 3.8
Hasta Python 3.6 un script llamado pyvenv también se incluyó como envoltorio de  venv, pero ya es obsoleto. Se eliminará por completo en Python 3.8.

#pyenv 
Instalar: https://github.com/pyenv/pyenv-installer

pyenv versions
python3 --version
pyenv install 3.7.2

Nota: Abro terminal
python3 --version
=> Python 3.11.4 (la global del sistema)

python --version 
=> error

Voy a carpeta Gauss con .python-version 3.7.2
python3 --version
=> Python 3.7.2 
python --version
=> Python 3.7.2 



# Para instalar Gauss:
pyenv install 3.7.17  => instalo la versions de python
pyenv virtualenv 3.7.17 gaussApp => creo un entorno virtual sobre la version
pyenv versions => veo todo, no es como rvm que tengo gemsets por separado
git clone https://github.com/jjmartinr01/gauss3.git gauss3
cd gauss
pyenv local gaussApp => al ejecutar en un directorio, activa la versión y crea .python-version
pip install -r requirements.txt


# Para célery añadir 
 importlib-metadata==4.13.0


pipenv shell # para lanzar el ambiente virtual de la carpeta donde estoy
pipenv --venv
# /home/david/.local/share/virtualenvs/package-LTdZVCTL



pip install -r requirements.txt => instala las dependencias
Me da problemas paho-mqtt
 > instalo: pip install --upgrade setuptools
y parece que me deja con un warning.Warning
Luego se isntalan más cosas, pero gracias al setuptools, lo solventa aunque haya errores
