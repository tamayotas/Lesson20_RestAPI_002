from selene import browser, by, have
from tests.conftest import LOGIN, PASSWORD, BASE_URL
from utils.utils import send_post_request


def test_add_product_with_params(open_browser):
    response = send_post_request("login", data={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response2 = send_post_request("addproducttocart/details/72/1", data={
        "product_attribute_72_5_18": 53,
        "product_attribute_72_6_19": 54,
        "product_attribute_72_3_20": 57,
        "product_attribute_72_8_30": 93,
        "addtocart_72.EnteredQuantity": 1}, allow_redirects=False, cookies={"NOPCOMMERCE.AUTH": cookies})
    assert response2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element('.product-name').should(have.text("Build your own cheap computer"))
    browser.element(".remove-from-cart").click()
    browser.element(".update-cart-button").press_enter()


def test_add_product_without_params(open_browser):
    response = send_post_request("login", data={"Email": LOGIN, "Password": PASSWORD},
                                 allow_redirects=False)
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response2 = send_post_request("addproducttocart/catalog/31/1/1", cookies={"NOPCOMMERCE.AUTH": cookies})
    assert response2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element('.product-name').should(have.text("14.1-inch Laptop"))
    browser.element(".remove-from-cart").click()
    browser.element(".update-cart-button").press_enter()