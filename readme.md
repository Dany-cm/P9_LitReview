# Lit Review

L’application permet de demander des critiques de livres ou d’articles, en créant un ticket publier des critiques de
livres ou d’articles

<p align="center">
  <img width="460" height="300" src="https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png">
</p>

## Installation

Python est nécessaire pour faire fonctionner l'application, télécharger le ici :

[Windows](https://www.python.org/downloads/windows/)

[Linux](https://www.python.org/downloads/source/)

[MacOS](https://www.python.org/downloads/macos/)

```python
Installer pipenv 
pip install pipenv
```

## Utilisation

Télécharger le site [ici](https://github.com/Danycm1/P9_LitReview/archive/refs/heads/master.zip) ensuite extraire le
dossier ou vous le souhaitez.

```txt
Acceder au dossier extrait avec la commande cd :
cd P9_LitReview\mysite

Installer les dépendances du projet:
pipenv install -r requirements.txt

Accéder à l'environnement virtuel avec :
pipenv shell

Lancer le serveur :
python manage.py runserver
```

Accéder au site :

http://127.0.0.1:8000

Accéder à l'interface d'administration :

http://127.0.0.1:8000/admin

Compte administrateur par défaut :

Utilisateur : admin

Mot de passe : f5ChX8ATJAiyhDw

## Fonctionnalités

- Se connecter et s’inscrire
- Consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre
  chronologique, les plus récents en premier
- Voir vos propres posts
- Créer de nouveaux tickets pour demander une critique sur un livre/article
- Créer des critiques en réponse à des tickets
- Créer des critiques qui ne sont pas en réponse à un ticket
- Voir, modifier et supprimer ses propres tickets et commentaires
- Suivre les autres utilisateurs en entrant leur nom d'utilisateur
- Voir qui il suit et suivre qui il veut
- Cesser de suivre un utilisateur.

## License

[Danycm1](https://github.com/Danycm1)