import allure
from pages.base_page import BasePage
from locators.PageSbis import Sbis


class PageContacts(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на раздел Контакты")
    def click_contacts(self):
        self.click_element(Sbis.contacts)

    @allure.step("Ожидаем видимость и кликабельность ссылки на страницу")
    def wait_and_find_office(self):
        self.wait_and_find_element(Sbis.offices)

    @allure.step("Клик на ссылку офисы")
    def click_offices(self):
        self.click_element(Sbis.offices)

    @allure.step("Ожидаем видимость и кликабельность кнопки региона Свердловская область")
    def wait_and_find_region(self):
        self.wait_and_find_element(Sbis.region)

    @allure.step("Проверяем отображение региона Свердловская область")
    def check_region_displayed(self):
        self.check_element_display(Sbis.region)

    @allure.step("Проверяем отображение списка партнеров Свердловской области")
    def check_list_of_partners_displayed(self):
        self.check_element_display(Sbis.list)

    @allure.step("Клик на Регион")
    def click_region(self):
        self.click_element(Sbis.region)

    @allure.step("Ожидаем видимость и кликабельность кнопки региона Камчатский край в списке")
    def wait_and_find_region_41(self):
        self.wait_and_find_element(Sbis.region_41)

    @allure.step("Клик на регион Камчатский край в списке")
    def click_region_41(self):
        self.click_element(Sbis.region_41)

    @allure.step("Ожидаем видимость и кликабельность кнопки Региона Камчатский край")
    def wait_and_find_Kamchatka(self):
        self.wait_and_find_element(Sbis.region_Kamchatka)

    @allure.step("Проверяем отображение региона Камчатский край")
    def check_region_Kamchatka_displayed(self):
        self.check_element_display(Sbis.region_Kamchatka)

    @allure.step("Проверяем отображение списка партнеров в Камчатском крае")
    def check_list_of_partners_41_displayed(self):
        self.check_element_display(Sbis.list_41)

    @allure.step("Проверяем отображение заголовка")
    def check_title_contains_kamchatka(self):
        return self.wait_for_title_contains("Камчатский", timeout=10)
