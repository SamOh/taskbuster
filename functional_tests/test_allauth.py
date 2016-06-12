# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate


# Test for googlelogin. Uses allauth. Setup/teardown, then checks
# Initializes a browser in setUp. WebDriverWait is used to make the
# browser wait a certain amount of time before rising an exception
# when an element is not found. tearDown just quits the browser
# get_element_by_id and get_button_by_id are helper functions that
# use WebDriverWait to find elements by ID. Note that for a button we
# wait until the element is clickable. get_full_url is another helper
# function that we used in other tests. It returns the full url given
# a reverse name. test_google_login is the main test here. It goes to
# the home page and: checks that the login button is present checks that
# the logout button is not present checks that the login button points to
# the correct url (/accounts/google/login) checks that after clicking on
# the login button, the user gets logged in and it sees the logout button instead.
# a click on the logout button should make the user see the login button again.

class TestGoogleLogin(StaticLiveServerTestCase):

    fixtures = ['allauth_fixture']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
            (By.ID, element_id)))

    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable(
            (By.ID, element_id)))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    #
    def user_login(self):
        import json
        with open("taskbuster/fixtures/google_user.json") as f:
            credentials = json.loads(f.read())
        # move cursor to email form and send keys for Email
        self.get_element_by_id("Email").send_keys(credentials["Email"])
        self.get_button_by_id("next").click()
        self.get_element_by_id("Passwd").send_keys(credentials["Passwd"])
        for btn in ["signIn", "submit_approve_access"]:
            self.get_button_by_id(btn).click()
        return

    # def test_google_login(self):
    #     self.browser.get(self.get_full_url("home"))
    #     google_login = self.get_element_by_id("google_login")
    #     with self.assertRaises(TimeoutException):
    #         self.get_element_by_id("logout")
    #     self.assertEqual(
    #         google_login.get_attribute("href"),
    #         self.live_server_url + "/accounts/google/login")
    #     google_login.click()
    #     self.user_login()
    #     with self.assertRaises(TimeoutException):
    #         self.get_element_by_id("google_login")
    #     google_logout = self.get_element_by_id("logout")
    #     google_logout.click()
    #     google_login = self.get_element_by_id("google_login")
