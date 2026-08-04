from customtkinter import *

class ResultScreen(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        CTkLabel(
            self,
            text="Final Score",
            font=("Arial",40)
        ).pack(pady=50)

        CTkButton(
            self,
            text="Home",
            command=master.show_home
        ).pack()