import customtkinter as ctk

from interface import theme
from interface.widgets.songcard import SongCard

class HomeScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.create_layout()

    def create_layout(self):
        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.left_frame = ctk.CTkFrame(self, fg_color=theme.PANEL, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.right_frame = ctk.CTkFrame(self, fg_color=theme.BACKGROUND, corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.bottom_frame = ctk.CTkFrame(self, fg_color=theme.PANEL, height=70, corner_radius=0)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.bottom_frame.grid_propagate(False)
        self.create_left()
        self.create_right()
        self.create_bottom()

    def create_left(self):
        self.song_panel = ctk.CTkFrame(self.left_frame, fg_color=theme.PANEL)
        self.song_panel.pack(fill="both", expand=False)
        title = ctk.CTkLabel(self.song_panel, text="Select a Song", font=theme.TITLE_FONT, text_color=theme.PRIMARY)
        title.pack(pady=(20, 30))
        self.song_container = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.song_container.pack(fill="both", expand=True)
        songs = [
            "Beer",
            "Buwan",
            "Pompeii",
            "Total Eclipse of the Heart",
        ]
        self.song_cards = []
        self.selected_song = None
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
        self.sing_button.configure(state="normal", fg_color=theme.PRIMARY, hover=True)

    def create_right(self):
        self.cover = ctk.CTkFrame(self.right_frame, width=350, height=350, fg_color=theme.SECONDARY)
        self.cover.pack(pady=30)
        self.cover.pack_propagate(False)
        self.cover_label = ctk.CTkLabel(self.cover, text="Album Cover")
        self.cover_label.place(relx=0.5, rely=0.5, anchor="center")
        self.song_name_label = ctk.CTkLabel(self.right_frame, text="Song Name", font=theme.HEADING_FONT)
        self.song_name_label.pack(pady=(20, 5))
        self.artist_label = ctk.CTkLabel(self.right_frame, text="by Artist", font=theme.BODY_FONT)
        self.artist_label.pack()
        self.duration_label = ctk.CTkLabel(self.right_frame, text="⏱ 3:45", font=theme.SMALL_FONT)
        self.duration_label.pack(pady=(10, 25))
        self.sing_button = ctk.CTkButton(
            self.right_frame,
            text="SING!",
            width=250,
            height=60,
            font=theme.HEADING_FONT,
            state="disabled",
            fg_color=theme.SECONDARY,
            hover_color=theme.ACCENT,
            text_color="black",
            hover=False,
            command=self.start_song
        )
        self.sing_button.pack()

    def start_song(self):
        if self.selected_song is None:
            return
        self.master.show_performance(self.selected_song.title)

    def create_bottom(self):
        # self.bottom_frame = ctk.CTkFrame(
        #     self,
        #     fg_color=theme.PANEL,
        #     height=theme.BOTTOM_BAR_HEIGHT,
        #     corner_radius=0
        # )
        # self.bottom_frame.pack(side="bottom", fill="x")
        # self.bottom_frame.pack_propagate(False)
        mic = ctk.CTkLabel(
            self.bottom_frame,
            text="Input: AudioRelay Virtual Mic",
            font=theme.SMALL_FONT
        )
        mic.pack(side="left", padx=30)
        waveform = ctk.CTkLabel(
            self.bottom_frame,
            text="▁▂▃▄▅▆▇█▇▆▅▄▃▂▁",
            font=("Consolas", 20),
            text_color=theme.INFO
        )
        waveform.pack(side="right", padx=30)