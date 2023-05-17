class LengthChecker:
    """
    This class should contain the code to check the password length.
    If lower than 8, the password is invalid
    """

    def __init__(self, password: str, min_length: int = 8) -> None:
        self.pwd = password.password
        self.min_length = min_length
        pass

    def check_length(self) -> None:
        length = len(self.pwd)
        if length < self.min_length:
            raise Exception("Password is too small. Must have 8 characters")
        return length
