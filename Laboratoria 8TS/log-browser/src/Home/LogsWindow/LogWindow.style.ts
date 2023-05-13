import styled from "styled-components";

export const SingleLog = styled("button")`
    font-size: 0.5rem;
    text-align: center;
    background-color: #132045;
    box-shadow: none;
    border-color:transparent;
    color:white;
    padding: 0.2rem;
    border-radius: 0.5rem;
    margin: 0.2rem;
    &:hover {
    //background-image: linear-gradient(purple, blue)
    background-color: #1d8541;
  }
`

export const LogListContainer = styled("div")`
    background-color: transparent;
    display:flex;
    flex-direction: column;
    margin: 1rem;
    overflow: scroll;
    ::-webkit-scrollbar {
    width: 0px;
    background: transparent; /* make scrollbar transparent */
}
`


