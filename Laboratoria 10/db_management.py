
import csv
import datetime
from pathlib import Path
from typing import Any, Callable, List
from sqlalchemy import Engine, MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session as ORM_Session



def get_db_engine(db_url:str, db_name:str, database_type:str):
    return create_engine(db_url+f"/{db_name}", echo=True)

def get_metadata_of_engine(db_engine:Engine)->MetaData:
    return MetaData(bind=db_engine, reflect=True)

def get_db_tables_as_dict(db_engine:Engine):
    return get_metadata_of_engine(db_engine).tables

def load_csv_file(csv_filepath:str,funcs: List[Callable[[str],Any]], delimeter:str=",")->None:

    if not Path(csv_filepath).exists():
        raise FileNotFoundError("Incorrect filepath")
    
    with open(csv_filepath) as file:
        next(file)
        csv_reader = csv.reader(file, delimiter=delimeter)
        for row in csv_reader:
            for func in funcs:
                func(row)

def create_db_session(database_url:str,db_name:str, database_type:str)-> ORM_Session:
    Session = sessionmaker(bind=get_db_engine(database_url, db_name,  database_type))
    return Session()

def parse_datetime_string(date_str:str)->datetime.datetime:
    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')