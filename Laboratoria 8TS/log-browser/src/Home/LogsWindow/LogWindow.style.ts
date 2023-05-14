import styled from "styled-components";
import gradient from "../../assets/wms-dev-original-cubism-gradient.png"

export const activeLogColor =  "#22317a"
export const unActiveLogColor ="#132045"


export const SingleLog = styled("button")<{focusedLog:boolean}>`
    font-size: 0.5rem;
    text-align: center;
    background-color: ${p => (p.focusedLog ? activeLogColor : unActiveLogColor)};
    box-shadow: none;
    border-color:transparent;
    color:white;
    padding: 0.2rem;
    border-radius: 0.5rem;
    margin: 0.2rem;
    margin-right:0.5rem;
    margin-left:0.5rem;
    width: 25rem;
    &:hover {
    transform: scale(1.03);
    background-color: ${activeLogColor} ;
  }
`

export const LogListContainer = styled("div")`
    background-color: transparent;
    display:flex;
    flex-direction: column;
    margin: 1rem;
    margin-top: 2rem;
    overflow: scroll;
    ::-webkit-scrollbar {
    width: 0px;
    background: transparent; /* make scrollbar transparent */
}
`


