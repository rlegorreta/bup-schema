import os
import logging
from dotenv import load_dotenv
from app.neo4jdb import DownLoadNeo4j
from app.schema import Schema

load_dotenv()  # note: this line must be commented when we want to dockerize it

# ============================================================================================================
# Main body
# ============================================================================================================
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.info(f'Start application:{os.getenv("APP_NAME")} version:{os.getenv("VERSION")}')
    if logging.getLogger().level == logging.DEBUG:
        schema = Schema(0)
        answer = schema.ask("""
        ¿Cuál es la compania con mas proveedores?
        """)
        print(f'The answer is: \n {answer}')
        answer = schema.ask("""
        ¿Quienes son la personas que trabajan en la compania ACME SA de CV?
        """)
        print(f'The answer is: \n {answer}')
        answer = schema.ask("""
        ¿Que email tiene la persona Diego?
        """)
        print(f'The answer is: \n {answer}')
    if logging.getLogger().level == logging.INFO:
        schema = Schema(1)
        answer = schema.ask("""
        What are the top 5 side effects reported?
        """)
        print(f'The answer is: \n {answer}')
        answer = schema.ask("""
        What are the top 3 manufacturing companies with the most reported side effects?
        """)
        print(f'The answer is: \n {answer}')
        answer = schema.ask("""
        What are the top 3 manufacturing companies with the most reported cases?
        """)
        print(f'The answer is: \n {answer}')
        answer = schema.ask("""
        What are the top 5 drugs whose side effects resulted in death of patients 
        as an outcome?
        """)
        print(f'The answer is: \n {answer}')
    if logging.getLogger().level == logging.DEBUG:
        neo4j = DownLoadNeo4j()
        result = neo4j.run_query("""
        CALL apoc.export.cypher.all(null, {
            format: "cypher-shell",
            stream:true,
            useOptimizations: {type: "UNWIND_BATCH", unwindBatchSize: 20}
        })
        """)
        file = open('health_care.cypshell', 'w')
        for res in result:
            file.write(res[10])
        file.close()


