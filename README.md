# Duplicate File Finder

Ce projet Python permet de détecter et de lister les fichiers en doublon présents dans un répertoire principal et ses sous-dossiers. Il offre une solution simple pour analyser un répertoire, identifier les fichiers ayant le même nom, et afficher leurs emplacements.

## Fonctionnalités

- **Recherche de doublons**: Le script parcourt un répertoire principal et tous ses sous-dossiers pour identifier les fichiers ayant le même nom.
- **Journalisation**: Les résultats sont sauvegardés dans un fichier de log, tout en étant affichés dans la console.
- **Rapidité**: Utilise une méthode efficace pour parcourir les répertoires et enregistrer les chemins des fichiers.

---

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- **Python**: Version 3.7 ou plus récente.

---

## Installation

1. **Clonez ou téléchargez le projet** :
   ```bash
   git clone https://github.com/votre-utilisateur/duplicate-file-finder.git
   cd duplicate-file-finder
2. Vérifiez que Python est installé :
   ```bash
   python --version
3. Aucune dépendance externe n'est requise pour ce projet.

Utilisez le script `duplicate-file-finder.py` pour lancer l'application.

---

## Utilisation

1. Modifiez le chemin du répertoire à analyser : Dans le script, remplacez main_directory par le chemin de votre répertoire principal, par exemple :
   ```python
   main_directory = "C:/mon/dossier/principal"
2. Exécutez le script : Lancez le script Python dans votre terminal ou IDE :
   ```bash
   python duplicate-file-finder.py
3. Consultez les résultats :
   - Les fichiers en doublon seront affichés dans la console.
   Un fichier de log nommé `duplicate_files_log.txt` est généré dans le répertoire courant contenant les détails des fichiers en doublon.

---

## Exemple de sortie
- Console:
    ```bash
    2024-12-07 12:00:00 - Fichiers en doublon trouvés :
    2024-12-07 12:00:01 - 
    Fichier : exemple.txt
    - C:/mon/dossier/principal/sous-dossier1/exemple.txt
    - C:/mon/dossier/principal/sous-dossier2/exemple.txt

- Fichier de log: (`duplicate_files_log.txt`)
    ```bash
    2024-12-07 12:00:00 - Fichiers en doublon trouvés :
    2024-12-07 12:00:01 - 
    Fichier : exemple.txt
    - C:/mon/dossier/principal/sous-dossier1/exemple.txt
    - C:/mon/dossier/principal/sous-dossier2/exemple.txt

---

## Limitations
- **Basé sur les noms de fichiers**: Le script détecte les doublons en se basant uniquement sur le nom des fichiers, sans vérifier leur contenu.
- **Non compatible avec les noms identiques dans des systèmes sensibles à la casse**: Par exemple, les fichiers `exemple.txt` et `Exemple.txt` sont considérés comme différents sous Windows.

---

## Personnalisation
- **Chemin du répertoire principal**: Changez la variable `main_directory` dans le script pour analyser un autre dossier.
- **Fichier de log**: Modifiez la variable `log_file` pour personnaliser le nom ou l'emplacement du fichier de log.

---

## Contribuer

Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Clonez le projet :
   ```bash
   git clone https://github.com/votre-utilisateur/duplicate-file-finder.git
   ```
2. Créez une branche pour votre travail :
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Faites vos modifications et testez-les :
   ```bash
   git add .
   git commit -m "Your commit message"
   ```
4. Pushez vos modifications vers votre branche :
   ```bash
   git push origin feature/your-feature-name
   ```
5. Créez une pull request pour fusionner votre branche avec la branche principale.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 