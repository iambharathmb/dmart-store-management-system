import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening MySQL Connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='root123', database='dmart_store_management_system')

  return __cnx