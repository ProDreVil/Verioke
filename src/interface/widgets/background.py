import customtkinter as ctk
import random
from pathlib import Path
from PIL import Image, ImageTk
import cv2

from interface import theme


class BackgroundVideo(ctk.CTkFrame):
    def __init__(self, master, bpm=120):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0
        )

        self.bpm = bpm
        self.video_path = None
        self.cap = None
        self.running = False
        self.playback_speed = 1.0

        self.label = ctk.CTkLabel(
            self,
            text="",
            fg_color="transparent"
        )
        self.label.pack(fill="both", expand=True)

        self.select_video()

    def select_video(self):
        folder = Path("assets/ui/backgrounds")

        if not folder.exists():
            return

        videos = [
            path for path in folder.iterdir()
            if path.suffix.lower() in [
                ".mp4",
                ".avi",
                ".mov",
                ".mkv"
            ]
        ]

        if not videos:
            return

        self.video_path = random.choice(videos)

    def start(self):
        if not self.video_path:
            return

        if self.cap:
            self.cap.release()

        self.cap = cv2.VideoCapture(str(self.video_path))

        fps = self.cap.get(cv2.CAP_PROP_FPS)
        frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)

        if fps <= 0 or frame_count <= 0:
            self.cap.release()
            self.cap = None
            return

        duration = frame_count / fps
        max_start = max(0, duration - 5)
        start_time = random.uniform(0, max_start)

        self.cap.set(
            cv2.CAP_PROP_POS_MSEC,
            start_time * 1000
        )

        self.playback_speed = max(
            0.75,
            min(self.bpm / 120, 1.5)
        )

        print(f"Video: {self.video_path.name}")
        print(f"BPM: {self.bpm:.2f}")
        print(f"Playback speed: {self.playback_speed:.2f}x")
        print(f"Starting timestamp: {start_time:.2f}s")

        self.running = True
        self.update_frame()

    def update_frame(self):
        if not self.running or self.cap is None:
            return

        ret, frame = self.cap.read()

        if not ret:
            self.cap.release()
            self.cap = None

            self.select_video()

            if self.video_path:
                self.start()

            return

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        width = self.winfo_width()
        height = self.winfo_height()

        if width > 1 and height > 1:
            image = Image.fromarray(frame)
            image = image.resize(
                (width, height),
                Image.Resampling.LANCZOS
            )

            photo = ImageTk.PhotoImage(image)

            self.label.configure(image=photo)
            self.label.image = photo

        fps = self.cap.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 30

        delay = max(
            1,
            int(1000 / (fps * self.playback_speed))
        )

        self.after(delay, self.update_frame)

    def stop(self):
        self.running = False

        if self.cap:
            self.cap.release()
            self.cap = None