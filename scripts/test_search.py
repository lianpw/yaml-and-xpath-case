import os, sys
sys.path.append(os.getcwd())
import pytest
from page.page_search import PageSearch
from base.get_driver import get_driver
from tools.read_data import read_data


def get_data(key):
    return read_data('search_data.yml')[key]


class TestSearch:

    def setup(self):
        self.driver = get_driver()
        self.search = PageSearch(self.driver)

    @pytest.mark.parametrize("value", get_data('test_search'))
    def test_search(self, value):
        self.search.page_click_search()
        self.search.page_input_value(value)
        self.search.page_back_btn()

    def teardown(self):
        self.driver.quit()