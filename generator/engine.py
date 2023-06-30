# Copyright (c) 2023 G.C Naol Dereje
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json

from random import randint


class ContentType:
    ALPHA = "alpha"
    NUMERIC = "numeric"
    SPECIAL = "special"

    def __iter__(self):
        return [self.ALPHA, self.NUMERIC, self.SPECIAL]


class CharacterSet:
    ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
    NUMERIC = "0123456789"
    SPECIAL = "!@#$%^&*()_-+={}[];:<>"

    def __dict__(self):
        return {
                "alpha": self.ALPHA,
                "numeric": self.NUMERIC,
                "special": self.SPECIAL,
                }


class Generator:
    __password_content = ""
    """ length of the password by default """

    content = []
    length = 16

    def __init__(self, length, content):
        self.length = int(length)
        self.content = content
        if len(self.content) == 0:
            self.content = content = [
                    ContentType.ALPHA,
                    ContentType.NUMERIC,
                    ContentType.SPECIAL
                    ]

        for c in self.content:
            if c in CharacterSet().__dict__():
                self.__password_content += CharacterSet().__dict__()[c]

    """ generates a passowrd according to the given property """

    def generate(self) -> str:
        result = ""
        for i in range(self.length):
            random_pos = randint(0, len(self.__password_content)-1)
            result += self.__password_content[random_pos]
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
