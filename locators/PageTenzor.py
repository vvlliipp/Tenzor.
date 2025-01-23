from selenium.webdriver.common.by import By


class Tenzor:
    power_is_in_people = By.XPATH, "//p[contains(@class, 'tensor_ru-Index__card-title') and text()='Сила в людях']"
    detailed = By.XPATH, "//a[text() = 'Подробнее']"
    working_section = By.XPATH, "//h2[text() = 'Работаем']"
    images_in_chronology = By.XPATH, "//img[contains(@class, 'tensor_ru-About__block3-image')]"
