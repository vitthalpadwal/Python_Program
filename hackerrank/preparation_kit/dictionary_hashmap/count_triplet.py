"""
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

For example, . If , we have  and  at indices  and .

Function Description

Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given  as an integer.

countTriplets has the following parameter(s):

arr: an array of integers
r: an integer, the common ratio
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .

Constraints

Output Format

Return the count of triplets that form a geometric progression.

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .


"""

from collections import defaultdict

def count_triple():
    print("Enter the number of input and common divisor")
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    m1, m2 = defaultdict(int), defaultdict(int)

    triplets = 0
    breakpoint()
    for i in reversed(arr):
        if (i * r) in m2:
            triplets += m2[i * r]

        if (i * r) in m1:
            m2[i] += m1[i * r]

        m1[i] += 1
    print(triplets)

if __name__ == '__main__':
    count_triple()



"""
Geeks for Geeks solution
# Python 3 program to find if  
# there exist three elements in 
# Geometric Progression or not 
  
# The function prints three elements  
# in GP if exists. 
# Assumption: arr[0..n-1] is sorted. 
def findGeometricTriplets(arr, n): 
  
    # One by fix every element  
    # as middle element 
    for j in range(1, n - 1): 
      
        # Initialize i and k for  
        # the current j 
        i = j - 1
        k = j + 1
  
        # Find all i and k such that  
        # (i, j, k) forms a triplet of GP 
        while (i >= 0 and k <= n - 1): 
          
            # if arr[j]/arr[i] = r and  
            # arr[k]/arr[j] = r and r  
            # is an integer (i, j, k) forms  
            # Geometric Progression 
            while (arr[j] % arr[i] == 0 and
                   arr[k] % arr[j] == 0 and
                   arr[j] // arr[i] == arr[k] // arr[j]): 
              
                # print the triplet 
                print( arr[i] , " " , arr[j],  
                                " " , arr[k])  
  
                # Since the array is sorted and  
                # elements are distinct. 
                k += 1
                i -= 1
  
            # if arr[j] is multiple of arr[i] 
            # and arr[k] is multiple of arr[j],  
            # then arr[j] / arr[i] != arr[k] / arr[j]. 
            # We compare their values to 
            # move to next k or previous i. 
            if(arr[j] % arr[i] == 0 and
                        arr[k] % arr[j] == 0): 
              
                if(arr[j] // arr[i] < arr[k] // arr[j]): 
                    i -= 1
                else: 
                    k += 1
  
            # else if arr[j] is multiple of  
            # arr[i], then try next k. Else,  
            # try previous i. 
            elif (arr[j] % arr[i] == 0): 
                k += 1
            else: 
                i -= 1
  
# Driver code 
if __name__ =="__main__": 
      
    arr = [1, 2, 4, 16] 
    n = len(arr) 
  
    findGeometricTriplets(arr, n) 
  
# This code is contributed  
# by ChitraNayal 

"""