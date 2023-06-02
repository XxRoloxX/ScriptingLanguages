import datetime
import sys
from typing import Any, List,Optional
from create_database import DATABASE_TYPE, DATABASE_URL,DEFAULT_DB_NAME
import create_database
from db_management import create_db_session, get_db_engine, load_csv_file, parse_datetime_string
from models import Rentals, Stations
from cmd_arguments_utils import get_line_arguments
from sqlalchemy.sql import func


class DataBaseHandler():
    
    def __init__(self):
        self.session=None
    def open_db_session(self,database_name=DEFAULT_DB_NAME,database_url=DATABASE_URL, database_type=DATABASE_TYPE):
        self.session = create_db_session(database_url,database_name,database_type)

    def close_db_session(self):
        self.session.close()

    def validate_session(self):
        if not self.session:
            raise Exception("Session is not set yet")
        
    def execute_sql(self,sql):
        result = self.session.execute(sql)
        self.session.commit()
        return result


class RentalsReader(DataBaseHandler):

    def get_average_time_of_travel_from_starting_station(self,station_name)->float:
        self.validate_session()
        selected_station = self.session.query(func.avg(Rentals.duration).label('average_duration'))\
            .filter(Rentals.rental_station_id==Stations.station_id)\
            .filter(Stations.station_name==station_name)\
            .all()
        return selected_station[0][0]
    
    def get_average_time_of_travel_from_ending_station(self,station_name)->float:
        self.validate_session()
        selected_station = self.session.query(func.avg(Rentals.duration).label('average_duration'))\
            .filter(Rentals.return_station_id==Stations.station_id)\
            .filter(Stations.station_name==station_name)\
            .first()
        return selected_station[0]
    
    def get_number_of_unique_bikes_at_station(self,station_name)->float:
        self.validate_session()
        selected_station = self.session.query(Rentals.bike_number)\
            .filter(Rentals.return_station_id==Stations.station_id)\
            .filter(Stations.station_name==station_name)\
            .group_by(Rentals.bike_number)\
            .count()
        return selected_station
    
    def get_longest_rental_from_station(self,station_name)->datetime.datetime:
        self.validate_session()
        last_rental = self.session.query(func.max(Rentals.duration).label('longest_rental'))\
            .filter(Rentals.rental_station_id==Stations.station_id)\
            .filter(Stations.station_name==station_name)\
            .first()
        return last_rental[0]

    
    def get_list_of_stations(self, filter=""):
        self.validate_session()
        return self.session.query(Stations).filter(Stations.station_name.contains(filter))

        
        


class RentalsLoader(DataBaseHandler):


    def load_rentals_row(self,attr:List[str]):

        self.validate_session()

        parsed_row = self._parse_rentals_csv_row_to_dict(attr)
        rental_station = self._create_if_absent_and_return_station(parsed_row["rental_station"])
        return_station = self._create_if_absent_and_return_station(parsed_row["return_station"])

        if not self._find_rental(parsed_row["rental_id"]):

            rental = Rentals(rental_id = parsed_row["rental_id"],
                             bike_number = parsed_row["bike_number"],
                             start_time = parse_datetime_string(parsed_row["start_time"]),
                             end_time = parse_datetime_string(parsed_row["end_time"]),
                             duration = parsed_row["duration"],
                             rental_station_id = rental_station.station_id,
                             return_station_id = return_station.station_id)
            
            self.session.add(rental)
            self.session.commit()

    def _find_station(self,station_name:str)->Optional[Stations]:
        self.validate_session()
        return self.session.query(Stations).filter_by(station_name=station_name).first()
    
    def _find_rental(self,rental_id:str)->Optional[Rentals]:
        self.validate_session()
        return self.session.query(Rentals).filter_by(rental_id=rental_id).first()
    
    def _create_if_absent_and_return_station(self,station_name:str):
        self.validate_session()
        current_station = self._find_station(station_name)
        if not current_station:
            self.session.add(Stations(station_name=station_name))
            self.session.commit()
            current_station = self._find_station(station_name)
        return current_station
    

    def _parse_rentals_csv_row_to_dict(self, attr: List[str]):
        return {
                "rental_id": attr[0],
                "bike_number": attr[1],
                "start_time": attr[2],
                "end_time": attr[3],
                "rental_station": attr[4],
                "return_station": attr[5],
                "duration": attr[6]
                }
    
def main():
    [csv_filepath, db_name] = get_line_arguments(2)
    rentals_loader = RentalsLoader()
    rentals_loader.open_db_session(db_name)
    load_csv_file(csv_filepath,[rentals_loader.load_rentals_row])
    rentals_loader.close_db_session()



if __name__ =="__main__":
    main()