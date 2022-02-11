from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgres_id = 'postgres'
postgres_pw = 'conversionBinary'
postgres_db = 'conversion'
postgres_ip = '127.0.0.1'
postgres_port = '5432'
SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_id}:{postgres_pw}@{postgres_ip}:{postgres_port}/{postgres_db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
