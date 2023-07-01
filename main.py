import sys
import argparse

from logo import Logo
from engine.generator import Generator
from engine.varification import Varification
from engine.util import ContentType


class Args:
    LONG_HELP = "--help"
    LONG_OPERATION = "operation"
    LONG_LENGTH = "--length"
    LONG_CONTENT = "--content"
    LONG_VERSION = "--version"
    LONG_PASSWORD = "--password"
    LONG_FILE = "--file"
    LONG_JSON = "--json"
    LONG_AMOUNT = "--amount"

    SHORT_HELP = "-h"
    SHORT_VERSION = "-v"
    SHORT_LENGTH = "-l"
    SHORT_CONTENT = "-c"
    SHORT_PASSWORD = "-p"
    SHORT_FILE = "-f"
    SHORT_JSON = "-j"
    SHORT_AMOUNT = "-a"

    MESSAGE_HELP_OPERATION = "use to classify operation type \
[generate | verify]"
    MESSAGE_HELP_CONTENT = "-c | --content [alpha, num, special]"
    MESSAGE_HELP_LENGTH = "-l | --lenght [value] to \
specify the password length"
    MESSAGE_HELP_JSON = "-j | --json to specify output as a json"
    MESSAGE_HELP_FILE = "-f | --file [file name] to specify \
output destination to a file"
    MESSAGE_HELP_PASSWORD = "-p | --password to specify \
password for varification"
    MESSAGE_HELP_VERSION = "-v | --version show version"
    MESSAGE_HELP_AMOUNT = "-a | --amount to specify how much password \
to generate"
    MESSAGE_USAGE = f"""
{Logo()}
PassVar is a simple python program used for verifying
and generating passwords based on OWASP standards.

use operation to classify whether to generate or validate
a password

1. Password Generation
PassVar can generate a pseudo random password
with the provided attributes such as the length
and content to be generated according to OWASP standard.

use --length | -l to specify the length
use --content | -c to classify what the kind of characters \
password should contain
The following are allowed content
[alpha, num, special]

2. Password Verification
The other main use case of passvar is to
verify a password based on some criterias.
Some of the criterias are the following
"""


class GenerateHandler:
    @staticmethod
    def file_handler(content, length, file, amount=1, is_json=False):
        generator = Generator(length, content)
        stream = ""
        if is_json:
            for i in range(amount):
                stream += generator.json_result() + chr(0x0a)
        else:
            for i in range(amount):
                stream += generator.generate() + chr(0x0a)
        with open(file, "+w") as ouput:
            ouput.write(stream)

    @staticmethod
    def stdout_handler(content, length, amount=1, is_json=False):
        generator = Generator(length, content)
        stream = ""
        if is_json:
            for i in range(amount):
                stream += generator.json_result() + chr(0xa)
        else:
            for i in range(amount):
                stream += generator.generate() + chr(0xa)

        print(f"{stream}")


def main():
    parser = argparse.ArgumentParser(prog="passvar", usage=Args.MESSAGE_USAGE)

    parser.add_argument(Args.LONG_OPERATION,
                        help=Args.MESSAGE_HELP_OPERATION,
                        nargs=1,
                        type=str,
                        default=None
                        )

    parser.add_argument(Args.LONG_VERSION, Args.SHORT_VERSION,
                        action='version',
                        version='%(prog)s 1.0',
                        )

    parser.add_argument(Args.LONG_CONTENT, Args.SHORT_CONTENT,
                        action="extend",
                        nargs="+",
                        help=Args.MESSAGE_HELP_CONTENT,
                        type=str,
                        )

    parser.add_argument(Args.LONG_LENGTH, Args.SHORT_LENGTH,
                        default=16,
                        required=False,
                        help=Args.MESSAGE_HELP_LENGTH
                        )

    parser.add_argument(Args.LONG_FILE, Args.SHORT_FILE,
                        default=None,
                        required=False,
                        help=Args.MESSAGE_HELP_FILE,
                        )

    parser.add_argument(Args.LONG_JSON, Args.SHORT_JSON,
                        action="store_true",
                        help=Args.MESSAGE_HELP_JSON,
                        )

    parser.add_argument(Args.LONG_PASSWORD, Args.SHORT_PASSWORD,
                        default=None,
                        required=False,
                        help=Args.MESSAGE_HELP_PASSWORD,
                        )

    parser.add_argument(Args.LONG_AMOUNT, Args.SHORT_AMOUNT,
                        required=False,
                        default=1,
                        help=Args.MESSAGE_HELP_AMOUNT,
                        )

    args = parser.parse_args(sys.argv[1:])

    if args.operation[0].lower() == "generate":
        length = args.length
        content = args.content
        if content is not None:
            for val in content:
                ctype = ContentType().__iter__()
                if ctype is not None:
                    if val not in ContentType().__iter__():
                        raise ValueError("unknown value")
        else:
            content = ContentType().__iter__()

        print(Logo())
        if args.file is not None:
            GenerateHandler.file_handler(content,
                                         length,
                                         args.file,
                                         int(args.amount),
                                         args.json
                                         )
        else:
            GenerateHandler.stdout_handler(content,
                                           length,
                                           int(args.amount),
                                           args.json
                                           )

    elif args.operation[0] == "verify":
        password = args.password
        if password != "" or password is not None:
            var = Varification(password).varify()
            pass_length = var['length']
            pass_strength = var['strength']
            print(f"length: {pass_length}")
            print(f"strength: {pass_strength}")
    else:
        sys.stdout.write("%s\n" % (Args.MESSAGE_USAGE))


if __name__ == "__main__":
    main()
