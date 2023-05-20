import sys
sys.path.append('../../')
from typing import *
from Zadanie1 import get_log_entry
from logUtils import *
import pytest



@pytest.mark.parametrize("log, expected_time", [
    ("Dec 10 07:07:38 LabSZ sshd[24206]: Invalid user test9 from 52.80.34.196", SimpleDate(11,10,7,7,38)),
    ("Dec 17 14:51:06 LabSZ sshd[4604]: Failed password for invalid user admin from 183.96.119.62 port 50426 ssh2", SimpleDate(11,17,14,51,6)),
    ("Jan  2 03:58:39 LabSZ sshd[22856]: Disconnecting: Too many authentication failures for root [preauth]", SimpleDate(0,2,3,58,39)),
    ("Jan  5 12:27:51 LabSZ sshd[18912]: PAM service(sshd) ignoring max retries; 6 > 3", SimpleDate(0,5,12,27,51)),
    ("Jan  7 17:22:01 LabSZ sshd[30291]: pam_unix(sshd:session): session opened for user jmzhu by (uid=0)", SimpleDate(0,7,17,22,1))
])

def test_time_extraction(log:str, expected_time:'SimpleDate'):
    assert simpleDateComparator(get_log_entry(log).date, expected_time)==0


@pytest.mark.parametrize("log, expected_ip", [
    ("Dec 10 07:07:38 LabSZ sshd[24206]: Invalid user test9 from 52.80.34.196","52.80.34.196"),
    ("Dec 17 14:51:06 LabSZ sshd[4604]: Failed password for invalid user admin from 183.96.119.62 port 50426 ssh2", "183.96.119.62"),
    ("Jan  2 03:58:39 LabSZ sshd[22856]: Disconnecting: Too many authentication failures for root [preauth]", None),
    ("Jan  5 12:27:51 LabSZ sshd[18912]: PAM service(sshd) ignoring max retries; 6 > 3", None),
    ("Jan  7 17:22:01 LabSZ sshd[30291]: pam_unix(sshd:session): session opened for user jmzhu by (uid=0)", None),
    ("Dec 17 14:51:06 LabSZ sshd[4604]: Failed password for invalid user admin from 666.999.222.111 port 50426 ssh2", None)
])
def test_ip_extraction(log:str, expected_ip:Union[str,None]):
    assert get_log_entry(log).ip == expected_ip