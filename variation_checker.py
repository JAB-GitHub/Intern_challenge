class VariationChecker:
    """
    This class should contain the code to check if there's a minimum of:
     - One numerical digit
     - One special character
     - One uppercase letter
     - One lowercase letter
     If not, the password is invalid
    """

    # Write your code here
    #similar to invalid

    def __init__(self, password: str) -> None:
        self.pwd = password.password
        self.low = 0
        self.upp = 0
        self.dig = 0
        self.spe = 0

    def verfy_char(self):
        special_chars = "!$%&\()*+-/?@_"
        Lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
        Uppercase_chars ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #Digits = "0123456789" pwd only have valid character

        for char in self.pwd:
            if (char in special_chars):
                self.spe += 1
            elif (char in Lowercase_chars):
                self.low += 1
            elif (char in Uppercase_chars): 
                self.upp += 1
            else:
                self.dig += 1
            

        #Can use swtch case
        if (self.low == 0):
            raise Exception("Invalid password. It must have at least one lowercase letter")
        if (self.upp == 0):
            raise Exception("Invalid password. It must have at least one uppercase letter")
        if (self.dig == 0):
            raise Exception("Invalid password. It must have at least one numerical digit") 
        if (self.spe == 0):
            raise Exception("Invalid password. It must have at least one special character")
