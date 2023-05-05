import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestGoogleSearch:

    def teardown_method(self):
        # close the browser window
        self.driver.quit()

    def test_search_example_on_google_by_chrome(self):
        # create a new Chrome web driver instance
        self.driver = webdriver.Chrome()
        # navigate to Google.com
        self.driver.get('https://www.google.com')

        # find the search input element
        search_input = self.driver.find_element(By.NAME, 'q')

        # enter the search query "example" into the search input element
        search_input.send_keys('example')

        # submit the search query by pressing the Enter key
        search_input.send_keys(Keys.RETURN)

        # verify that the search results page contains the word "example"
        assert 'example' in self.driver.page_source.lower()

    def test_search_example_on_google_by_firefox(self):
        # create a new Firefox web driver instance
        self.driver = webdriver.Firefox()
        # navigate to Google.com
        self.driver.get('https://www.google.com')

        # find the search input element
        search_input = self.driver.find_element(By.NAME, 'q')

        # enter the search query "example" into the search input element
        search_input.send_keys('example')

        # submit the search query by pressing the Enter key
        search_input.send_keys(Keys.RETURN)

        # verify that the search results page contains the word "example"
        assert 'example' in self.driver.page_source.lower()

    def test_search_example_on_google_by_edge(self):
        # create a new Edge web driver instance
        self.driver = webdriver.Edge()
        # navigate to Google.com
        self.driver.get('https://www.google.com')

        # find the search input element
        search_input = self.driver.find_element(By.NAME, 'q')

        # enter the search query "example" into the search input element
        search_input.send_keys('example')

        # submit the search query by pressing the Enter key
        search_input.send_keys(Keys.RETURN)

        # verify that the search results page contains the word "example"
        assert 'example' in self.driver.page_source.lower()


if __name__ == '__main__':
    pytest.main()
