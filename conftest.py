import pandas as pd
import pytest
from sqlalchemy import create_engine

mysql_engine=create_engine("mysql+pymysql://root:Radha%40150683@localhost:3306/vikrantdb")
mysql_conn=mysql_engine.connect()
'''
@pytest.fixture(scope='session')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Runs before each test")
    yield     
    print("Runs after each test")
'''
#define a fixture to connect a database
@pytest.fixture(scope='session')
def get_df():
    print("Start database connection and getting dataframe")
    df_source = pd.read_sql("select * from product", mysql_conn)
    yield df_source
    print("closing connection")

@pytest.fixture
def get_df_source():
    df_source = pd.read_csv("Data/Employee.csv")
    yield df_source

@pytest.fixture
def get_df_tgt():
    df_tgt = pd.read_csv("Data/Employee1.csv")
    yield df_tgt