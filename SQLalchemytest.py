from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import *

db_host = "gaz-db-1.cayzc8scmde6.us-west-2.rds.amazonaws.com"
db_port = 3306
db_user = "root"
db_pass = "O8^dTW8X9.6S9=E"
db_name = "ECO_test_1"

connection_string = "mysql+mysqlconnector://%s:%s@%s:%s/%s" % (db_user,db_pass,db_host,db_port,db_name)
engine = create_engine(connection_string)

Base = automap_base()
Base.prepare(engine,reflect=True)

Dimensions_dictionary = Base.classes.Dimensions_dictionary



metadata = MetaData()
metadata.reflect(engine)
print (metadata.tables.keys())

