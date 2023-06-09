# README

## Titre

Quiz en ligne automatisé avec réponse aléatoire

## Description

Ce script Python utilise Selenium pour automatiser la connexion et la navigation sur un site de quiz en ligne. Il répond de manière aléatoire aux questions du quiz, puis passe à la question suivante jusqu'à ce que le processus soit interrompu manuellement. Il est spécifiquement conçu pour le site Global Exam.

## Dépendances

- Python 3
- Selenium
- ChromeDriver (assurez-vous que ChromeDriver est compatible avec votre version de Chrome)

## Installation

1. Installez Python 3 depuis https://www.python.org/downloads/
2. Installez Selenium en exécutant `pip install selenium` dans votre terminal ou invite de commande.
3. Téléchargez ChromeDriver depuis https://sites.google.com/a/chromium.org/chromedriver/downloads et placez-le dans un répertoire accessible dans votre variable d'environnement `PATH`.

## Configuration

Remplacez les variables `USERNAME` et `PASSWORD` par votre nom d'utilisateur et mot de passe pour le site de quiz en ligne.

```python
USERNAME = ''
PASSWORD = ''
```

## Utilisation

1. Ouvrez votre terminal ou invite de commande.
2. Accédez au répertoire où se trouve le script.
3. Exécutez `python script.py` pour lancer le script.
4. Le script se connectera automatiquement à votre compte et répondra de manière aléatoire aux questions du quiz.
5. Pour arrêter le script, appuyez sur `CTRL+C` dans le terminal ou fermez la fenêtre du navigateur.

## Remarque

Ce script est destiné à des fins éducatives uniquement. L'utilisation de ce script pour tricher sur un site de quiz en ligne peut être contraire aux conditions d'utilisation du site et peut entraîner des conséquences indésirables. Utilisez ce script à vos propres risques.

