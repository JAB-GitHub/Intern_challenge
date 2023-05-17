
from common_password_checker import CommonPasswordChecker


class ScoreCalculation:
    """
    This class should contain the code to calculate the score.
    Passwords with score lower than 16 are invalid
    
    """

    def __init__(self, password: str) -> None:
        self.password = password
        self.common_checker = CommonPasswordChecker(password).check_common()
        self.score = 0

    def check_score_characters(self):
        # Write your code here
        print("Checking for common words")
        
        if self.common_checker == True:
            self.score -= 8

        print("Sum of valuo of each char") #Can be better implementation

        special_chars = "!$%&\()*+-/?@_"
        Lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
        Uppercase_chars ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Digits = "0123456789" 

        for char in self.password.password:
            if (char in special_chars):
                self.score += 3
            elif (char in Lowercase_chars):
                self.score += 1
            elif (char in Uppercase_chars): 
                self.score += 1
            else:
                self.score += 1
        
        print("Verify Consecutive characters")
        
        ant_char = "ç" #char impossible

        #Find possicion in the vector and verify if is consecutive
        #to avoid look a non possible possicion, necessary verify if the previous char it is the last of the list

        for char in self.password.password:
            if ant_char == "ç":
                ant_char = char
                continue

            if (char in special_chars) and (ant_char in special_chars) and (ant_char != "_"): 
                i=0
                while(ant_char != special_chars[i]): #Look the posicion of ant_char in the vector
                    i +=1
                if (char == special_chars[i+1]):
                    self.score -= 2

            elif (char in Lowercase_chars) and (ant_char in Lowercase_chars) and (ant_char != "z"):
                i=0
                while(ant_char != Lowercase_chars[i]): #Look the posicion of ant_char in the vector
                    i +=1
                if (char == Lowercase_chars[i+1]):
                    self.score -= 2

            elif (char in Uppercase_chars) and (ant_char in Uppercase_chars) and (ant_char != "Z"): 
                i=0
                while(ant_char != Uppercase_chars[i]): #Look the posicion of ant_char in the vector
                    i +=1
                if (char == Uppercase_chars[i+1]):
                    self.score -= 2
            elif (char in Digits) and (ant_char in Digits) and (ant_char != "9"):
                i=0
                while(ant_char != Digits[i]): #Look the posicion of ant_char in the vector
                    i +=1
                if (char == Digits[i+1]):
                    self.score -= 2

            ant_char = char



        return self.score