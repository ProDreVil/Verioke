import customtkinter as ctk
import time

from interface import theme
from sound.player import AudioPlayer
from sound.recorder import record_audio
from sound.audio import get_audio_duration
from threading import Thread
from utils.helpers import get_recording_path
from utils.lrc import load_lrc

class PerformanceScreen(ctk.CTkFrame):
    def __init__(self, master, song=None):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.song = song
        self.player = AudioPlayer()
        self.prepare_song()
        self.song_dration = 0
        self.start_time = 0
        self.create_stage()
        self.start_countdown()

    def prepare_song(self):
        self.instrumental = f"assets/songs/{self.song}/instrumental.wav"
        self.duration = get_audio_duration(self.instrumental)
        self.player.load(self.instrumental)
        self.lyrics = load_lrc(f"assets/songs/{self.song}/lyrics.lrc")
        self.current_index = 0

    def start_performance(self):
        output = get_recording_path(self.song)
        self.current_index = 0
        if self.lyrics:
            self.current_lyric.configure(text=self.lyrics[0]["text"])
        if len(self.lyrics) > 1:
            self.next_lyric.configure(text=self.lyrics[1]["text"])
        else:
            self.next_lyric.configure(text="")
        self.song_duration = self.duration
        self.start_time = time.time()
        self.player.play()
        Thread(target=record_audio, args=(output, self.duration), daemon=True).start()
        self.update_progress()

    def start_countdown(self):
        self.count = 3
        self.update_countdown()

    def update_countdown(self):
        if self.count > 0:
            self.countdown.configure(text=str(self.count))
            self.count -= 1
            self.after(1000, self.update_countdown)
        else:
            self.countdown.destroy()
            self.start_performance()

    def update_lyrics(self, elapsed):
        while (self.current_index + 1 < len(self.lyrics) and elapsed >= self.lyrics[self.current_index + 1]["time"]):
            self.current_index += 1
        self.current_lyric.configure(text=self.lyrics[self.current_index]["text"])
        if self.current_index + 1 < len(self.lyrics):
            self.next_lyric.configure(text=self.lyrics[self.current_index + 1]["text"])
        else:
            self.next_lyric.configure(text="")

    def update_progress(self):
        elapsed = time.time() - self.start_time
        self.update_lyrics(elapsed)
        progress = min(elapsed / self.song_duration, 1)
        self.progress.set(progress)
        if progress < 1:
            self.after(50, self.update_progress)
        else:
            self.master.show_results()

    def create_stage(self):
        self.stage = ctk.CTkFrame(self, fg_color=theme.BACKGROUND, corner_radius=0)
        self.stage.pack(fill="both", expand=True)
        self.background = ctk.CTkFrame(self.stage, fg_color=theme.BACKGROUND, corner_radius=0)
        self.background.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.background_label = ctk.CTkLabel(
            self.background,
            text="Background Video",
            font=theme.BODY_FONT
        )
        self.background_label.place(relx=0.5, rely=0.35, anchor="center")
        self.song_title = ctk.CTkLabel(
            self.stage,
            text="Beer - Itchyworms",
            font=theme.HEADING_FONT,
            text_color=theme.ACCENT
        )
        self.song_title.place(relx=0.05, rely=0.05, anchor="w")
        self.recording = ctk.CTkLabel(
            self.stage,
            text="🔴",
            font=theme.SMALL_FONT,
            text_color=theme.ERROR
        )
        self.recording.place(relx=0.96, rely=0.05, anchor="ne")
        self.countdown = ctk.CTkLabel(
            self.stage,
            text="3",
            font=(theme.FONT_FAMILY, 110, "bold"),
            text_color=theme.ACCENT
        )

        self.countdown.place(relx=0.5, rely=0.38, anchor="center")
        self.current_lyric = ctk.CTkLabel(
            self.stage,
            text="Current lyric",
            font=(theme.FONT_FAMILY, 40, "bold"),
            text_color=theme.CURRENT_LYRIC,
            justify="left",
            anchor="w",
            wraplength=1100
        )
        self.current_lyric.place(relx=0.05, rely=0.73, anchor="w")
        self.next_lyric = ctk.CTkLabel(
            self.stage,
            text="Next lyric",
            font=(theme.FONT_FAMILY, 26),
            text_color=theme.NEXT_LYRIC,
            justify="left",
            anchor="w",
            wraplength=1100
        )
        self.next_lyric.place(relx=0.05, rely=0.78, anchor="w")
        self.progress = ctk.CTkProgressBar(
            self.stage,
            width=1280,
            height=10
        )
        self.progress.place(relx=0.5, rely=0.87, anchor="center")
        self.progress.set(0)
        self.waveform = ctk.CTkLabel(
            self.stage,
            text="▁▂▃▄▅▆▇█▇▆▅▄▃▂▁",
            font=("Consolas", 22),
            text_color=theme.INFO
        )
        self.waveform.place(relx=0.5, rely=0.93, anchor="center")