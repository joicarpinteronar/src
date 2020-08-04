from selenium import webdriver


class Browser(object):
    #driver = webdriver.Firefox(executable_path='./driver/geckodriver.exe')
    #driver = webdriver.Ie(executable_path=r"C:\drivers\IEDriverServer\IEDriverServer.exe")
    driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')



    def close(context):
        context.driver.close()
