import { useContext, useState } from "react";
import "./LogsWindow.css";
import React from "react";
import { SingleLog, LogListContainer } from "./LogWindow.style";
import { FocusedLogIndexContext } from "../FocusedLogIndexContext";

type Logs = {
  logList: string[];
  handleLogList: (arg: string[]) => void
  focusedLogIndex: number
  focusedLogRef: React.MutableRefObject<HTMLButtonElement | null>
};

export const LogsWindow = (props: Logs) => {
  const [clickedLog, setClickedLog] = useState<string>("");
  const { focusedLogIndex, setFocusedLogIndex } = useContext(
    FocusedLogIndexContext
  );

  return (
    <>
      <LogListContainer>
        {props.logList
          ? props.logList.map((log, index) => (
              <SingleLog
                focusedLog={index == focusedLogIndex}
                ref={index==focusedLogIndex?props.focusedLogRef:undefined}
                onClick={() => {
                  setFocusedLogIndex(index);
                }}
              >
                {log}
              </SingleLog>
            ))
          : ""}
      </LogListContainer>
    </>
  );
};
