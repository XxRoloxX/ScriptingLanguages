
from typing import List
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import  Header, Footer, Input,DirectoryTree
from textual.containers import Horizontal, Vertical, ScrollableContainer, Center
from textual.widgets import DataTable
from textual.reactive import reactive
from custom_widgets import DatabaseLabel, StatisticsLabel
from models import Stations
from load_data import RentalsReader



class RentalsApp(App):

    CSS_PATH = "styles.css"

    database_path:str = reactive("")
    stations: List["Stations"] = reactive([Stations(station_id="1", station_name="One")])
    station_selected:str = reactive("")
    database_reader: RentalsReader = reactive(RentalsReader())


    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal(
                Vertical(
                    DatabaseLabel(),
                    DirectoryTree(".", id="directory_tree"),
                    id="directory_tree_container"
                   ),
                Vertical(
                    Input(id="input_stations_filter", placeholder="Select stations"),
                    Center(
                        ScrollableContainer(
                            DataTable(id="stations_table")     
                            ),
                        ),
                    id="stations_list_container"
                    
                    )
                    ,
                Vertical(
                    Center(
                        StatisticsLabel()
                        ),
                    DataTable(id="station_stats_table"),
                    id="station_stats_container"
                )
            ),
            
        )
        yield Footer()
    
    def on_mount(self)->None:
       self._set_data_tables()



    @on(DirectoryTree.FileSelected,"#directory_tree")
    def handle_directory_tree_file_selected(self, message:DirectoryTree.FileSelected):
        self.database_path = message.path

        try:
            self.database_reader.open_db_session(self.database_path)
            self.stations = self.database_reader.get_list_of_stations() 
            self._render_stations()
            self.database_reader.close_db_session()
        except Exception:
            self.database_path = "Not a database"

        self.query_one(DatabaseLabel).database_path = self.database_path


    @on(DataTable.CellSelected,"#stations_table")
    def handle_data_table_row_selected(self, message:DataTable.CellSelected):
       
        stations_table:DataTable = self.query_one("#stations_table")
        row = stations_table.get_row_at(message.coordinate.row)
        self.station_selected = row[1]
        average_time_when_start_station = self.database_reader.get_average_time_of_travel_from_starting_station(self.station_selected)
        average_time_when_end_station = self.database_reader.get_average_time_of_travel_from_ending_station(self.station_selected)
        number_of_unique_bikes = self.database_reader.get_number_of_unique_bikes_at_station(self.station_selected)
        longest_rental = self.database_reader.get_longest_rental_from_station(self.station_selected)

        self._render_statistics(average_time_when_start_station,
                                average_time_when_end_station,
                                number_of_unique_bikes,
                                longest_rental)
       

    @on(Input.Submitted, "#input_stations_filter")
    def handle_on_input_submitted(self, message:Input.Submitted):
        self.database_reader.open_db_session(self.database_path)
        self.stations = self.database_reader.get_list_of_stations(message.value)
        self._render_stations()
        self.database_reader.close_db_session()

    def _render_stations(self):
        table = self.query_one("#stations_table")
        table.clear()
        new_stations = [station.to_tupe() for station in self.stations]
        table.add_rows(new_stations)
    
    def _render_statistics(self,
                            average_time_when_start_station, 
                            average_time_when_end_station,
                            number_of_unique_bikes,
                            longest_rental):
         
         stats_table:DataTable = self.query_one("#station_stats_table")
         self.query_one(StatisticsLabel).station_name = self.station_selected
         stats_table.clear()
         stats_table.add_rows([("Average Time When Start Station", average_time_when_start_station)])
         stats_table.add_rows([("Average Time When End Station", average_time_when_end_station)])
         stats_table.add_rows([("Nuber of unique bikes", number_of_unique_bikes)])
         stats_table.add_rows([("Longest rental", longest_rental)])

    def _set_data_tables(self):
        stations_table = self.query_one("#stations_table")
        stations_table.add_columns("ID", "Name")

        statistics_table = self.query_one("#station_stats_table")
        statistics_table.add_columns("Statistic", "Value")

        stations_table.zebra_stripes =True
        statistics_table.zebra_stripes =True

        


if __name__ == "__main__":
    app = RentalsApp()
    app.run()