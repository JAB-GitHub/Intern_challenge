import difflib

class CommonPasswordChecker:
    """
    This class should contain the code to check
    if the password is common, using an external dataset
    """
    #use a lib to verify if is simillar 
    #If is simillar: true
    #else: False
    # Write your code here
    def __init__(self, password: str) -> None:
        self.pwd = password.password

    def check_common(self):

        fp= open(r'common_words.txt', 'r')

        if fp == None:
            raise Exception("Problem to open common_words.txt")                

        common_w = fp.read()
        words = common_w.split()
        
        fp.close()            
        matches = difflib.get_close_matches(self.pwd, words)
        if matches:
            return True
        else:
            return False
        