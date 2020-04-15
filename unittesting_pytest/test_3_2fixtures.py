from mydb_3 import MyDB_1
import pytest

### Using pytest fixtures

@pytest.fixture(scope='module') ## if we define scope = module then it will execute only once
def cur():   
    print('setting up')   ### to print this in console we have to use command pytest -v --capture=no
    db = MyDB_1()
    conn = db.connect('server')
    curs = conn.cursor()
    # return curs       ### replace return with yield and below code then it will not create everytime and close at the end
    yield curs
    curs.close()
    conn.close()
    print('closing DB')


def test_johns2_id(cur):
    # db = MyDB_1()         ### move  this repetative code in setup function
    # conn = db.connect('server')
    # cur = conn.cursor()
    id = cur.execute('select id from employee_db where name=John')
    assert id == 123

def test_toms2_id(cur):
    # db = MyDB_1()          ### move  this repetative code in setup function
    # conn = db.connect('server')
    # cur = conn.cursor()
    id = cur.execute('select id from employee_db where name=Tom')
    assert id == 789