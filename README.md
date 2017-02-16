# Recherche d'Information Web

### Quickstart

+ Cloner le repo git
+ Si nécessaire, installer `nltk`, `matplotlib` ainsi que `regex` via la commande `pip install <module>`
+ Si nécessaire, lancer `nltk_dowload.py` et installer la collection `stopwords` via le nltk downloader
+ Lancer `main.py` dans le dossier `cacm`
+ Suivre les instructions dans la console python

### Pour utiliser le moteur de recherche "Monkgle"

+ Lancer en local `app.py` dans le dossier `FlaskApp`
+ Ouvrir un navigateur et aller sur `http://127.0.0.1:5000`
+ Utiliser le moteur de recherche

A noter qu'à chaque nouvelle recherche un fichier html sera généré. Il serait bien sûr préférable d'avoir un fonctionnement autre moins gourmand en espace mémoire. Etant donné que cela n'était pas le coeur du travail à fournir, nous avons décidé de ne pas nous attarder sur ce point.

### Organisation du code

#### Dossier 'cacm'

Les différents fichiers présents dans le dossier `cacm` reprennent les consignes du devoir dans l'ordre, à savoir :

+ Préparation des documents : `tokenization.py`
+ 2.1 Traitements linguistiques (questions 1 à 5) : `A_traitements_linguistiques.py`
+ 2.2 Indexation : `B_indexation.py`
+ 2.2.1 Modèle de recherche booléen : `C_modele_booleen.py`
+ 2.2.2 Modèle de recherche vectoriel : `D_modele_vectoriel.py`
+ 2.3 Mesure de pertinence : `E_mesure_pertinence.py`

Les mesures de performances sont quant à elles effectuées au fil des opérations et affichées dans la console.

#### Dossier 'FlaskApp'

Les différents fichiers et dossiers présents dans le dossier `FlaskApp` ont pour but de gérer tout ce qui est relatif à l'intégration de l'interface, à savoir :

+ `documents` : regroupe les json nécessaires aux recherches afin de ne pas avoir à les recalculer à chaque requête
+ `static` : regroupe les styles css nécessaires
+ `templates` : regroupe les templates html nécessaires (`index.html`, `result.html`, `monkey.html` ainsi que les résultats générés au fil des requêtes)
+ `app.py` : méthodes de l'API Flask nécessaires aux recherches
+ `jsonToHTMLBoolean.py`: crée la page html associée au résultat d'une recherche booléenne
+ `jsonToHTMLVectorial.py`: crée la page html associée au résultat d'une recherche vectorielle

#### Dossier 'cs276'

Nous avions commencé à travailler en parrallèle sur les collections `cacm` et `cs276` mais n'avons malheureusement pas eu le temps d'avoir beaucoup de résultats avec `cs276`. Ce dossier regroupe nos débuts de travaux sur cette collection.