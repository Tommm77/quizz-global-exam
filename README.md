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
