import re
import json
from .util import PasswordLength
from .util import PasswordStrength


class Varification:
    __PASSWORD_VSTRONG = r"^(?=.*[a-zA-Z0-9_])(?=.*[@#\$%\^!&*()\[\]\{\}\:\;\<\>\+\=\-])[a-zA-Z0-9_@#\$%\^!&*()\[\]\{\}\:\;\<\>\+\=\-]+$"
    __PASSWORD_STRONG = r"^[A-Za-z0-9]+$"
    __PASSWORD_WEAK = r"^[A-Za-z]+$"

    strength: int = 0
    length: int = 0

    def __init__(self, password: str):
        self.password = password
        if len(self.password) < 8:
            self.length = PasswordLength.SHORT
        else:
            self.length = PasswordLength.LONG

        if re.fullmatch(self.__PASSWORD_WEAK, password):
            self.strength = PasswordStrength.WEAK
        elif re.fullmatch(self.__PASSWORD_VSTRONG, self.password):
            self.strength = PasswordStrength.VSTRONG
        elif re.fullmatch(self.__PASSWORD_STRONG, self.password):
            self.strength = PasswordStrength.STRONG
        else:
            self.strength = PasswordStrength.AMBIGUOUS

    def varify(self):
        return {
                "length": self.length,
                "strength": self.strength,
                }

    def json_result(self):
        return json.dumps({
            "length": self.length,
            "strength": self.strength,
            })
