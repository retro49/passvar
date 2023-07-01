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

    def get_set(self):
        return {
                "alpha": self.ALPHA,
                "numeric": self.NUMERIC,
                "special": self.SPECIAL,
                }


class ContentClassifier:
    content: list = None
    __VSTRONG_CONTENT = [
            ContentType.ALPHA,
            ContentType.NUMERIC,
            ContentType.SPECIAL
            ]

    __STRONG_CONTENT = [
            ContentType.ALPHA,
            ContentType.NUMERIC
            ]

    __WEAK_CONTENT = [
            ContentType.ALPHA
            ]

    def __init__(self, content: list):
        self.content = content
        self.content.sort()

    def get_strength(self):
        if self.content == self.__VSTRONG_CONTENT:
            return PasswordStrength.VSTRONG
        elif self.content == self.__STRONG_CONTENT:
            return PasswordStrength.STRONG
        elif self.content == self.__WEAK_CONTENT:
            return PasswordStrength.WEAK
        else:
            return PasswordStrength.AMBIGUOUS


class PasswordStrength:
    AMBIGUOUS = -1
    WEAK = 0
    STRONG = 1
    VSTRONG = 2


class PasswordLength:
    SHORT = 0
    LONG = 1
