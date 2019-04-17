from tkinter import *


space = ":          "

class ChadtherUnderground:
    location = []
    temp = []
    def __init__(self, master):
        self.master = master
        master.title("ChadtherUnderground")

        location = ["asdf", "fdas", "one_more"]
        temp = ["1", "2", "3"]


        for index in range(len(location)):     # by index
            Label(master, text=location[index]+space).grid(row=index, column=1)
            Label(master, text=temp[index]+space).grid(row=index, column=2)

    # if __name__ == "__main__":

    def addNode(self, master, location, temperature): 
        # this cannot update? you have to rewrite it?
        for index in range(len(location)):     # by index
            Label(master, text=location[index]+space).grid(row=index, column=1)
            Label(master, text=temperature[index]+space).grid(row=index, column=2)

root = Tk()
my_gui = ChadtherUnderground(root)
root.geometry("500x200")
root.mainloop()