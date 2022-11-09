import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_bascket_button_is_presented(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    button_text = button.text
    assert "Añadir al carrito" == button_text


