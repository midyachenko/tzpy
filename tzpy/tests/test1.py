# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class AppJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.firefox.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_yandex_market(self):
        driver = self.driver
        #Тест 1
        #Открыть страницу Гугл поиска
        driver.get("https://www.google.com/?gws_rd=ssl")
        #в поисковике ввести яндекс маркет
        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys(u"яндекс маркет")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #ожидание результата поиска
        time.sleep(2)
        #перейти по ссылке
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Веб-результат со ссылками на сайт'])[1]/following::h3[1]").click()
        #Смотрим результат
        time.sleep(2)
        #Тест 2
        # Открыть страницу яндекс маркет
        driver.get("https://market.yandex.ru/")
        # в поисковике ввеcти пылесосы
        driver.find_element_by_id("header-search").click()
        driver.find_element_by_id("header-search").clear()
        driver.find_element_by_id("header-search").send_keys(u"пылесосы")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='пылесосы'])[1]/following::button[1]").click()
        #Выполнить нажатие на кнопку Все фильтры
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Показать всё'])[2]/following::span[1]").click()
        #Выбрать в списке Polaris и Vitek
        # Внимание! Значения xpath Яндекса некорректно...
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Philips'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Thomas'])[1]/following::label[1]").click()
        #Установить  цену в поле  до = 6000
        driver.find_element_by_id("glf-priceto-var").click()
        driver.find_element_by_id("glf-priceto-var").clear()
        driver.find_element_by_id("glf-priceto-var").send_keys("6000")
        time.sleep(2)
        #Нажать Показать подходящие
        driver.find_element_by_link_text(u"Показать подходящие").click()
        # Смотрим результаты
        time.sleep(5)

        #Проверить что данные из фильтра  отобразились в настройках с права
        #Проверяем чекбоксы
        assert driver.find_element_by_id('onstock').get_attribute('checked'), "checkbox В продаже is unchecked"
        assert driver.find_element_by_id('7893318_288426').get_attribute('checked'), "checkbox Polaris is unchecked"
        assert driver.find_element_by_id('7893318_152837').get_attribute('checked'), "checkbox VITEK is unchecked"
        #Если раскомментить выпадет исключение на пустой чекбокс по Bosch например
        #assert driver.find_element_by_id('7893318_152900').get_attribute('checked'), "checkbox Bosch is unchecked"

        #Проверяем максимальную цену
        assert driver.find_element_by_id('glpriceto').get_attribute('value')=="6000", "price limit incorrect"

        time.sleep(5)
        driver.close()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
