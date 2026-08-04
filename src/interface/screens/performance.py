from customtkinter import *

class PerformanceScreen(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        CTkLabel(
            self,
            text="Singing...",
            font=("Arial",40)
        ).pack(pady=50)

        CTkButton(
            self,
            text="Finish",
            command=master.show_results
        ).pack()