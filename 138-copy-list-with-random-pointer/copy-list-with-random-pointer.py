"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        hashMap={} # will be filled like this: {'originalNode':'Node(originalNode.val) aka newNode'}

        #this loop creates a dict with key:value pairs that are "originalNode:copiedNode"
        originalNode = head
        while originalNode is not None:
            hashMap[originalNode] = Node(originalNode.val) #new key:value pair with originalNode:copiedNode (<-just has value, not next or random)
            originalNode = originalNode.next #go to the next Node

        ##and now this loop creates the deepcopy "copy" by calling the dict with the original Node intsances, but since a the dict then returns the value of this key, which is the copied node, we get "copy" which consist of copied nodes and their .next and .random functions also point to copied nodes
        originalNode = head
        while originalNode is not None:
            (hashMap[originalNode]).next = hashMap[originalNode.next] if originalNode.next else None #copy.next is now being set as 
            (hashMap[originalNode]).random = hashMap[originalNode.random] if originalNode.random else None

            originalNode = originalNode.next

        return hashMap[head]


        



        
        