import pytest
from data import Url
from pages.power_people_page import PageWork
from locators.PageTenzor import Tenzor
from pages.page_contacts import PageContacts


class TestImages:
    def test_images_sizes(self, driver):
        page_work = PageWork(driver)
        page = PageContacts(driver)

        page.click_contacts()
        page.wait_and_find_office()
        page.click_offices()
        page_work.wait_and_find_tenzor_banner()
        page_work.click_tenzor_banner()
        page_work.scroll_to_element(Tenzor.power_is_in_people)
        page_work.power_is_in_people_displayed()
        page_work.click_detailed()
        page_work.scroll_to_element(Tenzor.working_section)
        images_sizes = page_work.get_images_sizes()
        assert len(set(images_sizes)) == 1, f"Изображения имеют разные размеры: {images_sizes}"

    def test_tenzor_page_open(self, driver):
        page_work = PageWork(driver)
        page = PageContacts(driver)

        page.click_contacts()
        page.click_offices()
        page_work.click_tenzor_banner()
        page_work.scroll_to_element(Tenzor.power_is_in_people)
        page_work.power_is_in_people_displayed()
        page_work.click_detailed()
        url = page.wait_url_contains(Url.PAGE_TENZOR_ABOUT)
        assert Url.PAGE_TENZOR_ABOUT in url

