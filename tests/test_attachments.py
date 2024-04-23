import json
import allure
from allure_commons.types import Severity
from allure import attachment_type


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarvar")
@allure.feature("Задачи в репозиторий")
@allure.story("Авторизованный пользователь может создать задачу и репозитории")
@allure.link("https://github.com", name="Testing")

def test_attachments():
    allure.attach("Text content", name="Content from test", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world</h1>", name="HTML", attachment_type=attachment_type.TEXT)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=allure.attachment_type.JSON)
