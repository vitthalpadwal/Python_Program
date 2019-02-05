"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  or  digits.
■ Each digit is in the range of  to . ( and ).
■  letters can be lower case. ( and  are also valid digits).

Examples

Valid Hex Color Codes
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}
Input Format

The first line contains , the number of code lines.
The next  lines contains CSS Codes.

Constraints



Output Format

Output the color codes with '#' symbols on separate lines.

Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
Explanation

#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Note: There are no comments ( // or /* */) in CSS Code.
"""

import re
'''
n = int(input())
lines = input() 

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #ABC, #fff);
}
#Cab

'''
#for line in lines:
'''
r = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', re.IGNORECASE|re.MULTILINE)
out = r.search(lines)
print(out)

for i in range(n):
    inside_brackets = re.findall(r'\{.*?\}', lines, flags=re.DOTALL)
    for attributes in inside_brackets:
        code = re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', attributes)
        for i in code:
            print(i)
'''
n = int(input())
for t in range(n):
    s = input()
    match_result = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',s)
    for i in match_result:
        if i != '':
            print(i)