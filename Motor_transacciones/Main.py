import tkinter as tk
from gui import BankGUI

def main():

    root = tk.Tk()
    app = BankGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()