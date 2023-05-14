import re
from logUtils import *


class SSHUser:

    def __init__(self):
        self._username = ""
        self._lastLoginDate = None

    def __init__(self, newUsername, newLastLoginDate):
        self._username = newUsername
        self._lastLoginDate = newLastLoginDate

    @property
    def username(self):
        return self._username

    @property
    def lastLoginDate(self):
        return self._lastLoginDate

    @property
    def lastLoginDate(self, newDate: SimpleDate):
        self._lastLoginDate = newDate

    def __str__(self):
        return f"Username: {self._username}, last Login: {self._lastLoginDate}"

    def validate(self):
        if self._username == None:
            return False

        matchedObject = re.match(CORRECT_USER_PATTERN, self._username)

        if matchedObject == None:
            return False
        else:
            return True
