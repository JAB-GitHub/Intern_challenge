import argparse
from length_checker import LengthChecker
from invalid_checker import InvalidChecker
from score_calculation import ScoreCalculation
from variation_checker import VariationChecker



def validate_password(pwd):
    print("Checking for invalid characters")
    InvalidChecker(pwd)

    print("Checking password length")
    LengthChecker(pwd).check_length()

    #Before caculate score, verify if pwd conten minimum necessary
    print("Checking characters")
    VariationChecker(pwd).verfy_char()

    score = ScoreCalculation(pwd).check_score_characters()

    print("----")
    if (score >= 16):
        print(f"Valid password")
        print(f"Score: {score}")
    else:
        print("Weak password, try another password")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", dest="password",type=str, help="Receve the password to verify")
    pwd = parser.parse_args()
    validate_password(pwd)
