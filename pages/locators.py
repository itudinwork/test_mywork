from selenium.webdriver.common.by import By
class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BASKET_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")