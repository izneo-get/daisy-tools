# Daisy-tools

Outils qui permettent de simlpifier des actions sur les livres audios au format "Daisy 2".

## Daisy-renamer
Permet de renommer automatiquement les fichiers d'un livre audio au format "Daisy 2". 
Il faut avoir un répertoire qui contient : 
- Un fichier `master.smil`.
- Les fichiers `*.smil` de chaque chapitre. 
- Les fichiers `*.mp3` de chaque chapitre. 


### Utilisation
```
python -m daisy_renamer
```
ou 
```
python daisy_renamer.py
```
Le programme demande le répertoire qui contient les fichiers `master.smil`, `*.smil` et `*.mp3`. 
On lui copie / colle le chemin du répertoire et on valide avec la touche `Entrée`. 
Les fichiers audio seront **copiés** dans le sous-répertoire `OUTPUT` du dossier que vous avez indiqué. 


### Installation
Python : version 3.10 (non testé avec les versions antérieures). 

```
git clone https://github.com/izneo-get/daisy-tools.git
cd daisy-tools
```

#### Avec Poetry
```
poetry shell
poetry install 
```

### Avec Pip
```
python -m venv .venv
.venv\Scripts\activate.bat
pip install -U pip
pip install -r requirements.txt
```
