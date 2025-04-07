import tkinter as tk
import BST
window=tk.Tk()
window.title("Binary Search Tree and AVL Tree Visualization")
canvas=tk.Canvas(window, width=800, height=600, bg="white")
button=tk.Button(window, text="Insert", command=lambda: None) # Placeholder for insert function
entry=tk.Entry(window)
canvas.pack(side='right')
entry.pack()
button.pack()

bst=BST.BinarySearchTree() #novy strom

#function to insert a value into the BST and draw it


canvas.mainloop()
