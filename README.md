# Rimbaud  
Cette application Web crée un site de blog très basique en utilisant Django.  
Le site permet à un écrivain de créer des articles en texte uniquement à l'aide du site d'administration.  

## Quick Start  
Pour lancer ce projet localement sur votre ordinateur :  
1. Configurez l'environnement de développement Python.  
2. Exécutez les commandes suivantes:  
```
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
3. Ouvrez un navigateur sur http://127.0.0.1:8000/admin/ pour ouvrir le site d'administration.  
4. Ouvrez l'onglet vers http://127.0.0.1:8000 pour voir le site principal, avec vos nouveaux articles.  

## Resultat  
Vous pouvez voir le resultat sur le lien suivant:  
[https://rimbaud-ib.azurewebsites.net](https://rimbaud-ib.azurewebsites.net/)
