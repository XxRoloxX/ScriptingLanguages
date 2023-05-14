import React, { useContext, useEffect, useState } from "react";
import { eel } from "../../eel";
import { FocusedLogIndexContext } from "../FocusedLogIndexContext";
import { LogDetailsContainer, LogDetailsLabel, SingleLogDetail, SingleLogLabelWrapper } from "./LogDetails.style";


type LogDetailsResult = {
  date: string;
  ip: string;
  host: string;
  [index: string]: string;
};

export const LogDetails = () => {
  const [logDetails, setLogDetails] = useState<LogDetailsResult>({
    date: "",
    ip: "",
    host: "",
  });

  const { focusedLogIndex } = useContext(FocusedLogIndexContext);

  useEffect(() => {
    eel.getLogDetails(focusedLogIndex)((el) => {
      setLogDetails(el);
    });
  }, [focusedLogIndex]);

  {
    logDetails ? Object.values(logDetails).map((el) => <div>el</div>) : "";
  }

  return (
    <>
      <LogDetailsContainer>
        {logDetails
          ? Object.keys(logDetails).filter((el)=>(logDetails[el])).map((el: string) => (
            <SingleLogLabelWrapper>
                <LogDetailsLabel>{el.toUpperCase()}</LogDetailsLabel>
                <SingleLogDetail>{logDetails[el]}</SingleLogDetail>
              </SingleLogLabelWrapper>
            ))
          : ""}
      </LogDetailsContainer>
    </>
  );
};
