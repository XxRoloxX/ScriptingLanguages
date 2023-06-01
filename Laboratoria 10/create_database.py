from typing import Optional
from cmd_arguments_utils import get_line_arguments
from db_management import get_db_engine
import models
from sqlalchemy import create_engine

DEFAULT_DB_NAME:str = "default_db_name"
DATABASE_URL:str = "sqlite://"
DATABASE_TYPE = "sqlite3"

def create_db(db_name:str):
    engine = get_db_engine(DATABASE_URL, db_name, DATABASE_TYPE)
    models.Base.metadata.create_all(engine)

def main():
    input_db_name = get_line_arguments(1)[0]
    final_db_name = input_db_name if input_db_name else DEFAULT_DB_NAME
    create_db(final_db_name)

if __name__=="__main__":
    main()

