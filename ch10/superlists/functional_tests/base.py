from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(self):  #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    @classmethod
    def tearDown(self):  #3
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assetIn(row_text, [row.text for row in rows])
