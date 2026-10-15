import pytest
'''
@pytest.fixture(scope='module')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")
'''
def test_welcome_message_1(greetings):
    print("Welcome Mr. ABC !")
    print("From Module")
def test_welcome_message_2(greetings):
    print("Welcome Mr. XYZ !")
    print("From Module")
def test_welcome_message_3(greetings):
    print("Welcome Mr. Last !")
    print("From Module")