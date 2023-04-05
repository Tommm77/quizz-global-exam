import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Remplacez par l'URL du quiz en ligne
LOGIN_URL = 'https://auth.global-exam.com/login'

# Remplacez par votre nom d'utilisateur et mot de passe
USERNAME = ''
PASSWORD = ''


def login(driver):
    # Trouver les champs de saisie pour le nom d'utilisateur et le mot de passe
    username_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')

    # Saisir le nom d'utilisateur et le mot de passe
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    # Cliquer sur le bouton de connexion
    password_input.send_keys(Keys.ENTER)


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)


def atteindre_le_questionnaire(driver):
    # Attendre que le lien soit visible et cliquer dessus
    bouton_start_quiz = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(@class, 'ch-bold') and contains(text(), 'Parcours')]"))
    )
    bouton_start_quiz.click()


def prochain_module(driver):
    bouton_prochain_module = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'text-default-90') and contains(text(), 'Prochain module')]"))
    )
    if not bouton_prochain_module.is_displayed():
        scroll_to_element(driver, bouton_prochain_module)

    bouton_prochain_module.click()


def repondre_aleatoirement(driver):
    # Trouver l'élément "Suivant", "Continuer", "Terminer", "Commencer" ou "Quitter"
    try:
        bouton_suivant = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'button-solid-primary-large') and (contains(text(), 'Suivant') or contains(text(), 'Terminer') or contains(text(), 'Commencer'))] | //a[contains(@class, 'button-outline-primary-large') and contains(text(), 'Quitter')]"))
        )
    except TimeoutException:
        bouton_suivant = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'button-solid-primary-medium') and (contains(text(), 'Suivant') or contains(text(), 'Continuer') or contains(text(), 'Commencer'))] | //a[contains(@class, 'button-outline-primary-large') and contains(text(), 'Quitter')]"))
        )

    # Faire défiler la page jusqu'à ce que le bouton soit visible
    if not bouton_suivant.is_displayed():
        scroll_to_element(driver, bouton_suivant)

    # Vérifier si le bouton trouvé est "Quitter"
    if bouton_suivant.text == 'Quitter':
        # Cliquer sur le bouton "Quitter"
        bouton_suivant.click()
        time.sleep(10)

        # Revenir au questionnaire
        atteindre_le_questionnaire(driver)
        prochain_module(driver)
    else:
        # Cliquer sur le bouton "Suivant", "Continuer", "Terminer" ou "Commencer"
        bouton_suivant.click()
        time.sleep(10)

def main():
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)
    print("Page de connexion ouverte")

    # Se connecter avec le nom d'utilisateur et le mot de passe
    login(driver)
    print("Connexion réussie")

    # Attendre que le bouton "Continuer" soit visible et cliquer dessus
    atteindre_le_questionnaire(driver)
    print("Questionnaire atteint 1")

    prochain_module(driver)
    print("Prochain module atteint")

    # Répondre aux questions aléatoirement à l'infini puis appuyer sur le bouton "Suivant"
    for i in range(99999999999):
        repondre_aleatoirement(driver)
        print("Réponses aléatoires sélectionnées pour la question", i+1)

    # Fermer le navigateur après un certain temps (par exemple, 10 secondes)
    driver.implicitly_wait(10)
    driver.quit()


if __name__ == '__main__':
    main()
