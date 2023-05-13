import React from "react"

type IndexContextType = {
    focusedLogIndex:number,
    setFocusedLogIndex: React.Dispatch<React.SetStateAction<number>>
}


export const FocusedLogIndexContext = React.createContext({
    focusedLogIndex: 0,
    setFocusedLogIndex: ()=>{}
} as IndexContextType)