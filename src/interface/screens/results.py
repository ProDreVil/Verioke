import customtkinter as ctk

from pathlib import Path
from PIL import Image

from interface import theme
from core.scorer import (calculate_pitch_score, calculate_timing_score, calculate_loudness_score)

class ResultScreen(ctk.CTkFrame):
    def __init__(self, master, result):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.result = result
        self.score = int(result["score"])
        self.create_ui()

    def create_ui(self):
        score_label = ctk.CTkLabel(
            self,
            text=str(self.score),
            font=theme.SCORE_FONT,
            text_color=theme.ACCENT
        )
        score_label.pack(pady=(30, 0))
        grade_label = ctk.CTkLabel(
            self,
            text=self.get_grade(),
            font=theme.BODY_FONT,
            text_color=theme.PRIMARY
        )
        grade_label.pack(pady=(0, 10))
        image_path = Path("assets/ui/grades") / self.get_result_image()
        if image_path.exists():
            image = ctk.CTkImage(
                light_image=Image.open(image_path),
                dark_image=Image.open(image_path),
                size=(180, 180)
            )
            image_label = ctk.CTkLabel(
                self,
                image=image,
                text=""
            )
            image_label.pack(pady=10)
        breakdown = self.calculate_breakdown()
        breakdown_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        breakdown_frame.pack(
            fill="x",
            padx=100,
            pady=20
        )
        self.create_breakdown_bar(
            breakdown_frame,
            "Pitch Accuracy",
            breakdown["pitch"]
        )
        self.create_breakdown_bar(
            breakdown_frame,
            "Timing Accuracy",
            breakdown["timing"]
        )
        self.create_breakdown_bar(
            breakdown_frame,
            "Loudness Accuracy",
            breakdown["loudness"]
        )
        back_button = ctk.CTkButton(
            self,
            text="Return",
            width=200,
            height=40,
            font=theme.HEADING_FONT,
            fg_color=theme.PRIMARY,
            hover_color=theme.ACCENT,
            command=self.back_home
        )
        back_button.pack(pady=30)

    def create_breakdown_bar(self, parent, label, value):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(pady=8)
        if label == "Pitch Accuracy":
            progress_color = theme.PITCH
        elif label == "Timing Accuracy":
            progress_color = theme.TIMING
        else:
            progress_color = theme.LOUDNESS
        label_widget = ctk.CTkLabel(
            container,
            text=label,
            font=theme.BODY_FONT,
            width=150,
            anchor="w"
        )
        label_widget.grid(row=0, column=0, padx=(0, 10))
        progress = ctk.CTkProgressBar(
            container,
            width=300,
            height=8,
            corner_radius=6,
            progress_color=progress_color
        )
        progress.grid(row=0, column=1, padx=10)
        value_widget = ctk.CTkLabel(
            container,
            text=str(value),
            font=theme.BODY_FONT,
            width=30,
            anchor="e"
        )
        value_widget.grid(row=0, column=2, padx=(10, 0))
        progress.set(value / 100)

    def back_home(self):
        self.master.show_home()

    def calculate_breakdown(self):
        matches = self.result["matches"]
        if not matches:
            return {
                "pitch": 0,
                "timing": 0,
                "loudness": 0
            }
        pitch = sum(
            calculate_pitch_score(match)
            for match in matches
        )
        timing = sum(
            calculate_timing_score(match)
            for match in matches
        )
        loudness = sum(
            calculate_loudness_score(match)
            for match in matches
        )
        total = len(matches)
        return {
            "pitch": round(pitch / total),
            "timing": round(timing / total),
            "loudness": round(loudness / total)
        }

    def get_result_image(self):
        score = self.score
        if score == 0:
            return "0.jpg"
        if score == 67:
            return "67.jpg"
        if score <= 10:
            return "1-10.jpg"
        if score <= 20:
            return "11-20.jpg"
        if score <= 30:
            return "21-30.jpg"
        if score <= 40:
            return "31-40.jpg"
        if score <= 50:
            return "41-50.jpg"
        if score <= 60:
            return "51-60.jpg"
        if score <= 70:
            return "61-70.jpg"
        if score <= 80:
            return "71-80.jpg"
        if score <= 90:
            return "81-90.jpg"
        return "91-100.jpg"

    def get_grade(self):
        if self.score >= 90:
            return "Excellent!"
        if self.score >= 75:
            return "Good!"
        if self.score >= 50:
            return "Average"
        if self.score >= 25:
            return "Needs Improvement"
        return "Keep Practicing"