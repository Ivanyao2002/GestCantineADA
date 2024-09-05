# Gestion Cantine ADA

Projet pour une cantine, permettant d'enregistrer, voir, éditer et supprimer le menu et les plats.

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : git clone https://github.com/Ivanyao2002/GestCantineADA.git
- Créer un environnement virtuel dans le repertoire ( python ou python3 pour Unix -m venv nom_de_lenvironnement de prefence venv ou env)
- Naviguer vers le fichier activate.bat soit dans scripts ou bin, puis activer l'environnement (source activate ou activate pour windows)
- Revener au repertoire de votre projet puis installer les dépendances de l'application à partir du fichier requirements.txt (pip ou pip3 install -r requirements.txt)
- Installez et configurez une base de données MySQL nommée 'cantine_db'
- Naviguez vers le repertoire source (src) puis créer et appliquer les migrations : python manage.py makemigrations ensuite python manage.py migrate
  
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server : python manage.py runserver, vous pouvez preciser le port python manage.py runserver numeros_port ( exple : python manage.py runserver 8888)
  
## Description des fonctionnalités principales de l'application :
- Liste des menus
- Liste des plats
- Création d'un menu
- Création d'un plat
- Modification d'un menu
- Modification d'un plat
- Supression d'un menu
- Supression d'un plat
- Possibilité de faire des recherches en fonction du nom d'un plat



