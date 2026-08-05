from customtkinter import *

class HomeScreen(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        CTkLabel(self, text="VERIOKE", font=("Arial",40,"bold")).pack(pady=50)
        CTkButton(self, text="Sing", command=master.show_countdown).pack()