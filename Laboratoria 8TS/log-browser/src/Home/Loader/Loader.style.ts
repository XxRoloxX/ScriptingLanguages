import { keyframes } from "styled-components";
import styled    from "styled-components";
import { activeLogColor } from "../LogsWindow/LogWindow.style";


const SpinningAnimation = keyframes`
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
`

export const LoaderRingAnimation = styled("div")`
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin:auto;
  z-index: 10;
  border: 5px solid transparent;
  border-top: 5px solid white; 
  border-radius: 50%;
  background-color: transparent;
  width: 80px;
  height: 80px;
  opacity: 0.5;
  animation: ${SpinningAnimation} 2s ease-in-out infinite;
`
