import sys
from typing import Optional
def get_line_arguments(required_length)->Optional[str]: 
    return None if len(sys.argv)!=required_length+1 else sys.argv[1:]