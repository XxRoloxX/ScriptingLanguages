type EelObject = Window & {
    printHello: (arg:string)=>(fun:(arg:string)=>any) => any
    set_host: (arg:string)=>void
    getLogJournalFromFile: (arg:string)=>(fun:(arg:string[])=>any) => any
    filterJournalByDates: (startDate:string, endDate:string)=>(fun:(logs:string[])=>any)=>any
    getLogDetails: (logIndex: number) => (fun: (arg:any)=>any)=>any
    getJoke: (jokeIndex:number)=>(fun: (joke:string)=>any)=>any
    getNLogsFromFile:(startIndex: number, numberOfLogsToRetrieve:number)=>(fun:(arg:string[])=>any)=>any
}


export const eel = window["eel" as any] as EelObject;
export const EEL_WEBSOCKET_ADDRESS = "ws://localhost:8888";

eel.set_host(EEL_WEBSOCKET_ADDRESS)
