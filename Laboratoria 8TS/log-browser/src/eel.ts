type PythonObject = Window & {
    printHello: (arg:string)=>(fun:(arg:string)=>any) => any
    set_host: (arg:string)=>void
    getLogJournalFromFile: (arg:string)=>(fun:(arg:string[])=>any) => any
    filterJournalByDates: (startDate:string, endDate:string)=>(fun:(logs:string[])=>any)=>any
}


export const eel = window["eel" as any] as PythonObject;
eel.set_host("ws://localhost:8888")
