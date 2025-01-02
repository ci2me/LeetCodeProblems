## TASK
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Create Linked List
class LinkedList:
    # Head Node
    def __init__(self):
        self.head = ListNode()

    # Add to list
    def append(self,data):
        new_node = ListNode(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # initialise variables
        str1 = ''
        str2 = ''
        curr = l1
        # create a string from linked list values
        while curr.next != None:
            str1 = str1+ str(curr.val)
            curr = curr.next
        str1 = str1 + str(curr.val)

        # reverse the string
        str1 = str1[::-1]

        # repeat for second string
        curr = l2
        while curr.next != None:
            str2 = str2+ str(curr.val)
            curr = curr.next
        str2 = str2 + str(curr.val)
        str2 = str2[::-1]

        # turn to int and find the sum
        x = int(str1)
        y = int(str2)
        ans = x + y
        ans = str(ans)
        #reverse string
        ans = ans[::-1]
        # create linked list with values
        my_list = LinkedList()
        my_list.head.val = int(ans[0])
        length = len(ans)
        i = 1
        while i <length:
            my_list.append(int(ans[i]))
            i=i+1
        print(my_list.head)
        #return answer
        return(my_list.head)

            
