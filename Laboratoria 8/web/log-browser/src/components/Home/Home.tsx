import React from "react"
import { useEffect, useState } from "react"
import "./Home.css"
import {LogsWindow} from "../LogsWindow/LogsWindow.js"
import { eel } from "../../eel.js";

export const Home = () => {

    const [logList, setLogList] = useState("text")
    //<input type="file" placeholder="Type filepath" onChange={(event)=>{setLogList(eel.getLogJournalFromFile(event.files[0]))}}/>

    useEffect(()=>{
            console.log(eel)
            eel.printHello("Hello World")(function(value){
                console.log(value+"adasds")
                console.log("Cokolwiek")
            })   
    },[])
    useEffect(()=>{
        console.log("State has changed")
    },[logList])

    return(
        <>
            <button onClick={()=>{eel.printHello("clicked"+(Date.now()))(setLogList)}}> </button>
            <div>{eel.printHello("Hello World")(function(value){
                console.log(value)
                console.log("Cokolwiek")
            })}
            </div>
            <div className="main-container">
                <div>{logList}k</div>
                <LogsWindow logList={["log1", "log2", "log3"]} handleLogList={setLogList}/>
                <div>Second Hello</div>
            </div>
        </>
    )
        

}