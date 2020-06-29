from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(by, element):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, element)))


driver = webdriver.Firefox()
driver.get("https://www.notion.so/CyberSecurity-ac15517049f043778ab10fb5c9158a50")
email_field = wait_for_element(By.XPATH, '//input[@type="email"]')
email_field.clear()
email_field.send_keys('replace with username')
continue_button = wait_for_element(By.CSS_SELECTOR, '.notion-login > div:nth-child(2) > div:nth-child(4)')
continue_button.click()
password_field = wait_for_element(By.XPATH, '//input[@type="password"]')
password_field.clear()
password_field.send_keys('replace with password')
continue_button = wait_for_element(By.CSS_SELECTOR, '.notion-login > div:nth-child(2) > div:nth-child(6)')
continue_button.click()
see_more_button = wait_for_element(By.CSS_SELECTOR, '#notion-app > div > div.notion-cursor-listener > div.notion-frame '
                                                    '> div:nth-child(1) > div.notion-topbar > div > div:nth-child(3) > '
                                                    'div.notion-topbar-more-button')
see_more_button.click()
export_button_option = wait_for_element(By.CSS_SELECTOR, 'div.notion-scroller:nth-child(1) > div:nth-child(1) > '
                                                         'div:nth-child(6) > 6div:nth-child(2)')
export_button_option.click()
include_subpage_toggle = wait_for_element(By.CSS_SELECTOR, 'div.notion-overlay-container:nth-child(2) > div:nth-child'
                                                           '(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child'
                                                           '(1) > div:nth-child(2) > div:nth-child(2)')
include_subpage_toggle.click()
