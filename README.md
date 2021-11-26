# CRM project

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://img.shields.io)


Projet 12 de la formation DA Python de OpenClassrooms qui consiste à créer une API RESTFul en utilisant le framework Django Rest Framework et Django ORM avec une base de données PostgreSQL, permettant de créer le suivi de client au sein de l'entrepise. 
La documentation de l'api est disponible [ici](https://documenter.getpostman.com/view/17717922/UVJbHHPv)

## Pour commencer

- Télecharger le projet
- Aller dans le dossier du projet
- Créer un environnement virtuel : ``python3 -m venv env``
- Activer l'environnement virtuel : ``source env/bin/activate``
- Installer les packages : ``pip install -r requirements.txt``
- Générer une secret_key : [Djecrety](https://djecrety.ir/)
- Créer un fichier .env à la racine du projet et y mettre la clé généré dans une variable SECRET_KEY
- Créer une base de données PostgreSQL
- Dans le .env créer des variables NAME, USER, HOST, PORT et y mettre les informations relatives a la base de données créé précédemment
- Appliquer la fixture à la base de données : ``python manage.py loaddata data.json.gz``

## Démarrage

- Lancer le serveur : ``python manage.py runserver``
- Suivre la documentation de l'api pour connaître des diffèrentes requêtes possibles : [Documentation CRM project](https://documenter.getpostman.com/view/17717922/UVJbHHPv)

## Comptes utilisateurs test 

* Accès Admin :  
    - email : admin@admin.fr  
    - password : azerty

* Comptes utilisateurs Sales Team :  
    - username : moi@sales.fr
    - password : azerty

    - username : autre@sales.fr
    - password : azerty

* Comptes utilisateurs Support Team :  
    - username : me@support.fr
    - password : azerty

    - username : pasmoi@support.fr
    - password : azerty

* Compte utilisateur Management Team :  
    - username : ma@manage.fr
    - password : azerty

## Fabriqué avec

* [Python 3](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django rest framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
