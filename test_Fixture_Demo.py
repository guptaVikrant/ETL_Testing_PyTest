import pytest
'''
@pytest.fixture(scope='function')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")
'''
def test_welcome_message_1(greetings):
    print("Welcome Mr. ABC !")
    print("From Demo")
def test_welcome_message_2(greetings):
    print("Welcome Mr. XYZ !")
    print("From Demo")