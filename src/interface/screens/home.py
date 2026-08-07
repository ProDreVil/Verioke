import customtkinter as ctk
from utils.lrc import load_lrc
from sound.audio import get_audio_duration
from pathlib import Path
from PIL import Image

from pathlib import Path
from interface import theme
from interface.widgets.songcard import SongCard

class HomeScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.song_cards = []
        self.selected_song = None
        self.create_layout()

    def create_layout(self):
        self.grid_columnconfigure(0, weight=1, minsize=theme.LEFT_PANEL_WIDTH)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.left_frame = ctk.CTkFrame(self, fg_color=theme.PANEL, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.right_frame = ctk.CTkFrame(self, fg_color=theme.BACKGROUND, corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.bottom_frame = ctk.CTkFrame(self, fg_color=theme.PANEL, height=theme.BOTTOM_BAR_HEIGHT,corner_radius=0)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.bottom_frame.grid_propagate(False)
        self.create_left()
        self.create_right()
        self.create_bottom()

    def create_left(self):
        self.song_panel = ctk.CTkFrame(self.left_frame, fg_color=theme.PANEL)
        self.song_panel.pack(fill="x")
        title = ctk.CTkLabel(self.song_panel, text="> Select a Song <", font=theme.TITLE_FONT, text_color=theme.PRIMARY)
        title.pack(pady=(theme.SONG_PANEL_TITLE_TOP, theme.SONG_PANEL_TITLE_BOTTOM))
        self.song_container = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.song_container.pack(fill="both", expand=True)
        songs_path = Path("assets/songs")
        songs = sorted(
            folder.name
            for folder in songs_path.iterdir()
            if folder.is_dir()
        )
        for song in songs:
            card = SongCard(self.song_container, song, self.select_song)
            card.pack(fill="x")
            self.song_cards.append(card)

    def select_song(self, clicked_card):
        if self.selected_song == clicked_card:
            clicked_card.set_selected(False)
            self.selected_song = None
            self.sing_button.configure(state="disabled", fg_color=theme.SECONDARY, hover=False)
            return
        for card in self.song_cards:
            card.set_selected(False)
        clicked_card.set_selected(True)
        self.selected_song = clicked_card
        self.load_song(clicked_card.title)
        self.sing_button.configure(state="normal", fg_color=theme.PRIMARY, hover=True)

    def load_song(self, song_name):
        folder = Path("assets/songs") / song_name
        song = load_lrc(folder / "lyrics.lrc")
        self.song_name_label.configure(text=song["title"])
        self.artist_label.configure(text=song["artist"])
        duration = get_audio_duration(folder / "instrumental.wav")
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        self.duration_label.configure(text=f"⏱ {minutes}:{seconds:02d}")
        image = ctk.CTkImage(
            light_image=Image.open(folder / "cover.jpg"),
            dark_image=Image.open(folder / "cover.jpg"),
            size=(theme.COVER_SIZE, theme.COVER_SIZE)
        )
        self.cover_label.configure(image=image, text="")
        self.cover_label.image = image

    def create_right(self):
        self.cover = ctk.CTkFrame(self.right_frame, width=theme.COVER_SIZE, height=theme.COVER_SIZE, fg_color=theme.SECONDARY)
        self.cover.pack(pady=theme.COVER_TOP_PADDING)
        self.cover.pack_propagate(False)
        self.cover_label = ctk.CTkLabel(self.cover, text="Album Cover")
        self.cover_label.place(relx=0.5, rely=0.5, anchor="center")
        self.song_name_label = ctk.CTkLabel(self.right_frame, text="Song Name", font=theme.HEADING_FONT, width=400, anchor="center")
        self.song_name_label.pack(pady=(theme.SONG_NAME_TOP, theme.SONG_NAME_BOTTOM))
        self.artist_label = ctk.CTkLabel(self.right_frame, text="by Artist", font=theme.BODY_FONT)
        self.artist_label.pack()
        self.duration_label = ctk.CTkLabel(self.right_frame, text="⏱ --:--", font=theme.SMALL_FONT)
        self.duration_label.pack(pady=(theme.DURATION_TOP, theme.DURATION_BOTTOM))
        self.sing_button = ctk.CTkButton(
            self.right_frame,
            text="SING!",
            width=theme.SING_BUTTON_WIDTH,
            height=theme.SING_BUTTON_HEIGHT,
            font=theme.HEADING_FONT,
            state="disabled",
            fg_color=theme.SECONDARY,
            hover_color=theme.ACCENT,
            text_color="black",
            hover=False,
            command=self.start_song
        )
        self.sing_button.pack()
        self.song_name_label.pack(
            pady=(theme.SONG_NAME_TOP, theme.SONG_NAME_BOTTOM),
            fill="x"
        )

    def start_song(self):
        if self.selected_song is None:
            return
        self.master.show_performance(self.selected_song.title)

    def create_bottom(self):
        mic = ctk.CTkLabel(self.bottom_frame, text="Input: AudioRelay Virtual Mic", font=theme.SMALL_FONT)
        mic.pack(side="left", padx=theme.BOTTOM_SIDE_PADDING)
        waveform = ctk.CTkLabel(
            self.bottom_frame,
            text="▁▂▃▄▅▆▇█▇▆▅▄▃▂▁",
            font=(
                "Consolas",
                theme.BOTTOM_WAVEFORM_FONT_SIZE
            ),
            text_color=theme.INFO
        )
        waveform.pack(side="right", padx=theme.BOTTOM_SIDE_PADDING)