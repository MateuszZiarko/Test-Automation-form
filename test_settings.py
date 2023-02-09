class TestSettings:
    page_url = "https://cv.parleto.io/jobs/task/066bd6df-22f2-4957-b2a9-2c8d78d2ad55/"

    # Form Tab
    xpath_form_osoba = "//input[@placeholder='imię i nazwisko']"
    xpath_form_pesel = "//input[@prop='pesel']"
    xpath_form_data_urodzenia = "//div[@class='el-form-item is-required']//div[@class='el-tooltip el-input']//input[@type='text']"
    xpath_form_email = "//div[4]//div[1]//div[1]//input[1]"
    xpath_form_haslo = "//div[5]//div[1]//div[1]//input[1]"
    xpath_form_powtorz_haslo = "//div[6]//div[1]//div[1]//input[1]"
    xpath_form_wyslij_button = "//div[@class='el-form-item__content']/button[@type='button']"
    xpath_form_pesel_button = "//span[@class='el-checkbox__inner']"
    xpath_form_actual_errors = "//div[@class='el-form-item__error']"
    id_form_button = "el-button el-button--primary"
