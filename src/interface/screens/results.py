import customtkinter as ctk
from pathlib import Path
from PIL import Image

from interface import theme
from core.scorer import calculate_pitch_score, calculate_timing_score, calculate_loudness_score


class ResultScreen(ctk.CTkFrame):
    def __init__(self, master, result):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.result = result
        self.score = int(result["score"])
        self.create_ui()

    def create_ui(self):
        score_label = ctk.CTkLabel(self, text=str(self.score), font=(theme.FONT_FAMILY, 100, "bold"), text_color=theme.ACCENT)
        score_label.pack()
        image_path = Path("assets/ui/grades") / self.get_result_image()
        if image_path.exists():
            image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(250, 250))
            image_label = ctk.CTkLabel(self, image=image, text="")
            image_label.image = image
            image_label.pack(pady=20)
        breakdown = self.calculate_breakdown()
        breakdown_label = ctk.CTkLabel(
            self,
            text=(
                f"Pitch Accuracy:    {breakdown['pitch']}\n"
                f"Timing Accuracy:   {breakdown['timing']}\n"
                f"Loudness Accuracy: {breakdown['loudness']}"
            ),
            font=theme.BODY_FONT,
            justify="left"
        )
        breakdown_label.pack(pady=20)
        grade_label = ctk.CTkLabel(self, text=self.get_grade(), font=theme.HEADING_FONT)
        grade_label.pack()
        back_button = ctk.CTkButton(
            self,
            text="Return",
            width=200,
            height=50,
            font=theme.HEADING_FONT,
            fg_color=theme.PRIMARY,
            hover_color=theme.ACCENT,
            command=self.back_home
        )
        back_button.pack(pady=30)

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
        pitch = sum(calculate_pitch_score(match) for match in matches)
        timing = sum(calculate_timing_score(match) for match in matches)
        loudness = sum(calculate_loudness_score(match) for match in matches)
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
        elif self.score >= 75:
            return "Good!"
        elif self.score >= 50:
            return "Average"
        elif self.score >= 25:
            return "Needs Improvement"
        return "Keep Practicing"