import json
import sys

from random import randint
from random import shuffle
from .util import ContentType
from .util import CharacterSet
from .util import ContentClassifier
from .varification import Varification


class Generator:
    __password_content: str = ""
    """ length of the password by default """

    content = []
    length = 16

    def __init__(self, length, content):
        sys.setrecursionlimit(0x1000000)
        self.length = int(length)
        self.content = content
        if len(self.content) == 0:
            self.content = content = [
                    ContentType.ALPHA,
                    ContentType.NUMERIC,
                    ContentType.SPECIAL
                    ]

        charset = CharacterSet().get_set()
        for c in self.content:
            if c in charset:
                self.__password_content += charset[c]
        self.__password_content = list(self.__password_content)

    """ generates a passowrd according to the given property """

    def generate(self) -> str:
        result = ""
        shuffle(self.__password_content)
        for i in range(self.length):
            random_pos = randint(0, len(self.__password_content) - 1)
            result += self.__password_content[random_pos]

        genc = Varification(result).varify()['strength']
        givc = ContentClassifier(self.content).get_strength()
        while genc != givc:
            result = Generator(self.length, self.content).generate()

        return result

    """ returns the generated text in the form of json """

    def json_result(self):
        return json.dumps({
            "length": self.length,
            "content": self.content,
            "password": self.generate()
            })

    """ writes the file to the given stream """

    def to_file(self, path):
        with open(path, "w+") as file:
            file.write(self.generate())
