"""
The square-ten tree decomposition of an array is defined as follows:

The lowest () level of the square-ten tree consists of single array elements in their natural order.
The  level (starting from ) of the square-ten tree consists of subsequent array subsegments of length  in their natural order. Thus, the  level contains subsegments of length , the  level contains subsegments of length , the  level contains subsegments of length , etc.
In other words, every  level (for every ) of square-ten tree consists of array subsegments indexed as:

Level  consists of array subsegments indexed as .
The image below depicts the bottom-left corner (i.e., the first  array elements) of the table representing a square-ten tree. The levels are numbered from bottom to top:

4x128 square-ten tree table

Task
Given the borders of array subsegment , find its decomposition into a minimal number of nodes of a square-ten tree. In other words, you must find a subsegment sequence  such as  for every , , , where every  belongs to any of the square-ten tree levels and  is minimal amongst all such variants.

Input Format

The first line contains a single integer denoting .
The second line contains a single integer denoting .

Constraints

The numbers in input do not contain leading zeroes.
Output Format

As soon as array indices are too large, you should find a sequence of  square-ten tree level numbers, , meaning that subsegment  belongs to the  level of the square-ten tree.

Print this sequence in the following compressed format:

On the first line, print the value of  (i.e., the compressed sequence block count).
For each of the  subsequent lines, print  space-separated integers,  and  (, ), meaning that the number appears consequently  times in sequence . Blocks should be listed in the order they appear in the sequence. In other words,  should be equal to ,  should be equal to , etc.
Thus  must be true and  must be true for every . All numbers should be printed without leading zeroes.

Sample Input 0

1
10
Sample Output 0

1
1 1
Explanation 0

Segment  belongs to level  of the square-ten tree.
"""

# work with big numbers as strings
L = input()
R = input()

# look for largest possible level
d = len(R)
level = 0
n = 1
tree = [n] # chunk dimension
while d >= n + 1:
    tree.append(n)
    level += 1
    n = 2 ** level

# go backwards from largest level
def breakdown(N, k):
    if k == 0:
        return [int(N)]

    div = tree[k]
    chunks = breakdown(N[-div:], k - 1)
    chunks.append(N[:-div].lstrip('0') or 0)
    return chunks

divL = breakdown(L, level)
divR = breakdown(R, level)
seq = []

# add up to higher level for L
carry = 0
for k, n in enumerate(map(int, divL)):
    if k == 0:
        carry = -1 # add up lowest number

    n += carry
    carry = 0

    if k < level:
        if n > 0:
            n = 10 ** tree[k] - n
            carry = 1
        elif n < 0:
            n = 1 # if lowest was zero

        seq.append((k, n))

# sum up last level of L and R
if n != 0:
    divR[k] = int(divR[k]) - n
    while divR[-1] == 0:
        del divR[-1]
        n = seq.pop()[1]
        if n != 0:
            divR[-1] = int(divR[-1]) + n

# add R in reversed order
seq.extend(reversed(list(enumerate(divR))))

# exclude empty levels
seq = [s for s in seq if s[1] != 0]
print(len(seq))

for s in seq:
    print(*s)