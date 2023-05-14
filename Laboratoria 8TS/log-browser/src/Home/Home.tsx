import React, { ChangeEvent, MouseEventHandler, useRef } from "react";
import { useEffect, useState } from "react";
import "./Home.css";
import { LogsWindow } from "./LogsWindow/LogsWindow";
import { eel } from "../eel";
import {
  FileSearchBar,
  SearchWrapper,
  FilterDateInput,
  FiltersWrapper,
  ListAndFilterContainer,
  LogMasterDetailContainer,
  FilterInputWrapper,
  FilterInputLabel,
  ChangeIndexButtonsWrapper,
  ErrorLabel,
  MaterialUIFilterButton,
  MaterialUIForwardIndexButton,
  MaterialUIBackwardIndexButton,
  MaterialUIFileSearchButton
} from "./Home.style";
import { FocusedLogIndexContext } from "./FocusedLogIndexContext";
import { LogDetails } from "./LogDetails/LogDetails";
import { Placeholder } from "./Placeholder/Placeholder";
import { LoaderRingAnimation } from "./Loader/Loader.style";

const PAGINATION_DEFAULT_SIZE=15
const PAGINATION_TRIGGER_INDEX = 5

export const Home = () => {

  const [logList, setLogList] = useState<string[]>([]);
  const [areLogsLoaded, setAreLogsLoaded] = useState(false);
  const [incorrectLogPath, setIncorrectLogPath] = useState(false);
  const [logPath, setLogPath] = useState("");
  const [filterStartDate, setFilterStartDate] = useState("");
  const [filterEndDate, setFilterEndDate] = useState("");
  const [focusedLogIndex, setFocusedLogIndex] = useState(1);
  const [lastLogRetrievedIndex, setLastLogRetrievedIndex] = useState(0);
  const [isWaitingForData, setIsWaitingForData] = useState(false)

  const focusedLogRef = useRef<HTMLButtonElement | null>(null);

  const handleLogPath = (event: ChangeEvent<HTMLInputElement>) => {
    setLogPath(event.target.value);
  };

  const handleFilterStartTime = (event: ChangeEvent<HTMLInputElement>) => {
    setFilterStartDate(event.target.value);
  };
  const handleFilterEndTime = (event: ChangeEvent<HTMLInputElement>) => {
    setFilterEndDate(event.target.value);
  };

  const handleSetLogList = (logList: string[]) => {
    if (logList !== null) {
      setLogList(logList);
      setAreLogsLoaded(true);
      setIncorrectLogPath(false);
      setFocusedLogIndex(0);
    } else {
      setAreLogsLoaded(false);
      setIncorrectLogPath(true);
    }

    setIsWaitingForData(false)

  };

  const handleAppendLogList = (logList:string[])=>{

    setLogList((logs)=>{ const newLogs = logs.concat(logList); setLastLogRetrievedIndex(newLogs.length-1) ;return newLogs})
  }

  const handleFilterSubmit = () => {
    setIsWaitingForData(true)
    eel.filterJournalByDates(filterStartDate, filterEndDate)(handleSetLogList);
  };
  const handleIncrementIndex = () => {
    if (focusedLogIndex < logList.length - 1) {
      setFocusedLogIndex((index) => index + 1);
      executeScroll();
    }
  };

  const handleDecrementIndex = () => {
    if (focusedLogIndex > 0) {
      setFocusedLogIndex((index) => index - 1);
      executeScroll();
    }
  };

  const retrieveLogs = () => {
    setIsWaitingForData(true)
    eel.getLogJournalFromFile(logPath)(handleSetLogList);
    setFilterStartDate("");
    setFilterEndDate("");
    setFocusedLogIndex(0)
    setLastLogRetrievedIndex(0)
  };

  const executeScroll = () => {
    if (focusedLogRef.current) {
      focusedLogRef.current.scrollIntoView({
        behavior: "smooth",
        block: "center",
      });
    }
  };


  useEffect(()=>{
    if(focusedLogIndex>=logList.length- PAGINATION_TRIGGER_INDEX){
      eel.getNLogsFromFile(lastLogRetrievedIndex+1,PAGINATION_DEFAULT_SIZE)(handleAppendLogList)
      setLastLogRetrievedIndex(lastLogRetrievedIndex+PAGINATION_DEFAULT_SIZE)
    }
  },[focusedLogIndex])


  return (
    <>

      <SearchWrapper>
        <FileSearchBar placeholder="Type filepath" onChange={handleLogPath} />
        <MaterialUIFileSearchButton onClick={retrieveLogs} />
      </SearchWrapper>
      {isWaitingForData?<LoaderRingAnimation/>:""}
      {incorrectLogPath ? <ErrorLabel>Incorrect filepath </ErrorLabel> : ""}
    
      {areLogsLoaded ? (
        <>
          <FocusedLogIndexContext.Provider
            value={{ focusedLogIndex, setFocusedLogIndex }}
          >
            <LogMasterDetailContainer>
              <ListAndFilterContainer>
                <FiltersWrapper>
                  <FilterInputWrapper>
                    <FilterInputLabel>From</FilterInputLabel>
                    <FilterDateInput
                      type="date"
                      onChange={handleFilterStartTime}
                      value={filterStartDate}
                    />
                  </FilterInputWrapper>
                  <FilterInputWrapper>
                    <FilterInputLabel>To</FilterInputLabel>
                    <FilterDateInput
                      type="date"
                      onChange={handleFilterEndTime}
                      value={filterEndDate}
                    />
                    <MaterialUIFilterButton onClick={handleFilterSubmit} />
                  </FilterInputWrapper>
                </FiltersWrapper>
                <LogsWindow
                  logList={logList}
                  handleLogList={setLogList}
                  focusedLogIndex={focusedLogIndex}
                  focusedLogRef={focusedLogRef}
                />
              </ListAndFilterContainer>

              <LogDetails />
            </LogMasterDetailContainer>
          </FocusedLogIndexContext.Provider>

          <ChangeIndexButtonsWrapper>
            <MaterialUIBackwardIndexButton
              onClick={handleDecrementIndex}
              isActive={focusedLogIndex <= 0}
            />
            <MaterialUIForwardIndexButton
              onClick={handleIncrementIndex}
              isActive={focusedLogIndex >= logList.length - 1}
            />
          </ChangeIndexButtonsWrapper>
        </>
      ) : (
        <Placeholder />
      )}
    </>
  );
};
