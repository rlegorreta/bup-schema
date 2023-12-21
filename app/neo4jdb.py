import os
import logging
from neo4j import GraphDatabase


# ============================================================================================================
# Opens the 'current' database and executes queries
# ============================================================================================================
class Neo4jDB:

    def __init__(self, host):
        user = os.getenv("NEO4J_USER")  # we supposed both DB has same user and password set
        password = os.getenv("NEO4J_PASSWORD")
        self.driver = GraphDatabase.driver(host, auth=(user, password))
        logging.debug(f'Database {host} opened')

    def run_query(self, query, params={}):
        with self.driver.session() as session:
            result = session.run(query, params)
            return result.to_df()

    def run_query_no_df(self, query, params={}):
        with self.driver.session() as session:
            result = session.run(query, params)
            output = [r.values() for r in result]
            output.insert(0, result.keys())
            return output


def setSchema(schema):
    if schema == '1':
        return os.getenv("NEO4J_HOST_HEALTH_CARE")

    return os.getenv("NEO4J_HOST_BUP")


# This is just a temporary procedure to generate locally the health-care database
class DownLoadNeo4j:

    def __init__(self):
        user = 'neo4j'
        password = 'meters-mosses-catch'
        host = 'bolt://3.89.19.99:7687'
        self.driver = GraphDatabase.driver(host, auth=(user, password))
        logging.info(f'Database {host} opened')

    def run_query(self, query, params={}):
        with self.driver.session() as session:
            result = session.run(query, params)
            return list(result)
