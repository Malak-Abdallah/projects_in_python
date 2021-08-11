from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)
root.left.left=Node(5)
root.left.right=Node(7)
root.right.left=Node(7)
root.right.right=Node(9)


goal=[]

def check(node,maxx):
    maxx=max(maxx,root.value)
    if root.value >= maxx:
        goal.append(node.value)
    else:
        check(root.right,maxx)
        check(root.left,maxx)


check(root,root.value)





print(goal)


# Getting binary tree
#print('Binary tree :', root)
'''
def add_node(self,value):
    self.value = value
    self.left = None
    self.right = None


if __name__ == '__main__':
    # creating a tree:
    root=add_node(3)
    root.left=add_node(1)
    root.right=add_node(4)
    root.left.left=add_node(3)
    root.right.left=add_node(1)
    root.right.right=add_node(5)
'''





