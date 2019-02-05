"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
Input Format

The first line of input contains an integer .
The next  lines contain credit card numbers.

Constraints


Output Format

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

Sample Input

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
Sample Output

Valid
Valid
Invalid
Valid
Invalid
Invalid
Explanation

4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234--8912-3456 : Invalid, because the card number is not divided into equal groups of .
4123356789123456 : Valid
51-67-8912-3456 : Invalid, consecutive digits  is repeating  times.
5123456789123456 : Invalid, because space '  ' and - are used as separators.
"""

import re


def credit_card_validation(card_no):
    credit_hiphen = card_no.replace('-', '')
    valid = True
    length_16 = bool(re.match(r'^[4-6]\d{15}$', card_no))
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', card_no))
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)', credit_hiphen))

    if length_16 == True or length_19 == True:
        if consecutive == True:
            valid = False
    else:
        valid = False

    if valid == True:
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        card_no = input().strip()
        credit_card_validation(card_no)


"""
PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def is_valid_card_number(sequence):
    Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6 
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-". 
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.
    

    match = re.match(PATTERN,sequence)

    if match == None:
        return False

    for group in match.groups:
        if group[0] * 4 == group:
            return False
    return True
"""