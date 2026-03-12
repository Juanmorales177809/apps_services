from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

database_url = "postgresql://admin:admin@190.248.28.132:3010/postgres"
engine = create_engine(database_url)

Base = declarative_base()

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

