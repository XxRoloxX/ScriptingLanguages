import { keyframes } from "styled-components";
import styled    from "styled-components";
import { activeLogColor } from "../LogsWindow/LogWindow.style";


const SpinningAnimation = keyframes`
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
`

export const LoaderRingAnimation = styled("div")`
  position: fixed;
  top: 20vh;
  left: 45vw;
  z-index: 10;
  border: 5px solid transparent; /* Light grey */
  border-top: 5px solid white; /* Blue */
  border-radius: 50%;
  background-color: transparent;
  width: 80px;
  height: 80px;
  opacity: 0.5;
  animation: ${SpinningAnimation} 2s ease-in-out infinite;
`
