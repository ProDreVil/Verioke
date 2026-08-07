import customtkinter as ctk
import sounddevice as sd
import utils.config as config

from interface import theme
from interface.screens.home import HomeScreen
from interface.screens.performance import PerformanceScreen
from interface.screens.results import ResultScreen
from sound.inputmeter import InputMeter

class Verioke(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(theme.WINDOW_TITLE)
        self.geometry(f"{theme.WINDOW_WIDTH}x{theme.WINDOW_HEIGHT}")
        self.minsize(theme.MIN_WIDTH, theme.MIN_HEIGHT)
        self.configure(fg_color=theme.BACKGROUND)
        try:
            self.iconbitmap("assets/ui/favicon.ico")
        except Exception:
            pass
        self.input_meter = InputMeter()
        self.input_meter.start()
        # self.debug_meter()
        self.current_screen = None
        self.warmup_audio()
        self.show_home()
        self.after(10, lambda: self.state("zoomed"))

    # def debug_meter(self):
    #     print(round(self.input_meter.get_level(), 4))
    #     self.after(200, self.debug_meter)
    
    def switch_screen(self, screen, *args):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = screen(self, *args)
        self.current_screen.pack(fill="both", expand=True)

    def show_home(self):
        self.switch_screen(HomeScreen)

    def show_performance(self, song):
        self.switch_screen(PerformanceScreen, song)

    def show_results(self):
        self.switch_screen(ResultScreen)

    def warmup_audio(self):
        try:
            sd.rec(
                int(0.05 * config.SAMPLE_RATE),
                samplerate=config.SAMPLE_RATE,
                channels=1,
                dtype="float32",
                device=config.INPUT_DEVICE
            )
            sd.wait()
            print("Audio warm-up complete.")
        except Exception as e:
            print(f"Audio warm-up failed: {e}")