# Projet d'Indexation Web

Ce projet d'indexation web comprend des scripts Python pour effectuer diverses tâches liées à l'exploration et à l'indexation de pages web. Le projet est organisé comme suit:

## Contenu du Répertoire

- `example.db`: Base de données d'exemple utilisée dans le projet.
- `README.md`: Le fichier que vous lisez actuellement, contenant la documentation du projet.
- `requirements.txt`: Fichier spécifiant les dépendances du projet.

## Diagramme de Classes

![Diagramme de Classes](TP1/doc/diagramme_de_classes.drawio.svg)
### Dossiers et Fichiers Importants

- `TP1`: Dossier principal du TP1.


  - `doc`: Dossier contenant la documentation du TP1.
    - `diagramme_de_classes.drawio.svg`: Diagramme de classes du TP1.
  - `main.py`: Script principal du TP1.
  - `src`: Dossier contenant les scripts sources du TP1.
    - `classes`: Dossier contenant la définition de la base de données
    - `compter_pages_d_un_domaine.py`: Script pour compter les pages d'un domaine.
    - `create_session.py`: Script pour créer une session en base de données.
    - `fetch_url.py`: Script pour récupérer une URL.
    - `is_allowed_by_robots.py`: Script pour vérifier si le site autorise les robots
    - `get_age.py`: retourne la date de dernière modification d'une url
    - `get_hrefs_from_url.py`: retourne les liens contenus dans le html d'une page url

- `TP1.pdf`: Document PDF associé au TP1.

## Instructions d'Exécution

Pour exécuter le TP1, suivez les étapes suivantes:

1. Installez les dépendances en utilisant `pip install -r requirements.txt`.
2. Exécutez le script principal `main.py` du TP1.

## Remarques Importantes

- Les fichiers et dossiers sont organisés de manière à simplifier la navigation et l'exécution du projet.
- Certains fichiers ont été exclus de la documentation pour des raisons de clarté.

N'hésitez pas à explorer le contenu de chaque dossier et fichier pour plus de détails sur la mise en œuvre du projet.
