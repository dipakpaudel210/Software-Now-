#!/usr/bin/env python3
"""
HIT137 Assignment 3 - AI Model Integration GUI
Reusing Assignment 2 repository structure
Team Leader: [YOUR NAME]
"""
import tkinter as tk
from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
