import sys
import argparse

from logo import Logo
from generator.engine import ContentType
from generator.engine import Generator


class Args:
    LONG_HELP = "--help"
    SHORT_HELP = "-h"
    LONG_OPERATION = "operation"
    SHORT_OPERATION = "o"
    LONG_VERSION = "--version"
    SHORT_VERSION = "-v"
    LONG_LENGTH = "--length"
    SHORT_LENGTH = "-l"
    LONG_CONTENT = "--content"
    SHORT_CONTENT = "-c"
    LONG_PASSWORD = "--password"
    SHORT_PASSWORD = "-p"

    MESSAGE_HELP_OPERATION = "use to classify operation type \
[generate | verify]"
    MESSAGE_HELP_CONTENT = "-c | --content [alpha, num, special]"
    MESSAGE_HELP_LENGTH = "-l | --lenght [value] to \
specify the password length"

    MESSAGE_USAGE = f"""
{Logo()}
PassVar is a simple python program used for verifying
and generating passwords based on OWASP standards.

use operation to classify whether to generate or validate
a password

>>> operation generate
1. Password Generation
PassVar can generate a pseudo random password
with the provided attributes such as the length
and content to be generated according to OWASP standard.

use --length | -l to specify the length
use --content | -c to classify what the kind of characters \
password should contain
The following are allowed content
[alpha, num, special]

>>> operation verify
2. Password Verification
The other main use case of passvar is to
verify a password based on some criterias.
Some of the criterias are the following

#### dude here this will be gone
A. Length
Length determines whether the password
is strong or weak according to OWASP protocol.

B. Content
Content determines whether the the password
has a common used characters according to
OWASP and IBM standard.
"""


"""
!, @, #, $, %, ^, &, or *.
special characters allowed according to IBM standard
"""


def main():
    parser = argparse.ArgumentParser(prog="passvar", usage=Args.MESSAGE_USAGE)

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
                        )

    parser.add_argument(Args.LONG_PASSWORD, Args.SHORT_PASSWORD,
                        default=None,
                        required=False,
                        )

    parser.add_argument(Args.LONG_OPERATION,
                        help=Args.MESSAGE_HELP_OPERATION,
                        nargs=1,
                        type=str,
                        default=None
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
                        print("heeeeey here: ", val)
        else:
            content = ContentType().__iter__()
        print(Generator(length, content).json_result())
        Generator(length, content).to_file("./pass.txt")
    elif args.operation[0] == "verify":
        password = args.password
    else:
        sys.stdout.write("%s\n" % (Args.MESSAGE_USAGE))


if __name__ == "__main__":
    main()
