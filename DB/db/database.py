import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    postgres_id = 'postgres'
    postgres_pw = 'postgres'
    postgres_db = 'postgres'
    postgres_ip = 'localhost'
    postgres_port = '5432'
    SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_id}:{postgres_pw}@{postgres_ip}:{postgres_port}/{postgres_db}"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Session = sessionmaker(bind=engine)
    Base = declarative_base()

    List = list()
    iList = list()

    conn = engine.connect()
    try:
        select_query = "select * from user_db"
        select_query2 = "select * from log"
        result = conn.execute(select_query)
        result2 = conn.execute(select_query2)

        for _r in result:
            List.append(_r)

        cnt = 0

        for _r in result2:
            iList.append(_r[0])
        try:
            iList = iList[-1]
        except IndexError:
            pass
    except sqlalchemy.exc.ProgrammingError:
        pass
except sqlalchemy.exc.OperationalError:
    print("DOCKER 을 켜 주세요.")
