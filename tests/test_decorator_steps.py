import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarvar")
@allure.feature("Поиск репозиторий")
@allure.story("Декораторы")
@allure.link("https://github.com", name="Testing")

def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('')


@allure.step('Ищем репозиторию{repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).submit()

@allure.step('Переходим по ссылке репозитория{repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем tab Issues')
def open_issue_tab():
    s('#issues-tab').click()

@allure.step('Проверяем Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()