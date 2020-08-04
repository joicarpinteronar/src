from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Actions.variuos_functions import VariousFunctions
from Locators.locators import get_locator
from Features.browser import Browser
from selenium.webdriver import ActionChains
from allure.constants import AttachmentType
import allure
import time

functions_ = VariousFunctions()

class Actions(Browser):

    def clear(self,locator):
        self.driver.find_element(*get_locator(locator)).clear()

    def fill_field(self, text, locator):
        try:
            if text == "random":
               text = functions_.random("AUT_")
               self.driver.find_element(*get_locator(locator)).send_keys(text)
            else:
               self.driver.find_element(*get_locator(locator)).send_keys(text)
        except NoSuchElementException:
            print('no se encontró el elemento')

    def click_element(self, locator):
        try:
            time.sleep(1)
            self.driver.find_element(*get_locator(locator)).click()
            return True
        except NoSuchElementException:
            print('no se encontró el elemento')
            return False

    def scroll_interno(self, locator):
        element = self.driver.find_element(*get_locator(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        #element.location_once_scrolled_into_view

    def navigate(self, address):
       self.driver.get(address)
       self.driver.implicitly_wait(40)
       self.driver.set_page_load_timeout(40)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term, locator):
        self.fill_field(search_term, *get_locator(locator))
        self.click_element(*get_locator(locator))

    def get_text(self, locator):
        try:
            time.sleep(2)
            message = self.driver.find_element(*get_locator(locator)).text
            return message
        except NoSuchElementException:
            return False
      #allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
      # def put_screenshot(self):
      #  allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
     #   allure.attach(self.driver.get_screenshot_as_png(),
           #           attachment_type=allure.attachment_type.PNG)

    def drag_and_drop(self,source_element,dest_element):
        source_element = self.driver.find_element(*get_locator(source_element))
        dest_element = self.driver.find_element(*get_locator(dest_element))
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()

    def count_elements(self):
        #print(self.driver.find_elements(*get_locator("//div[@class='dx-datagrid-group-panel']")))
        #list_elements = self.driver.findElement(By.XPATH("//td[contains(@role,'columnheader')]"))
        print("")

    def hover(self,element):
        time.sleep(2)
        element_to_hover_over = self.driver.find_element(*get_locator(element))
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()
        self.driver.implicitly_wait(40)

    def double_click(self,element):
        element_to_double_clic = self.driver.find_element(*get_locator(element))
        ActionChains(self.driver).double_click(element_to_double_clic).perform()

    def send_keys(self,text, locator):
        time.sleep(1)
        self.driver.find_element(*get_locator(locator)).send_keys(text)
        #self.driver.find_element(*get_locator(locator)).send_keys(Keys.ENTER)
    def prueba(self):
       # time.sleep(2)
       # elem1 = self.driver.find_element_by_xpath("/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[2]/div/div/div[4]/div")
       # elem1.click()
        
        time.sleep(1)
        elem = self.driver.find_element_by_xpath("//div[4]/div")
        
        elem.send_keys("pycon")
        #elem.send_keys("pycon")
        #elem1.ENTER
        
        time.sleep(1)

    def select_fill(self,option,locator):
        time.sleep(2)
        select = Select(self.driver.find_element(*get_locator(locator)))
        #select.select_by_index(option)
        select.select_by_visible_text(option)
        
        #select.select_by_value(value)
    def select_dropdown_value(self, locator, value):
        selectOption = Select(self.driver.find_element(*get_locator(locator)))
        option_selected = selectOption.select_by_value(value)

    def is_element_located(self,locator):
        delay = 10  # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(*get_locator(locator)))
            print ("Page is ready!")
            return True
        except TimeoutException:
            print ("Loading took too much time!")
            return False
