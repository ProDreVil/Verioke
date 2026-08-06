import customtkinter as ctk

from interface import theme

class PerformanceScreen(ctk.CTkFrame):
    def __init__(self, master, song=None):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.song = song
        self.create_stage()

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