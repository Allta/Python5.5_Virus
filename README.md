# TP Guess The Number - Ynov Python B1

:see_no_evil: _**Il s'agit d'un travail autonomne.**_ :speak_no_evil:

:sparkles: Une fois le TP et le rendu terminé commitez et pushez le dans le repo. :sparkles:
  
### Tips   

:raising_hand: Si vous avez des soucis n'hésitez pas à m'appeler. 
 
 ## Exercice 1: TV Show Renamer
 
Dans ce projet, dans le fichier `main.py` vous devez réaliser un programme pour renommer les épisodes d'une série téléchargée depuis des sources différentes.
Dans cet exercice vous devrez utiliser les fichiers du dossier `exercice 1`


 Il faudra : 
- Detecter le numéro de l'épisode
- Renommer le fichier sans modifier l'extension en suivant le pattern suivant : 
  - **Tokyo Ghoul [SEASON_NUMBERxEPISODE_NUMBER] - EPISODE_NAME.EXTENSION** 
  - Pour cela vous devrez utiliser les fonctions de manipulation de chaîne de caractère
  - Vous allez devoir boucler sur les fichiers du dossier `exerce1` pour récupérer les noms des fichiers.
  - Pensez à trier les fichiers

  <summary>Astuce</summary>
  
  
  ```python
  import os

  for filename in os.listdir("/path/to/dir/"):
    if filename.endswith("XXX") or filename.endswith("XXX"): 
        print(os.path.join(directory, filename))

    else:
        print('not found)
        
   files =  os.listdir()

  print(files)

  Output

  ['A sample.txt', 'src.py', 'D sample.txt', 'E sample.txt', 'C sample.txt', 'B sample.txt']


  sorted_files =  sorted(files)

  print(sorted_files)
  ```


 - Vous pouvez créer une liste ou un dictionnaire (key:value) contenant les noms des épisodes. Par exemple {"1":"Tragedy","2":"Incubation"...} ou une liste : ["Tragedy", "Incubation",...,"High Spirits"]
 - Les noms des épisodes sont fournis ci-dessous.


Tokyo Ghoul [1x5] - Scars.mp4  
Tokyo Ghoul [1x9] - Birdcage.mp4  
Tokyo Ghoul [1x7] - Captivity.mp4  
Tokyo Ghoul [1x2] - Incubation.mp4  
Tokyo Ghoul [1x8] - Circular.mp4    
Tokyo Ghoul [1x11] - High Spirits.mp4  
Tokyo Ghoul [1x10] - Aogiri.mp4  
Tokyo Ghoul [1x4] - Supper.mp4  
Tokyo Ghoul [1x3] - Dove.mp4  
Tokyo Ghoul [1x6] - Cloudburst.mp4  
Tokyo Ghoul [1x1] - Tragedy.mp4  


## Exercice BONUS : 

- Ne pas utiliser la liste des épisodes ci-dessus.
- Utiliser le dossier :  `exercice_bonus`
- Le programme doit detecter le nom de la série en comptant le nombre d'occurence des mots dans les des noms de fichier présents dans le dossier (Ou une autre façons si vous préférez)
- Le programme doit detecter le numéro de la saison de l'épisode, si des saisons différentes sont dans le même dossier il faudra alors séparer les épisodes dans des dossiers différents comportant le numéro de la saison.
- A l'aide du site : https://thetvdb.com/series/the-big-bang-theory/seasons/official/6 et de la librairie `request` (ou de la librairie `tvdb-api`) récupérer les noms des épisodes et renommer en concordance.
- Le programme peut fonctionner uniquement pour les 2 séries présentes. Vous pouvez si vous le souhaitez déterminer les séries présentes dynamiquement. 




