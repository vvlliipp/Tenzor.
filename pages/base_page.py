import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
import time


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Видимость элемента")
    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception:
            return False

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator, max_retries=3, scroll_pause_time=1, scroll_step=200):
        try:
            retries = 0
            while retries < max_retries:
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        expected_conditions.presence_of_element_located((locator))
                    )
                    element_visible = False
                    while not element_visible:
                        self.driver.execute_script(f"window.scrollBy(0, {scroll_step});")
                        time.sleep(scroll_pause_time)
                        if self.is_element_visible(locator):
                            element_visible = True
                    print(f"Элемент успешно найден и видим: {locator}")
                    return element

                except Exception as inner_exception:
                    print(f"Ошибка при прокрутке: {inner_exception}")
                    retries += 1
                    time.sleep(2)
            print(f"Не удалось прокрутить до элемента после {max_retries} попыток.")
            return None
        except Exception as e:
            print(f"Ошибка при прокрутке до элемента: {e}")
            return None

    @allure.step("Клик на элемент")
    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step("Ожидаем видимость и кликабельность элемента")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step("Проверяем отображение элемента")
    def check_element_display(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Ожидание, пока URL не будет содержать актуальный")
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    @allure.step("Ожидание, пока заголовок страницы будет содержать текст")
    def wait_for_title_contains(self, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(lambda driver: text in driver.title,
            f"Заголовок не содержит текст '{text}'. Текущий заголовок: '{self.driver.title}'")
