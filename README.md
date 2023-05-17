# Password Validator

This tool will analyse the provided password, checking if it's valid and giving a score

## Instructions

Dear candidate,

Thank you for taking the time to participate in this technical challenge. We would like to inform you that the code provided for this challenge has been modified to remove certain portions and include intentional bugs. This has been done to test your problem-solving skills and ability to debug code.

To get started, please read the following instructions carefully:

1. Download the code provided for the technical challenge.
2. Open the code in your preferred development environment.
3. Please note that the code has been modified to include intentional bugs. These bugs may cause errors or unexpected behavior when running the code. Your task is to identify and fix these bugs.
4. In addition to the bugs, some portions of the code have been removed. You may need to write your own code to replace these missing portions. Please make sure that your solution follows the requirements outlined in the challenge prompt.
5. Once you have fixed all the bugs and completed the missing portions, please test your solution thoroughly to ensure that it is working correctly.

## Definitions

- Lowercase characters: `abcdefghijklmnopqrstuvwxyz`
- Uppercase characters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Digits: `0123456789`
- Special characters: `!$%&\()*+-/?@_`

## Score calculation

- Alphanumerical characters (+1 point per character)
- Consecutive characters (-2 points per character)
- Special characters (+3 points per character)
- Common words (-8 points penalty, independent of the number of common words found)

Only passwords with $score \geq 16$ are valid

## Expected behavior

- This code must be able to run in Python 3.11

- The code should receive the password by the argument section, printing the score if it's a valid password and raising an Exception if it isn't.

## Examples

### Valid

The following input:

```bash
python password_validator.py --password "98Eyq98rhwq98+"
```

should return the following output:

```text
Valid password
Score: 16
```

### Invalid

```bash
python password_validator.py --password "98Eyq98rhwq98"
```

should return the following exception:

```text
Exception: Invalid password. It must have at least one special character
```
