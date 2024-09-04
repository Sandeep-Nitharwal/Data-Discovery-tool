import sqlalchemy
from sqlalchemy import create_engine

def connect_to_database(db_uri):
    engine = create_engine(db_uri)
    connection = engine.connect()
    return connection

def fetch_data_from_database(connection, query):
    result = connection.execute(query)
    return result.fetchall()
