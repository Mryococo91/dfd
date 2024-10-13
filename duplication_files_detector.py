import os
import logging
from collections import defaultdict

def setup_logger(log_file):
    # Configurer le logger pour écrire dans un fichier et dans la console
    logger = logging.getLogger("DuplicateFileLogger")
    logger.setLevel(logging.INFO)

    # Créer un gestionnaire pour écrire dans un fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Créer un gestionnaire pour afficher dans la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format des messages de log
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Ajouter les gestionnaires au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def find_duplicate_files_in_main_directory(main_directory, logger):
    # Dictionnaire pour stocker les fichiers avec le même nom
    files_dict = defaultdict(list)

    # Parcourir le dossier principal et ses sous-dossiers
    for root, _, files in os.walk(main_directory):
        for file in files:
            # Ajouter le fichier à la liste des fichiers ayant le même nom
            files_dict[file].append(os.path.join(root, file))

    # Rechercher les doublons (fichiers qui apparaissent plus d'une fois)
    duplicates = {file: paths for file, paths in files_dict.items() if len(paths) > 1}
    
    if duplicates:
        logger.info("Fichiers en doublon trouvés :")
        for file, paths in duplicates.items():
            logger.info(f"\nFichier : {file}")
            for path in paths:
                logger.info(f" - {path}")
    else:
        logger.info("Aucun fichier en doublon trouvé.")

if __name__ == "__main__":
    # Spécifie le dossier principal à parcourir
    main_directory = "C:/your/folder/path"  # Remplace ce chemin

    # Spécifie le fichier de log
    log_file = "duplicate_files_log.txt"

    # Configurer le logger
    logger = setup_logger(log_file)

    # Lancer la recherche des fichiers doublons
    find_duplicate_files_in_main_directory(main_directory, logger)
