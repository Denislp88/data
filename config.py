host = "Denis88.mysql.pythonanywhere-services.com"
user = "Denis88"
password = "89124662375Zaq1xsw2cde3"
db_name = "Denis88$default"




   #
from mysql.connector import connect, Error

try:
   with connect(
            host="Denis88.mysql.pythonanywhere-services.com",
            user="Denis88",
            passwd="89124662375Zaq1xsw2cde3"
    ) as connection:
        print(connection)
except Error as e:
   print(e)
   #