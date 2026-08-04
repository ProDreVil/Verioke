from customtkinter import *

from interface.screens.home import HomeScreen
from interface.screens.countdown import CountdownScreen
from interface.screens.performance import PerformanceScreen
from interface.screens.results import ResultScreen

class Verioke(CTk):

    def __init__(self):
        super().__init__()

        self.title("Verioke")
        self.geometry("1280x720")
        self.attributes("-fullscreen", False)
        self.iconbitmap("assets/ui/logo.ico")

        self.current_screen = None

        self.show_home()

    def change_screen(self, screen):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = screen(self)
        self.current_screen.pack(fill="both", expand=True)

    def show_home(self):
        self.change_screen(HomeScreen)

    def show_countdown(self):
        self.change_screen(CountdownScreen)

    def show_performance(self):
        self.change_screen(PerformanceScreen)

    def show_results(self):
        self.change_screen(ResultScreen)