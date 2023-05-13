import { useState } from "react"
import "./LogsWindow.css"
import React from "react"

export const LogsWindow = (props)=>{

    const [clickedLog, setClickedLog] = useState(null)

    return (
        <>
            <div className="log-container">
            <div>Clicked Log: {clickedLog}</div>
                {props.logList.map((log)=><button className="log-instance" onClick={()=>{setClickedLog(log)}}>{log}</button>)}
            </div>
        </>
    )

}