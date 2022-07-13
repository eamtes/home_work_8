from selenium.webdriver.common.by import By


class Success_Alert:
    SELF = (By.CSS_SELECTOR, ".alert-success")
    LOGIN = (By.LINK_TEXT, "login")
    SOPPING_CART = (By.PARTIAL_LINK_TEXT, "shopping cart")
    PRODUCT_COMPARISON = (By.LINK_TEXT, "product comparison")


class User_Login_Form:
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")


class Cart_Page:
    BUTTON_REMOVE = (By.CSS_SELECTOR, "[data-toggle=tooltip][onclick^=cart]")
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    TEXT_CART_IS_EMPTY = "//div[@id='content']//p[text()='Your shopping cart is empty!']"
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")
    CONTENT = (By.CSS_SELECTOR, "#content")


class Cart_Product_Page:
    DOT = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    LINK_HP = (By.CSS_SELECTOR, "a[href$='hewlett-packard']")
    BUTTON_CART = (By.CSS_SELECTOR, "button#button-cart")
    INPUT_OPTION_255 = (By.CSS_SELECTOR, "#input-option225")
    BUTTON_ONCLICK_COMPARE = (By.CSS_SELECTOR, "button[onclick^='compare']")


class Catalog_Page:
    INPUT_LIMIT = (By.ID, "input-limit")
    INPUT_SORT = (By.ID, "input-sort")
    LIST_VIEV = (By.ID, "list-view")
    GRID_VIEV = (By.ID, "grid-view")
    COLUMN_LEFT = (By.ID, "column-left")
    LAPTOP_HP_3065 = (By.CSS_SELECTOR, "[alt$='3065']")


class Login_Page:
    BUTTON_CONTINUE_FOR_LOGOUT = (By.CSS_SELECTOR, ".pull-right [href$='common/home']")
    LINK_REGISTER = (By.CSS_SELECTOR, "a[href$='register'].btn")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[value='Login']")
    PLACEHOLDER_MAIL = (By.CSS_SELECTOR, "[placeholder='E-Mail Address']")
    PLACEHOLDER_PASSWORD = (By.CSS_SELECTOR, "[placeholder='Password']")
    LINK_FORGOTTEN = (By.CSS_SELECTOR, "div.form-group>a[href$='forgotten']")
    TEXT_ACCOUNT_LOGOUT = "//div[@id='content']//h1[text()='Account Logout']"


class Main_Page:
    BUTTON_MY_ACCOUNT = (By.CSS_SELECTOR, "[title$=Account]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[href$='account/login']")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "[href$='account/logout']")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[href$='account/register']")
    BUTTON_DESKTOPS = (By.CSS_SELECTOR, "[href$=desktops].dropdown-toggle")
    BUTTON_SHOW_ALL_DESKTOPS = (By.CSS_SELECTOR, "[href$=desktops].see-all")
    BUTTON_CURRENCY = (By.CSS_SELECTOR, "[class=btn-group] [data-toggle=dropdown]")
    CURRENCY_EURO = (By.CSS_SELECTOR, "[name=EUR]")
    CURRENCY_POUND_STERLING = (By.CSS_SELECTOR, "[name=GBP]")
    CURRENCY_US_DOLLAR = (By.CSS_SELECTOR, "[name=USD]")
    IMG_MACBOOK = (By.CSS_SELECTOR, "img[title*=MacBook]")
    IMG_IPHONE = (By.CSS_SELECTOR, "img[title*=iPhone]")
    SEARCH = (By.NAME, "search")
    CART_TOTAL = (By.ID, "cart-total")
    LINK_TEXT_OPENCART = (By.LINK_TEXT, "OpenCart")
    FEATURE_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    FEATURE_PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")


class Product_Page:
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[type=button]#button-cart")
    ADD_TO_COMPARISON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")


class Register_Page:
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[name=firstname]")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "[name=lastname]")
    FIELD_EMAIL = (By.CSS_SELECTOR, "[name=email]")
    FIELD_TELEPHONE = (By.CSS_SELECTOR, "[name=telephone]")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "[name=password]")
    FIELD_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "[name=confirm]")
    CHECKBOX_PRIVACY_POLICY = (By.CSS_SELECTOR, "[name=agree]")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "[value=Continue]")
    BUTTON_CONTINUE_AFTER_REGISTRATION = (By.CSS_SELECTOR, ".buttons [href$='account/account']")
    BUTTON_SUCCESS = (By.CSS_SELECTOR, "[href$='account/success']")
    SUBSCRIBE_YES = (By.CSS_SELECTOR, "input[name='newsletter'][value='1']")
    SUBSCRIBE_NO = (By.CSS_SELECTOR, "input[name='newsletter'][value='0']")
    LINK_PRIVACY_POLICY = (By.CSS_SELECTOR, ".agree")


class User_Page:
    SHOPPING_CART = (By.CSS_SELECTOR, "[title='Shopping Cart']")
    BACK_TO_MAIN_PAGE = (By.CSS_SELECTOR, "[href$='common/home'] [title='Your Store']")
    PAYMENT_FORM = (By.CSS_SELECTOR, "#payment-new")
