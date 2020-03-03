class MissingLabelError(KeyError):
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass

# program... user enter wrong username
def login():
    raise IncorrectUsernameError
try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect. Have you forgotten it? ")
except IncorrectPasswordError:
    print("Your password was wrong. Have you forgotten it? ")
