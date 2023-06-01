
from typing import List
from textual import on
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Label, Button, Header, Footer,Static, Input,DirectoryTree, TextLog, Tree, ListView, ListItem
from textual.containers import Horizontal, Vertical, ScrollableContainer, Center
from textual.widgets import DataTable
from textual.reactive import reactive
from textual.widget import Widget
from models import Stations
from load_data import RentalsReader
from sqlite3 import DatabaseError


class StationsList(ListView):
    stations: List["Stations"] = reactive([Stations(station_id="1", station_name="One")])

    def render(self)->str:
        return str(self.stations[0])

class DatabaseLabel(Label):
    database_path: str = reactive("")
    def render(self)->str:
        return "Select database: "+str(self.database_path)


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
                    Center(
                        Label("Select station")
                        ),
                    Center(ScrollableContainer(
                        DataTable(id="stations_table"),
                        id="stations_list_container"
                    ),))
                    ,
                Vertical(
                    Center(Label("Statistics")),
                    DataTable(id="station_stats_table"),
                    Horizontal(
                        Label("Średni czas: ")
                    ),
                    id="station_stats_container"
                )
            ),
            
        )
        yield Footer()
    
    def on_mount(self)->None:
        self.query_one("#stations_table").add_columns("ID", "Name"),
        self.query_one("#station_stats_table").add_columns("Statistic", "Value")
        #self.query_one(DataTable).add_columns("ID", "Name")
    @on(DirectoryTree.FileSelected,"#directory_tree")
    def handle_directory_tree_file_selected(self, message:DirectoryTree.FileSelected):
        self.database_path = message.path
        # try:
        #     self.database_reader.open_db_session(self.database_path)
        #     self.stations = self.database_reader.get_list_of_stations()  
        #     self.query_one(ListView).clear()
        #     new_stations = [ListItem(Label(str(station), classes="station_label")) for station in self.stations]
        #     for station in new_stations:
        #         self.query_one(ListView).append(station)
        # except Exception:
        #     self.database_path = "Not a database"

        try:
            self.database_reader.open_db_session(self.database_path)
            self.stations = self.database_reader.get_list_of_stations() 
            table = self.query_one("#stations_table")
            #table.clear()
            new_stations = [station.to_tupe() for station in self.stations]
            table.add_rows(new_stations)
        except Exception:
            self.database_path = "Not a database"

        self.query_one(DatabaseLabel).database_path = self.database_path
    @on(DataTable.CellSelected,"#stations_table")
    def handle_data_table_row_selected(self, message:DataTable.CellSelected):
        stats_table:DataTable = self.query_one("#station_stats_table")
        stations_table:DataTable = self.query_one("#stations_table")
        stats_table.clear()
        row = stations_table.get_row_at(message.coordinate.row)
        average_time = self.database_reader.get_average_time_of_arrival_from_starting_station(row[1])
        stats_table.add_rows([("Average Time", average_time)])




        


if __name__ == "__main__":
    app = RentalsApp()
    app.run()