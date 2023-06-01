
import sys
sys.path.append('../../')
#from utils import test_append_type
from SSHLogJournal import SSHLogJournal
from typing import *
from Zadanie1 import *
from logUtils import *
import pytest




@pytest.mark.parametrize("log, expected_type", [
    ("Dec 17 14:51:06 LabSZ sshd[4604]: Failed password for invalid user admin from 183.96.119.62 port 50426 ssh2", SSHLogFailedPassword),
    ("Jan  4 19:38:32 LabSZ sshd[5769]: Accepted password for curi from 137.189.241.248 port 21926 ssh2",  SSHLogAcceptedPassword ), 
    ("Jan  5 12:27:51 LabSZ sshd[18912]: PAM service(sshd) ignoring max retries; 6 > 3",  SSHLogOther),
    ("Jan  4 23:21:41 LabSZ sshd[8445]: error: Received disconnect from 103.207.36.21: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]",  SSHLogError),
    ("Jan  5 08:47:52 LabSZ sshd[16564]: message repeated 5 times: [ Failed password for root from 59.63.188.30 port 2932 ssh2]", SSHLogFailedPassword),
    ("Jan  5 08:47:52 LabSZ sshd[16564]: Disconnecting: Too many authentication failures for root [preauth]", SSHLogOther),
    ("Jan  5 08:47:48 LabSZ sshd[16566]: Accepted password for jmzhu from 112.96.33.40 port 48253 ssh2", SSHLogAcceptedPassword),
    ("Jan  5 08:48:46 LabSZ sshd[16692]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=59.63.188.30  user=root", SSHLogOther)
])
def test_append_type(log:str, expected_type:SSHLogEntry):
    journal = SSHLogJournal()
    journal.append(log)
    assert isinstance(journal.get(0), expected_type)


@pytest.mark.parametrize("log, expected_type", [
    ("Jan  4 19:38:32 LabSZ sshd[5769]: Accepted password for curi from 137.189.241.248 port 21926 ssh2",  SSHLogAcceptedPassword ), 
    ("Jan  5 08:47:48 LabSZ sshd[16566]: Accepted password for jmzhu from 112.96.33.40 port 48253 ssh2", SSHLogAcceptedPassword),
])
def test_accepted_password_type_append(log:str, expected_type:SSHLogAcceptedPassword):
    journal = SSHLogJournal()
    journal.append(log)
    assert isinstance(journal.get(0), expected_type)


@pytest.mark.parametrize("log, expected_type", [
    ("Dec 17 14:51:06 LabSZ sshd[4604]: Failed password for invalid user admin from 183.96.119.62 port 50426 ssh2", SSHLogFailedPassword),
    ("Jan  5 08:47:52 LabSZ sshd[16564]: message repeated 5 times: [ Failed password for root from 59.63.188.30 port 2932 ssh2]", SSHLogFailedPassword),
])
def test_failed_password_type_append(log:str, expected_type:SSHLogFailedPassword):
    journal = SSHLogJournal()
    journal.append(log)
    assert isinstance(journal.get(0), expected_type)


@pytest.mark.parametrize("log, expected_type", [
    ("Jan  4 23:21:41 LabSZ sshd[8445]: error: Received disconnect from 103.207.36.21: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]",  SSHLogError),
    ("Dec 21 14:51:41 LabSZ sshd[19519]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]",SSHLogError)
])
def test_error_log_type_append(log:str, expected_type:SSHLogError):
    journal = SSHLogJournal()
    journal.append(log)
    assert isinstance(journal.get(0), expected_type)


@pytest.mark.parametrize("log, expected_type", [
    ("Jan  5 12:27:51 LabSZ sshd[18912]: PAM service(sshd) ignoring max retries; 6 > 3",  SSHLogOther),
    ("Jan  5 08:47:52 LabSZ sshd[16564]: Disconnecting: Too many authentication failures for root [preauth]", SSHLogOther),
])
def test_other_log_type_append(log:str, expected_type:SSHLogOther):
    journal = SSHLogJournal()
    journal.append(log)
    assert isinstance(journal.get(0), expected_type)
