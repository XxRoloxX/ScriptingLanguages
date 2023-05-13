import { useState } from "react"
import "./LogsWindow.css"
import React from "react"
import { SingleLog, LogListContainer } from "./LogWindow.style"


type Logs = {
    logList:string[],
    handleLogList: (arg:string[])=>void
}

export const LogsWindow = (props:Logs)=>{

    const [clickedLog, setClickedLog] = useState<string>("")

    return (
        <>
            
            <LogListContainer>
                <div>Clicked Log: {clickedLog}</div>
                {props.logList?props.logList.map((log)=><SingleLog onClick={()=>{setClickedLog(log)}}>{log}</SingleLog>):""}
            </LogListContainer>
            
                
        </>
    )

}