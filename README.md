# Symphony
Symphony est un langage compilé de création de musique et de sons MIDI.<br>
L'utilisateur pourra employer des fonctions du langage pour générer des notes d’instruments différents sur multiples pistes pour créer un fichier final contenant son œuvre.<br>
Le travail effectué est :<br>
- Création d'un analyseur lexical
- Création d'un analyseur syntaxique
- Création d'un compilateur qui va transformer notre langage en python pour ensuite générer du son
- Gestion des erreurs

## Conditions
Pour que le langage Symphony fonctionne, il faut installer quelques packages importants pour python.<br>
- pydot --> Installation : pip install pydot
- ply --> Installation : pip install ply
- os --> Installation : déjà installé de base
- operator --> Installation : déjà installé de base (pip install pyoperators sinon)
- re --> Installation : déjà installé de base (pip install regex sinon)
- midiutil --> Installation : pip install MIDIUtil & Utilisation : from midiutil import MIDIFile
- graphviz --> Installation : pip install graphviz (Si pas installé sous forme d'exe)

## Installation
Pour installer symphony, il faut récupérer les différents fichiers correspondants au langage.<br>
- AST.py
- symphony_ley.py
- symphony_parser.py
- symphony_compiler.py

Pour faire fonctionner le langage, il suffit donc de générer un fichier du langage Symphony (Sous forme .txt ou autre) et de le faire passer au compilateur.<br>
Lorsque l'on lance le compilateur, un fichier .midi sera généré et pourra être écouté via n'importe quel lecteur.<br>

### VLC
Pour vlc, il faut installer un plugin permettant de lire le format midi.<br>
https://ourcodeworld.com/articles/read/1170/how-to-play-midi-files-on-the-vlc-media-player-3-0-8<br>
https://wiki.videolan.org/Midi/<br>

## Membres
Bruno Costa<br>
Diogo Lopes Da Silva