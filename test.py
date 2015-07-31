import mysql.connector

db_host = "gaz-db-1.cayzc8scmde6.us-west-2.rds.amazonaws.com"
db_port = 3306
db_user = "root"
db_pass = "O8^dTW8X9.6S9=E"
db_name = "ECO_test_1"


def connect():
    try:
        con = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name, use_unicode=1)
    except mysql.connector.Error as err:
        print(err)
    return con


def connection_reset(con):
    if con.in_transaction:
        print('reseting....')
        con.rollback()


def insert_dimension(con, id, description):
    add_dimensions = "INSERT INTO Dimensions_dictionary (ID_DIMENSION, DIMENSION_DESCRIPTION) VALUES (%s,'%s')" % (
    id, description)
    cursor = con.cursor()
    print(add_dimensions)
    cursor.execute(add_dimensions)
    con.commit()


def insert_param(con, id, id_dimension, secret, description):
    add_param = "insert into Params_dictionary (ID_PARAM, ID_DIMENSION, IS_SECRET, PARAM_DESCRIPTION) values (%s,%s,%s,'%s')" % (id, id_dimension,secret,description)
    cursor = con.cursor()
    print(add_param)
    cursor.execute(add_param)
    con.commit()


def fill_dicts(con):
    dimensions_dict = {0: "мг/м3", 1: "PPM", 2: "г/с", 3: "м3/с", 4: "град.С", 5: "%", 6: "м/с", 7: "атм"}
    con.cursor().execute("truncate Dimensions_dictionary")
    # for key, value in dimensions_dict.items():
        # print (str(key)+":"+value)
        # insert_dimension(con, key, value)

    param_list = [[301,"Показаель 1",2,int(False)], [30101,"Показатель 2",0,int(True)]]

    for key in param_list:
        print(key)
        insert_param(con, key[0], key[2], key[3], key[1])

def helloWorld(name):
    print("ia am {_name}".format(_name=name))


con = connect()
fill_dicts(con)
helloWorld('sergey')
