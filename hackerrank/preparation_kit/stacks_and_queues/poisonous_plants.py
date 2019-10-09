"""
There are a number of plants in a garden. Each of these plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.

For example, pesticide levels . Using a -indexed array, day  plants  and  die leaving . On day , plant  of the current array dies leaving . As there is no plant with a higher concentration of pesticide than the one to its left, plants stop dying after day .

Function Description
Complete the function poisonousPlants in the editor below. It must return an integer representing the number of days until plants no longer die from pesticide.

poisonousPlants has the following parameter(s):

p: an array of integers representing pesticide levels in each plant
Input Format

The first line contains an integer , the size of the array .
The next line contains  space-separated integers .

Constraints



Output Format

Output an integer equal to the number of days after which no plants die.

Sample Input

7
6 5 8 4 7 10 9
Sample Output

2
Explanation

Initially all plants are alive.

Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}

Plants[k] = (i,j) => jth plant has pesticide amount = i.

After the 1st day, 4 plants remain as plants 3, 5, and 6 die.

Plants = {(6,1), (5,2), (4,4), (9,7)}

After the 2nd day, 3 plants survive as plant 7 dies.

Plants = {(6,1), (5,2), (4,4)}

After the 2nd day the plants stop dying.
"""

from collections import deque


# Thanks Python for not having a Linked List data structure!
class Node:
    __slots__ = ['value', 'prev', 'next']

    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class EndOfDay:
    pass


def is_last_node(array, node):
    return node.next == len(array)


def is_first_node(node):
    return node.prev == -1


def delete_node(array, node):
    if not is_first_node(node):
        array[node.prev].next = node.next
    if not is_last_node(array, node):
        array[node.next].prev = node.prev


def main():
    n = int(input())
    days = 0
    work = deque()
    plants = []

    # Populate the initial plants list and initialize the queue
    for i, v in enumerate(map(int, input().split())):
        node = Node(v, i - 1, i + 1)
        plants.append(node)
        if not is_first_node(node):
            if node.value > plants[node.prev].value:
                work.appendleft(node)

    while days < n:
        died = 0
        days += 1
        work.appendleft(EndOfDay())

        while True:
            dead = work.pop()

            if isinstance(dead, EndOfDay):
                break

            try:
                peek = work[-1]
            except IndexError:
                peek = None

            if (not is_last_node(plants, dead) and
                    plants[dead.next] is not peek and
                    plants[dead.prev].value < plants[dead.next].value):
                work.appendleft(plants[dead.next])
            delete_node(plants, dead)
            died += 1

        if not died:
            print(days - 1)
            break

if __name__ == '__main__':
    main()