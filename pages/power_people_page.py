import allure
from locators.PageTenzor import Tenzor
from pages.base_page import BasePage
from locators.PageSbis import Sbis


class PageWork(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем видимость и кликабельность баннера Тензор")
    def wait_and_find_tenzor_banner(self):
        self.wait_and_find_element(Sbis.banner_tenzor)

    @allure.step("Клик на баннер Тензор")
    def click_tenzor_banner(self):
        self.click_element(Sbis.banner_tenzor)

    @allure.step("Проверяем отображение блока Сила в людях")
    def power_is_in_people_displayed(self):
        self.check_element_display(Tenzor.power_is_in_people)

    @allure.step("Клик на кнопку Подробнее")
    def click_detailed(self):
        self.click_element(Tenzor.detailed)

    @allure.step("Проверяем отображение блока Работаем")
    def section_work_displayed(self):
        self.check_element_display(Tenzor.working_section)

    @allure.step("Получение размеров картины")
    def get_images_sizes(self):
        sizes = []
        images = self.driver.find_elements(Tenzor.images_in_chronology)
        for img in images:
            width = int(img.get_attribute('width'))
            height = int(img.get_attribute('height'))
            sizes.append((width, height))
        return sizes
