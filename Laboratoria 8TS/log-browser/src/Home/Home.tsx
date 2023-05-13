import React, { ChangeEvent } from "react";
import { useEffect, useState } from "react";
import "./Home.css";
import { LogsWindow } from "../LogsWindow/LogsWindow";
import { eel } from "../../eel";
import {
  FileSearchBar,
  SearchWrapper,
  FileSearchButton,
  FilterDateInput,
  FiltersWrapper,
  ListAndFilterContainer,
  LogMasterDetailContainer,
  FilterInputWrapper,
  FilterInputLabel,
  FilterButton
} from "./Home.style";

export const Home = () => {
  const [logList, setLogList] = useState<string[]>([]);
  const [logPath, setLogPath] = useState("");
  const [filterStartDate, setFilterStartDate] = useState("");
  const [filterEndDate, setFilterEndDate] = useState("");
  const [focusedLogIndex, setFocusedLogIndex] = useState(-1)

  const handleLogPath = (event: ChangeEvent<HTMLInputElement>) => {
    setLogPath(event.target.value);
  };

  const handleFilterStartTime = (event: ChangeEvent<HTMLInputElement>)=> {
    setFilterStartDate(event.target.value)
  }
  const handleFilterEndTime = (event: ChangeEvent<HTMLInputElement>)=> {
    setFilterEndDate(event.target.value)
  }
  const handleFilterSubmit = () =>{

    console.log(filterStartDate+"  "+filterEndDate)
    eel.filterJournalByDates(filterStartDate, filterEndDate)(setLogList)
  }


  const retrieveLogs = () => {
    eel.getLogJournalFromFile(logPath)(setLogList);
  };

  useEffect(() => {
    console.log(eel);
  }, []);

  useEffect(() => {
    console.log("State has changed");
  }, [logList]);

  return (
    <>
      <SearchWrapper>
        <FileSearchBar placeholder="Type filepath" onChange={handleLogPath} />
        <FileSearchButton onClick={retrieveLogs}>Open</FileSearchButton>
      </SearchWrapper>
      <LogMasterDetailContainer>
        <ListAndFilterContainer>
          <FiltersWrapper>

            <FilterInputWrapper>
                <FilterInputLabel>Start date</FilterInputLabel>
                <FilterDateInput type="date" onChange={handleFilterStartTime}/>
            </FilterInputWrapper>
            <FilterInputWrapper>
                <FilterInputLabel>End date</FilterInputLabel>
                <FilterDateInput type="date" onChange={handleFilterEndTime}/>
            </FilterInputWrapper>
            <FilterButton onClick={handleFilterSubmit}>Filter</FilterButton>
            
          </FiltersWrapper>
          <LogsWindow logList={logList} handleLogList={setLogList} />
        </ListAndFilterContainer>
      </LogMasterDetailContainer>
    </>
  );
};
