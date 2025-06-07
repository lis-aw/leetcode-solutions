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
        hashMap={}
        originalNode = head
        while originalNode is not None:
            hashMap[originalNode] = Node(originalNode.val) 
            originalNode = originalNode.next 
        originalNode = head
        while originalNode is not None:
            (hashMap[originalNode]).next = hashMap[originalNode.next] if originalNode.next else None 
            (hashMap[originalNode]).random = hashMap[originalNode.random] if originalNode.random else None
            originalNode = originalNode.next
        return hashMap[head]     