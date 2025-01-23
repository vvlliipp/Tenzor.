import pytest
from data import Url
from pages.page_contacts import PageContacts


class TestContacts:
    def test_contacts_section(self, driver):
        page = PageContacts(driver)

        page.click_contacts()
        page.wait_and_find_office()
        page.click_offices()
        page.wait_and_find_region()
        page.check_region_displayed()
        page.check_list_of_partners_displayed()
        page.click_region()
        page.wait_and_find_region_41()
        page.click_region_41()
        page.wait_and_find_Kamchatka()
        page.check_region_Kamchatka_displayed()
        page.check_list_of_partners_41_displayed()
        page.check_title_contains_kamchatka()
        url = page.wait_url_contains(Url.PAGE_SBIS_41)
        assert Url.PAGE_SBIS_41 in url

