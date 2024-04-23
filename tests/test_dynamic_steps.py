import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarvar")
@allure.feature("Поиск репозиторий")
@allure.story("Шаги через with allure.step")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('')

    with allure.step('Ищем репозиторию'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()

    with allure.step('Переходим по ссылке репозитории'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем tab Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем Issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)
