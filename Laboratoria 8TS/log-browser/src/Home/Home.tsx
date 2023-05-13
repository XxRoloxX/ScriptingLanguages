import React, { ChangeEvent, MouseEventHandler, useRef } from "react";
import { useEffect, useState } from "react";
import "./Home.css";
import { LogsWindow } from "./LogsWindow/LogsWindow";
import { eel } from "../eel";
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
  FilterButton,
  ChangeIndexButtonsWrapper,
  ChangeIndexButton
} from "./Home.style";
import { FocusedLogIndexContext } from "./FocusedLogIndexContext";
import { LogDetails } from "./LogDetails/LogDetails";
import { Placeholder } from "./Placeholder/Placeholder";

export const Home = () => {

  const [logList, setLogList] = useState<string[]>([]);
  const [logPath, setLogPath] = useState("");
  const [filterStartDate, setFilterStartDate] = useState("");
  const [filterEndDate, setFilterEndDate] = useState("");
  const [focusedLogIndex, setFocusedLogIndex] = useState(1)

  const focusedLogRef = useRef<HTMLButtonElement | null>(null)


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
  const handleIncrementIndex = () => {
    if(focusedLogIndex<logList.length){
      setFocusedLogIndex((index)=>index+1)
      executeScroll()
    }
    
  }

  const handleDecrementIndex = () => {
    if(focusedLogIndex>0){
      setFocusedLogIndex((index)=>index-1)
      executeScroll()
    }
    
  }


  const retrieveLogs = () => {
    eel.getLogJournalFromFile(logPath)(setLogList);
  };

  const executeScroll = () => {
    if(focusedLogRef.current){
      focusedLogRef.current.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }
    
  }

  useEffect(() => {
    console.log(eel);
  }, []);

  useEffect(() => {
    console.log("State has changed");
    console.log(!logList)
  }, [logList]);

  return (
    <>
      <SearchWrapper>
        <FileSearchBar placeholder="Type filepath" onChange={handleLogPath} />
        <FileSearchButton onClick={retrieveLogs}>Open</FileSearchButton>
      </SearchWrapper>

      {logList.length>0?<><FocusedLogIndexContext.Provider value={{focusedLogIndex,setFocusedLogIndex}}>

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
              <FilterInputWrapper>
                <FilterButton onClick={handleFilterSubmit}>Filter</FilterButton>
              </FilterInputWrapper>
              
              
            </FiltersWrapper>
            <LogsWindow logList={logList} handleLogList={setLogList} focusedLogIndex={focusedLogIndex} focusedLogRef={focusedLogRef}/>
          </ListAndFilterContainer>

          <LogDetails />

          
        </LogMasterDetailContainer>

      </FocusedLogIndexContext.Provider>

      <ChangeIndexButtonsWrapper>
          <ChangeIndexButton onClick={handleDecrementIndex} isActive={focusedLogIndex<=0}>Previous</ChangeIndexButton>
          <ChangeIndexButton onClick={handleIncrementIndex} isActive={focusedLogIndex>=logList.length}>Next</ChangeIndexButton>
      </ChangeIndexButtonsWrapper></>: <Placeholder/>}

      
    </>
  );
};
