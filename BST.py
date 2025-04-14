class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        # Insert a new value into the BST
        # smaller values go to the left, larger values go to the right
        if value < self.data:
            if self.left is None:
                self.left=Node(value) #constructor call
            else:
                self.left.insert(value) #recursive call
        elif value > self.data:
            if self.right is None:
                self.right=Node(value) #constructor call
            else:
                self.right.insert(value) #recursive call

    def drawNode(self, x, y, px, py, canvas):
        if px!=-1: #if there is a parent
            canvas.create_line(px, py, x, y) #draw line from parent to child
        if self.left: #check if left child exists
            self.left.drawNode(x-50, y+50, x, y, canvas)
        if self.right: #check if right child exists
            self.right.drawNode(x+50, y+50, x, y, canvas)
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white") #draw the node after the children and lines
        canvas.create_text(x, y, text=str(self.data)) #draw the text in the node


    def preorder(self):
        # Preorder traversal: root -> left -> right
        print(self.data, end=" ") #print the root
        if self.left: #check if left child exists
            self.left.preorder() #recursive call to the left child
        if self.right: #check if right child exists
            self.right.preorder() #recursive call to the right child

    def inorder(self):
        # Inorder traversal: left -> root -> right
        if self.left: #check if left child exists
            self.left.inorder() #recursive call to the left child
        print(self.data, end=" ") #print the root
        if self.right: #check if right child exists
            self.right.inorder() #recursive call to the right child

    def postorder(self):
        # Postorder traversal: left -> right -> root
        if self.left: #check if left child exists
            self.left.postorder() #recursive call to the left child
        if self.right: #check if right child exists
            self.right.postorder() #recursive call to the right child
        print(self.data, end=" ")

    def search(self, target):
        if self.data==target:
            return self #found the target, return the node
        elif target<self.data: #search in the left subtree
            return self.left.search(target) #recursive call
        else:
            return self.right.search(target) #search in the right subtree

    def findMinParent(self, parent):
        pass #placeholder

    def findMaxParent(self, parent):
        pass #placeholder

    def delete(self, target, parent):
        # Delete a node with the given target value
        pass #placeholder
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def preorder(self):
        if self.root:
            self.root.preorder()
        else:
            print("BST is empty.")
    def inorder(self):
        if self.root:
            self.root.inorder()
        else:
            print("BST is empty.")
    def postorder(self):
        if self.root:
            self.root.postorder()
        else:
            print("BST is empty.")

    def drawTree(self, startx, starty, canvas):
        if self.root:
            canvas.delete("all") # delete previous tree
            self.root.drawNode(startx, starty, -1, -1, canvas) # to be completed
        else:
            print("BST is empty.")

    def delete(self, target):
        if self.root:
            #edge case: root is a target
            #else, delete a node
            pass
        else:
            print("BST is empty.")