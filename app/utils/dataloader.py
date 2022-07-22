import mysql.connector
import pandas as pd
import settings

db_config = {
    "host": settings.DB_HOST,
    "database": settings.DB_NAME,
    "password": settings.DB_PASSWORD,
    "user": settings.DB_USERNAME,
}


def create_db_connection():
    """
    Creates connection to the database
    :return: connection
    """
    return mysql.connector.connect(**db_config)


def get_query(sql):
    connection = create_db_connection()
    data = pd.read_sql_query(sql, connection)
    connection.close()

    return data
