import customtkinter as ctk

from interface import theme

class ResultsScreen(ctk.CTkFrame):
    def __init__(self, master, score):
        super().__init__(master, fg_color=theme.BACKGROUND)
        self.score = score
        self.create_ui()

    def create_ui(self):
        title = ctk.CTkLabel(self, text="Performance Result", font=theme.TITLE_FONT)
        title.pack(pady=40)
        score_label = ctk.CTkLabel(
            self,
            text=f"{self.score:.1f}",
            font=(theme.FONT_FAMILY, 100, "bold"),
            text_color=theme.ACCENT
        )
        score_label.pack()
        grade = self.get_grade()
        grade_label = ctk.CTkLabel(self, text=grade, font=theme.HEADING_FONT)
        grade_label.pack(pady=20)

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