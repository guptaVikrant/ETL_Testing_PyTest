import pandas as pd
import pytest
import pymysql
from sqlalchemy import create_engine
'''
@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Runs before each test")
    yield
    print("Runs after each test")

mysql_engine=create_engine("mysql+pymysql://root:Radha%40150683@localhost:3306/vikrantdb")
mysql_conn=mysql_engine.connect()
#without fixture
def test_rowcount_check():
    df1=pd.read_sql("select count(*) from product",mysql_conn)
    df_source=pd.read_sql("select * from product",mysql_conn)
    print("\n")
    row_count=len(df_source)
    expected_rowcount=100
    assert row_count == expected_rowcount, "Row count is mismatched"
    print(df_source.head())
'''

def test_data(get_df_source, get_df_tgt):
    assert get_df_source.equals(get_df_tgt), "Different data"

#with using fixture
def test_countchk1(get_df):
    count_actual=len(get_df)
    count_expected=20
    assert count_actual == count_expected, "Counts are not equal"

def test_countchk2(get_df):
    df_size=get_df.size
    print("df_size:",df_size)

def test_countchk3(get_df):
    df_count=get_df.count()
    print("df_count:",df_count)

@pytest.mark.regression
@pytest.mark.parametrize("a,b,c,expected", [(2,3,4,25), (5,3,2,30), (10, 5, 2,150)])
def test_multiply(a,b,c,expected):
    assert a*b*c == expected

@pytest.mark.smoke
@pytest.mark.parametrize("a,b,expected", [(6,3,2), (5,3,2), (10, 5, 3)])
def test_divide_param(a,b,expected):
    assert a/b == expected
@pytest.mark.skip(reason="Not ready yet")
def test_divide():
    assert False, "skipped"

@pytest.mark.xfail  #expected failed
def test_fail_abc():
    assert 10!=10, "Failed"

@pytest.mark.smoke
def test_welcome1():
    print("Welcome into smoke test")

@pytest.mark.regression
def test_welcome2():
    print("Welcome into regression test")


