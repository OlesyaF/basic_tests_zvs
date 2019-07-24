import json

import pytest

from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        # agent_password = request.config.getoption("--agent_password") - так задавать параметр, если вводить при запуске тестов
        fixture = Application(ov_url=target['ov_url'], client_login=target['client_login'], client_password=target['client_password'], arm_ric_url=target['arm_ric_url'],
                              agent_login=target['agent_login'], agent_password=target['agent_password'], browser=target['browser'], resource=target['resource'],
                              kit=target['kit']) #agent_password=agent_password - так задавать параметр, если вводить при запуске тестов
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default=r'C:\Tools\target.json')
    # parser.addoption("--agent_password", action="store", default="8n43jyfu") - так задавать параметр, если вводить при запуске тестов

