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
        browser = request.config.getoption("--browser")
        resource = request.config.getoption("--resource")
        ov_url = request.config.getoption("--ov_url")
        client_login = request.config.getoption("--client_login")
        client_password = request.config.getoption("--client_password")
        arm_ric_url = request.config.getoption("--arm_ric_url")
        agent_login = request.config.getoption("--agent_login")
        agent_password = request.config.getoption("--agent_password")
        kit = request.config.getoption("--kit")
        fixture = Application(ov_url=ov_url, client_login=client_login, client_password=client_password, arm_ric_url=arm_ric_url,
                              agent_login=agent_login, agent_password=agent_password, browser=browser, resource=resource, kit=kit) #agent_password=target['agent_password'] - так задавать параметр, если брать из target.json
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--resource", action="store", default="dt")
    parser.addoption("--ov_url", action="store", default="http://dt-kplustest1.kc.kplus/chat/cgi/online.cgi")
    parser.addoption("--client_login", action="store", default="152_980557")
    parser.addoption("--client_password", action="store", default="password")
    parser.addoption("--arm_ric_url", action="store", default="https://zv6.consultant.ru/zv/index.pl")
    parser.addoption("--agent_login", action="store", default="ric996fesaiou")
    parser.addoption("--agent_password", action="store", default="8n43jyfu")
    parser.addoption("--kit", action="store", default="SPK-V_980557")
