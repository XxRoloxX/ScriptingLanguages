import styled from "styled-components";

export const FileSearchBar = styled("input")`
    text-align: left;
    width:70%;
    margin-right: 3rem;
    margin-top: 0.5rem;
`

export const FileSearchButton = styled("button")`
    border-radius: 0.5rem;
    text-align: center;
    width: 5rem;
    &:hover{
        transform: scale(1.1);
    }
`

export const SearchWrapper = styled("div")`
    width:90vw;
    margin:auto;
    justify-items: center;
    justify-content: center;
    text-align: center;
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
    &:hover{
        transform: scale(1.1);
    }
`

type IndexButton = {
    isActive: boolean
}


export const ChangeIndexButton = styled(FilterButton)<IndexButton>`
    background-color: ${(props)=>props.isActive?"red":"white"};
    &:hover{
        transform: scale(1.1);
    }
`

export const ChangeIndexButtonsWrapper = styled(FilterInputWrapper)`
    justify-content: space-around;
`