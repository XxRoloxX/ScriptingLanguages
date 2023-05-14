import React, { useEffect, useReducer, useState } from "react"
import { JokeWrapper, MaterialUINewJokeButton, NewJokeButton, PlaceholderContainer } from "./Placeholder.styles"
import { eel } from "../../eel"



export const Placeholder = () => {

    const [joke, setJoke] = useState("")


    const handleNewJoke = ()=>{
        eel.getJoke(Math.floor(Math.random()*100))(setJoke)
        console.log(joke)
    }

    useEffect(()=>{
        handleNewJoke()
    },[])


    return <PlaceholderContainer>
        <JokeWrapper>{joke}</JokeWrapper>
        <MaterialUINewJokeButton onClick={handleNewJoke}/>
    </PlaceholderContainer>




}