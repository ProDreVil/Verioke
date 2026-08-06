import customtkinter as ctk

from interface import theme
from interface.screens.home import HomeScreen
from interface.screens.countdown import CountdownScreen
from interface.screens.performance import PerformanceScreen
from interface.screens.results import ResultScreen

class Verioke(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(theme.WINDOW_TITLE)
        self.geometry(f"{theme.WINDOW_WIDTH}x{theme.WINDOW_HEIGHT}")
        self.minsize(theme.MIN_WIDTH, theme.MIN_HEIGHT)
        self.configure(fg_color=theme.BACKGROUND)
        self.attributes("-fullscreen", False)
        try:
            self.iconbitmap("assets/ui/favicon.ico")
        except Exception:
            pass
        self.current_screen = None
        self.show_home()

    def switch_screen(self, screen):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = screen(self)
        self.current_screen.pack(fill="both", expand=True)

    def show_home(self):
        self.switch_screen(HomeScreen)

    def show_countdown(self):
        self.switch_screen(CountdownScreen)

    def show_performance(self):
        self.switch_screen(PerformanceScreen)

    def show_results(self):
        self.switch_screen(ResultScreen)