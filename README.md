# TP Virus  - Ynov Python B1

:see_no_evil: _**Il s'agit d'un travail autonomne.**_ :speak_no_evil:

:sparkles: Une fois le TP et le rendu terminé commitez et pushez le dans le repo. :sparkles:
  
### Tips   

:raising_hand: Si vous avez des soucis n'hésitez pas à m'appeler. 
 
 ## Exercice 1: Python Virus
 
L'objectif de cet exercice est de créer un virus qui va se répliquer automatiquement sur un système infecté. 

Un virus, pour rappel, est un programme qui embarque un code malveillant (payload) qui va infecter un systeme d'information et se multiplier sur cet OS. Il ne détruit pas le système d'exploitation mais va agir en background pour rester le plus longtemps indetecté. 


  
Votre programme devra lorsqu'il est executé : 
-  Lister les fichiers python présent dans le dossier (Nous travaillons uniquement dans un dossier pour éviter de contaminer toute la machine)

Pour chaque fichier Python il faudra : 

- Lire le fichier python 
- Insérer au début du fichier le payload (Morceau de script malveillant)

Le payload et la partie infection sera donc présent sur le nouveau fichier. Et lorsque celui-ci est executé il devra faire la même chose à son tour : 

- Scanner le dossier
- Vérifier si le fichier n'est pas déjà infecté
- Si il ne l'est pas il faudra l'infecté

