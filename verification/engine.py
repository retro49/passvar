import re
import json


class PasswordStrength:
    AMBIGUOUS = -1
    WEAK = 0
    STRONG = 1
    VSTRONG = 2


class PasswordLength:
    SHORT = 0
    LONG = 1


class Varification:
    __PASSWORD_VSTRONG = r"^(?=.*[a-zA-Z0-9_])(?=.*[@#\$%\^!&*()\[\]\{\}\:\;\<\>\+\=\-])[a-zA-Z0-9_@#\$%\^!&*()\[\]\{\}\:\;\<\>\+\=\-]+$"
    __PASSWORD_STRONG = r"[A-Za-z0-9]+"
    __PASSWORD_WEAK = r"[A-Za-z]+"

    strength: int = 0
    length: int = 0

    def __init__(self, password: str):
        self.password = password
        if len(self.password) < 8:
            self.length = PasswordLength.SHORT
        else:
            self.length = PasswordLength.LONG

        if re.fullmatch(self.__PASSWORD_VSTRONG, self.password):
            self.strength = PasswordStrength.VSTRONG
        elif re.fullmatch(self.__PASSWORD_STRONG, self.password):
            self.strength = PasswordStrength.STRONG
        elif re.fullmatch(self.__PASSWORD_WEAK, password):
            self.strength = PasswordStrength.WEAK
        else:
            self.strength = PasswordStrength.AMBIGUOUS

    def verify(self):
        return {
                "length": self.length,
                "strength": self.strength,
                }

    def json_result(self):
        return json.dumps({
            "length": self.length,
            "strength": self.strength,
            })
