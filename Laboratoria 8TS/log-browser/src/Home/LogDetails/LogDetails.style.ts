import styled from "styled-components";
import gradient from "../../assets/wms-dev-original-cubism-gradient.png"

export const LogDetailsContainer = styled("div")`
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 0.5rem;
    margin: 10vh;
    height: 55vh;
`
export const SingleLogDetail = styled("div")`
    height: 2rem;
    margin: 0.5rem;
    padding: 0.5rem;
    font-size: 1rem;
    text-align: center;
    background: url(${gradient});
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 0.5rem;
`
export const SingleLogLabelWrapper = styled("div")`
    margin: auto;
    display: grid;
    grid-template-columns: 9rem 10rem;
    border-color: purple;
    border-width: 20px;
`
export const LogDetailsLabel = styled("div")`
    font-size: 1.5rem;
    text-align: left;
    display:flex;
    flex-direction: column;
    justify-content: center;
    margin-left:1rem;
`