import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
    print("TEST")

    root = tk.Tk()
    root.withdraw()

    while True:
        selection = input("[1] exit\nSelection: ")
        if selection == "1":
            break
        else:
            print("Invalid option.")