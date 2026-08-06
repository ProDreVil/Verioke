import customtkinter as ctk

from interface import theme

class SongCard(ctk.CTkFrame):
    def __init__(self, master, title, command=None):
        super().__init__(master, fg_color=theme.PANEL, corner_radius=0, border_width=0, height=60)
        self.title = title
        self.selected = False
        self.command = command
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        self.song_label = ctk.CTkLabel(
            self,
            text=f"♪ {self.title}",
            font=theme.BODY_FONT,
            text_color=theme.TEXT,
            anchor="w"
        )
        self.song_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=15
        )
        self.indicator = ctk.CTkLabel(
            self,
            text="",
            font=theme.BODY_FONT,
            text_color=theme.PRIMARY,
            width=30
        )
        self.indicator.grid(
            row=0,
            column=1,
            padx=(0, 20)
        )

    def bind_events(self):
        widgets = [
            self,
            self.song_label,
            self.indicator
        ]
        for widget in widgets:
            widget.bind("<Enter>", self.on_enter)
            widget.bind("<Leave>", self.on_leave)
            widget.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if self.command:
            self.command(self)

    def on_enter(self, event):
        if self.selected:
            return
        self.configure(
            fg_color="#2A2A2A"
        )

    def on_leave(self, event):
        if self.selected:
            return
        self.configure(
            fg_color=theme.PANEL
        )

    def set_selected(self, state):
        self.selected = state
        if state:

            self.configure(
                border_width=2,
                border_color=theme.PRIMARY,
                fg_color="#2A2A2A"
            )

            self.indicator.configure(
                text="►"
            )

        else:

            self.configure(
                border_width=0,
                fg_color=theme.PANEL
            )

            self.indicator.configure(
                text=""
            )