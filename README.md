# Msc_Experiment

![image](https://user-images.githubusercontent.com/118670170/226708152-f8de9ff4-5cde-4f77-be29-4ca2ae39302b.png)

## 1. Qu'est-ce que c'est ?

Dans le cadre d'un mémoire de Master de Sciences Cognitives de l'Université Lyon-2, la réalisation d'une expérience sur la mémoire transactive a été réalisée.  
Cette expérience a nécessité la création de 2 expériences :

- la réplication de l'expérience 4 de Sparrow et al.
- une nouvelle expérience spécialement conçue pour répondre à une nouvelle problématique. Vous pourrez retrouver ce mémoire dans un futur proche sur ce repo.

Ces deux expériences ont été codées avec le logiciel Psychopy et faites pour être réalisées hors-ligne pour répondre aux problématiques matérielles de passation à l'Université de Bron.

## 2. Mode d'emploi via l'application PsychoPy

Pour lancer ces 2 expérimentations, il vous faudra installer le logiciel libre PsychoPy v2022.2.5  

(DL link: https://www.psychopy.org/download.html)  

Les expériences nécessitent un PC avec un clavier et une souris.  

### Expérimentation 1 : Réplication expérience 4 de Sparrow et al.

- Télécharger le repo "Msc_Experiment" au format zip ou cloner le sur votre ordinateur (git).

![image](https://user-images.githubusercontent.com/118670170/226709057-abf8b98e-0a62-4693-90ef-ab9afac0b713.png)


- Ouvrez le fichier "Expérimentation_Sparrow_Solo" > Ce dossier possède 4 fichiers :

  - "Expérimentation_SOLO_train.psyexp" > Expérimentation d'entrainement à la tâche.
  - "Expérimentation_SOLO_task.psyexp" > Expérimentation complète (Tâche).
  - "EXPE_TRAIN.xlsx" > Fichier excel contenant les anecdotes d'entrainement.  
  - "EXPE_STIM.xlsx" > Fichier excel contenant les anecdotes remaniées de l'expérience de Sparrow et al pour la tâche principale.
  - "DOSSIER" > Un dossier accessible aux participants durant la phase d'entrainement.

![image](https://user-images.githubusercontent.com/118670170/226707318-9e833392-4a2c-4c85-a094-8a1456a7de49.png)


- Ouvrez les deux fichiers .psyexp > La console PsychoPy est censé s'ouvrir avec le déroulé de l'expérience en bas de la console (Flow)

![image](https://user-images.githubusercontent.com/118670170/226710963-38dd87fd-0f7f-4ecd-b534-906a5c656a68.png)


- Cliquez sur les boucles présentent dans le Flow (représentées par des carrés gris) > une console s'ouvre > Sur la ligne "Conditions", cliquez sur l'icone dossier est insérez le fichier excel correspondant à l'expérimentation en cours (train ou tâche) et appuyez sur "Ok".

![image](https://user-images.githubusercontent.com/118670170/226710702-86be274a-6f32-43cf-b66c-705021087da1.png)

- Envoyez le train et la tâche dans le runner PsychoPy puis lancez.

![image](https://user-images.githubusercontent.com/118670170/226714453-9e6818eb-8806-42bd-9964-c9f27f95deb7.png)

- L'expérience se lance > Les consignes sont indiquées dans l'expérimentation.


### Expérimentation 2 : Tâche de groupe

- Télécharger le repo "Msc_Experiment" au format zip ou cloner le sur votre ordinateur (git).

![image](https://user-images.githubusercontent.com/118670170/226709057-abf8b98e-0a62-4693-90ef-ab9afac0b713.png)


- Ouvrez le fichier "Expérimentation_Groupe" > Ce dossier possède 7 dossiers et 2 fichiers :

  - Les dossiers des personnages (Amazon / DeepBlue / E.T / Pikachu / R2D2 / Sam) contenant un fichier train_nom.psyexp et un fichier exp_nom_double.psyexp
  - Un dossier "DOSSIER" accessible aux participants durant la phase d'entrainement.
  - 2 fichiers excel correspondant aux anecdotes et fichiers d'entrainement de de la tâche principale.

![image](https://user-images.githubusercontent.com/118670170/226718388-7089c8b6-d864-4cbb-a38a-799b79f511a3.png)

- L'expérience étant hors-ligne, il va falloir réaliser la manipulation ci-dessous sur 6 PCs différents.

- Ouvrez les deux fichiers .psyexp > La console PsychoPy est censé s'ouvrir avec le déroulé de l'expérience en bas de la console (Flow)

![image](https://user-images.githubusercontent.com/118670170/226710963-38dd87fd-0f7f-4ecd-b534-906a5c656a68.png)

- Cliquez sur la boucle présente dans le Flow pour le train et la task (représentée par un carré gris) > une console s'ouvre > Sur la ligne "Conditions", cliquez sur l'icone dossier est insérez le fichier excel correspondant à l'expérimentation en cours (train ou tâche) et appuyez sur "Ok".

![image](https://user-images.githubusercontent.com/118670170/226710702-86be274a-6f32-43cf-b66c-705021087da1.png)

- Envoyez le train et la tâche dans le runner PsychoPy puis lancez.

![image](https://user-images.githubusercontent.com/118670170/226714453-9e6818eb-8806-42bd-9964-c9f27f95deb7.png)

- L'expérience se lance > Les consignes sont indiquées dans l'expérimentation.

IMPORTANT > L'expérience étant hors-ligne, l'usage de timer a été utilisé. Pour que l'expérience semble le plus fluide possible pour les participants, à la fin de la consigne de base, il est demandé aux participants de vous appeler. Pour lancer l'expérience, il est conseillé de faire un décompte à la fin duquel les participants devront cliquer sur la touche'i'. (ex : "Après un décompte de 3 secondes, veuillez appuyer sur la touche 'i' de votre clavier. 1...2...3 ! Click!")


## 3. Déroulé des expériences

![image](https://user-images.githubusercontent.com/118670170/226736540-9a162fa9-78b6-43c8-9837-4e27b9e54c98.png)


### Expérience 1 :

L'expérience 1 est divisée en 4 phases :

  - Une phase de training : Une version miniature et réduite de la tâche principale pour s'assurer que le participant a bien compris les consignes de l'expérience. Les participants peuvent avoir accès au "DOSSIER" durant la phase de reconnaissance de cet entrainement. Cette phase d'entrainement ne comprend que 2 des 3 blocs de la tâche principale.
 
  - Une phase "Tâche" : Le participant réalise une tâche consistant à lire puis réécrire les anecdotes qui s'affichent sur l'écran. Un message indique dans quel dossier l'anecdote a été sauvegardée après validation de l'anecdote par le participant.

  - Une phase "Rappel" : Seulement présente dans la tâche principale. Le participant doit rappeler le plus d'anecdotes possibles sur une feuille dans un intervalle de 10minutes. (Bien lui préciser de rappeler tous ce dont il se souvient que ce soit des mots, des thématiques ou des parties des anecdotes)
  
  - Une phase de reconnaissance : Le participant doit rappeler le fichier dans lequel l'anecdote a été sauvegardée durant la phase "Tâche".

### Expérience 2 :

Même déroulé que l'expérience 1 : 

Quelques changements :

- Les noms des personnages doivent être affichés au dessus des PCs.
- Une phase de discussion pré-tâche doit être effectuée pour que les participants s'habituent au nom qui leur a été donné.
- Le message de validation comprends maintenant le nom d'un fichier + le nom d'un personnage.
- Les participants écrivent à tour de rôle (scripté).
- La tâched erappel reste individuelle.
- Pour la tâche de reconnaissance, les participants doivent rappeler soit le nom du personnage ayant sauvegardé l'anecdote, soit le nom du fichier où celle-ci est sauvegardée.

Informations supplémentaires :

- Les données des expériences sont sauvegardées automatiquement dans un fichier "data" au format csv.
- Le notebook d'analyse exploratoire est disponible dans le dossier "Analyse"
- Les analyses statistiques sont également disponibles dans le dossier "Analyse"

Sources : 

- Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory: cognitive consequences of having information at our fingertips. Science (New York, N.Y.), 333(6043), 776–778. https://doi.org/10.1126/science.1207745
