from selenium.webdriver.common.by import By


class Sbis:
    contacts = By.XPATH, "//div[text()='Контакты']"
    offices = By.XPATH, "//span[text() = 'Еще 19 офисов в регионе']"
    banner_tenzor = By.XPATH, "//a[@href='https://tensor.ru/']"
    region = By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text') and contains(text(), 'Свердловская обл.')]"
    list = By.CLASS_NAME, "sbisru-Contacts-List__name"
    region_41 = By.XPATH, "//span[contains(text(), 'Камчатский край')]"
    region_Kamchatka = By.XPATH, "//span[text()='Камчатский край']"
    list_41 = By.XPATH, '//div[text()="Saby - Камчатка"]'

