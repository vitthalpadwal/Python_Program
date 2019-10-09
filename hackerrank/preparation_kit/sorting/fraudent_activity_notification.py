"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, find and print the number of times the client will receive a notification over all  days.

For example,  and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is  and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. (Wikipedia)

Function Description

Complete the function activityNotifications in the editor below. It must return an integer representing the number of client notifications.

activityNotifications has the following parameter(s):

expenditure: an array of integers representing daily expenditures
d: an integer, the lookback days for median spending
Input Format

The first line contains two space-separated integers  and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending.
The second line contains  space-separated non-negative integers where each integer  denotes .

Constraints

Output Format

Print an integer denoting the total number of times the client receives a notification over a period of  days.

Sample Input 0

9 5
2 3 4 2 3 6 8 4 5
Sample Output 0

2
Explanation 0

We must determine the total number of  the client receives over a period of  days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data: .

On the sixth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the seventh day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the eighth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which does not trigger a notification because : .

On the ninth day, the bank has  days of prior transaction data, , and a transaction median of  dollars. The client spends  dollars, which does not trigger a notification because : .

Sample Input 1

5 4
1 2 3 4 4
Sample Output 1

0
There are  days of data required so the first day a notice might go out is day . Our trailing expenditures are  with a median of  The client spends  which is less than  so no notification is sent.

Python 3



"""

'''
import math
import os
import random
import re
import sys
from statistics import median

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    new_list1 = expenditure[:d]
    new_list2 = expenditure[d:]
    count =0
    for i in new_list2:
        new_list1.sort()
        mid = median(new_list1)
        if i >= mid*2:
            count = count + 1
        new_list1 = new_list1[1:]
        new_list1.append(i)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
'''

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


class RunningMedian(object):

    def __init__(self, maxLen):
        self.d = [0] * 201
        self.queue = deque()
        self.maxLen = maxLen

    def add(self, v: int) -> None:
        self.queue.append(v)
        self.d[v] += 1
        if len(self.queue) > self.maxLen:
            val = self.queue.popleft()
            self.d[val] -= 1

    def median(self) -> int:
        a = int(self.maxLen / 2)
        b = a + 1
        mid1 = None
        mid2 = None
        rs = 0

        for idx, v in enumerate(self.d):
            rs += v
            if rs >= a and mid1 is None:
                mid1 = idx
            if rs >= b:
                mid2 = idx
                break

        if self.maxLen % 2 == 0:
            return (mid1 + mid2) / 2.0
        else:
            return mid2


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    r = RunningMedian(d)
    for v in expenditure[:d]:
        r.add(v)

    for idx, v in enumerate(expenditure[d:]):
        median = r.median()
        # print(median, expenditure[idx: idx+d])
        if v >= (2 * median):
            notifications += 1
        r.add(v)

    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
