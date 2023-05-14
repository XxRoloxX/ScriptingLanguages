import React, { MouseEventHandler } from "react";
import styled from "styled-components";
import { MaterialUISpan } from "../Home.style";

export const PlaceholderContainer = styled("div")`
    margin: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`

export const JokeWrapper = styled("div")`
    height: 50vh;
    font-size: 1.5rem;
    text-align: center;
    color:white;
    display:flex;
    justify-content: center;
    align-items: center;
    margin:3rem;
    opacity: 0.5;

`
export const NewJokeButton = styled("button")`
    border-radius: 0.5rem;
    text-align: center;
    background-color: transparent;
    color:white;
    border-width: 0;
    opacity: 0.5;
    margin-bottom: 10rem;
    &:hover{
        transform: scale(1.5);
    }
`


export const MaterialUINewJokeButton = (props: {onClick: MouseEventHandler<HTMLButtonElement>})=>{
    return <NewJokeButton onClick={props.onClick}>
        <MaterialUISpan type={"sync"} size={"4rem"}/>
    </NewJokeButton>
}