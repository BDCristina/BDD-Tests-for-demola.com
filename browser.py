from selenium import webdriver


class Browser:
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    driver.maximize_window()

    def close(self):
        self.driver.close()
