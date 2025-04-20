
# postgresql+psycopg://postgres-POSTGRES_USER:asdf@localhost:5432/timescaledb


import sqlmodel


engine = sqlmodel.create_engine("postgresql+psycopg://postgres-POSTGRES_USER:asdf@localhost:5432/timescaledb")

def init_db():
    print("crating db")
    sqlmodel.SQLModel.metadata.create_all(engine)

def get_session():
    with sqlmodel.Session(engine) as session:
        yield session