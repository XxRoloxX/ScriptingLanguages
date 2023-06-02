from typing import List
from textual.widgets import Label,ListView
from textual.reactive import reactive
from models import Stations



class StationsList(ListView):
    stations: List["Stations"] = reactive([Stations(station_id="1", station_name="One")])

    def render(self)->str:
        return str(self.stations[0])

class DatabaseLabel(Label):
    database_path: str = reactive("")
    def render(self)->str:
        return "Select database: "+str(self.database_path)

class StatisticsLabel(Label):
    station_name: str =reactive(None)
    def render(self)->str:
        return str(self.station_name)