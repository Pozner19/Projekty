#-*-coding: utf *8 -*-
from selenium import webdriver
import unittest
from time import sleep

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page/#/")

    def test_invalid_email(self):
        driver = self.driver
        zaloguj_btn = driver.find_element_by_css_selector("#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button")
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_css_selector("#login-modal > form > div > p > button")
        rejestracja_btn.click()

        imie = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        imie.send_keys('Rafal')
        nazwisko = driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        nazwisko.send_keys('Poznerowicz')

        plec = driver.find_element_by_id("register-gender-male")
        plec.click()

        tel = driver.find_element_by_css_selector("#regmodal-scroll-hook-3 > input")
        tel.send_keys(123445678)

        email = driver.find_element_by_css_selector("#regmodal-scroll-hook-4 > div.rf-input__inner > label > input")
        email.send_keys('rafalrafal.pl')

        haslo = driver.find_element_by_css_selector("#regmodal-scroll-hook-5 > div.rf-input__inner > label > input")
        haslo.send_keys('Anna1234')

        obywatelstwo = driver.find_element_by_css_selector("#regmodal-scroll-hook-6 > div.rf-input__inner > label > input")
        obywatelstwo.click()

        kraj= driver.find_element_by_xpath('//*[@class="register-form__country-container__locations"]/label[164]')
        kraj.location_once_scrolled_into_view
        kraj.click()

        politykaprywatnosci = driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[10]/span/label[1]')
        politykaprywatnosci.click()

        error_notice = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span')
        print(error_notice.text)
        assert error_notice.is_displayed
        # rejestrecja_button =driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[11]/button')
        # rejestrecja_button.click()

        sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
