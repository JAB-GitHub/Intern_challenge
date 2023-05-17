class InvalidChecker:
    """ "
    This class should contain the code to check
    if the password contains any invalid characters
    """

    def __init__(self, password: str) -> None:

        #List of permit characters, peparete by type 
        special_chars = "!$%&\()*+-/?@_"
        Lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
        Uppercase_chars ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Digits = "0123456789"

        for char in password.password:
            if (char not in special_chars) and (char not in Lowercase_chars) and (char not in Uppercase_chars) and (char not in Digits):
                raise Exception("Invalid password: Contains an invalid character")
