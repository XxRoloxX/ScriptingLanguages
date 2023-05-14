import styled from "styled-components";
import React, { MouseEventHandler } from 'react'

export const MaterialUISpan = (props: {type:string}) => {
    return <span className="material-symbols-outlined" style={{display:"flex", alignItems:"center", justifyContent:"center"}}>{props.type}  </span>
}


export const FileSearchBar = styled("input")`
    text-align: left;
    border-radius: 1rem;
    padding: 0.3rem;
    color: grey;
    padding-left:1rem;
`

export const SearchWrapper = styled("div")`
    width:90vw;
    margin:auto;
    display:grid;
    grid-template-columns: 7fr 1fr;
   
`

export const FilterDateInput = styled("input")`
    width: 5rem;
    text-align: center;
    margin: auto;
`
export const FilterInputWrapper = styled("div")`
    display: flex;
    flex-direction: row;
    margin:1rem;
`
export const FilterInputLabel = styled("div")`
    text-align: center;
    color:white;
    font-weight: 200;
    margin-right: 1rem;
`

export const FiltersWrapper = styled("div")`
    height:5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
`

export const ListAndFilterContainer = styled("div")`
    display: flex;
    flex-direction: column;
    height: 70vh;
  
`

export const LogMasterDetailContainer = styled("div")`
    display:flex;
    flex-direction: row;
    color:white;
    margin: 0.5rem;
`
export const FilterButton = styled("button")`
    border-radius: 0.7rem;
    text-align: center;
    width: 5rem;
    height:1.5rem;
    background-color: transparent;
    border-width: 0;
    color:white;
    &:hover{
        transform: scale(1.1);
    }
`

const StyledFileSearchButton = styled("button")`
    border-radius: 0.5rem;
    color:white;
    background-color: transparent;
    margin:auto;
    border-width:0;
    text-align: left;
    &:hover{
        transform: scale(1.1);
    }
`


export const MaterialUIFileSearchButton = (props: {onClick: MouseEventHandler<HTMLButtonElement>})=>{

    return <StyledFileSearchButton onClick={props.onClick}>
        <MaterialUISpan type={"search"}/>
    </StyledFileSearchButton>
}


export const MaterialUIFilterButton = (props:{onClick: MouseEventHandler<HTMLButtonElement>})=>{
    return <FilterButton onClick={props.onClick}>
        <MaterialUISpan type="filter_alt_off"/>
    </FilterButton>
}

type IndexButton = {
    isActive: boolean
}


export const ChangeIndexButton = styled("button")<IndexButton>`
    background-color:transparent;
    color:${(props)=>props.isActive?"grey":"white"};
    border-width: 0;
    &:hover{
        transform: scale(1.1);
    }
`
export const MaterialUIForwardIndexButton = (props: {isActive:boolean, onClick:MouseEventHandler<HTMLButtonElement>})=>{
    return <ChangeIndexButton isActive={props.isActive} onClick={props.onClick}>
        <MaterialUISpan type={"arrow_forward_ios"}/>
    </ChangeIndexButton>
}

export const MaterialUIBackwardIndexButton = (props: {isActive:boolean, onClick:MouseEventHandler<HTMLButtonElement>})=>{
    return <ChangeIndexButton isActive={props.isActive} onClick={props.onClick}>
        <MaterialUISpan type={"arrow_back_ios"}/>
    </ChangeIndexButton>
}

export const ChangeIndexButtonsWrapper = styled(FilterInputWrapper)`
    justify-content: space-around;
`
export const ErrorLabel = styled("label")`
    color:red;
    text-align: center;
    display: flex;
    justify-content: center;
    text-align: center;

`