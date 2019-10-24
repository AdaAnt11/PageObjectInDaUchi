from UchiPages import LoginStudent

def test_student_login(browser):
    uchi_main_page = LoginStudent(browser)
    uchi_main_page.go_to_site()
    uchi_main_page.enter_login_data(login=22, password='космос')
    uchi_main_page.click_on_the_login_button()

