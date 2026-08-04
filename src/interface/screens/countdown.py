from customtkinter import *

class CountdownScreen(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        CTkLabel(
            self,
            text="Countdown",
            font=("Arial",40)
        ).pack(pady=50)

        CTkButton(
            self,
            text="Next",
            command=master.show_performance
        ).pack()