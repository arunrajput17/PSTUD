from mydb_3 import MyDB_1


### Using Setup and Teardown method

conn = None
cur = None

def setup_module(module):       ### Executed before test execution
    print('setting up 1')
    global conn
    global cur
    db = MyDB_1()
    conn = db.connect('server')
    cur = conn.cursor()

def teardown_module(module):    ### Executed after test execution
    print('closing 1')
    cur.close()
    conn.close()

def test_johns_id():
    # db = MyDB_1()         ### move  this repetative code in setup function
    # conn = db.connect('server')
    # cur = conn.cursor()
    id = cur.execute('select id from employee_db where name=John')
    assert id == 123

def test_toms_id():
    # db = MyDB_1()          ### move  this repetative code in setup function
    # conn = db.connect('server')
    # cur = conn.cursor()
    id = cur.execute('select id from employee_db where name=Tom')
    assert id == 789