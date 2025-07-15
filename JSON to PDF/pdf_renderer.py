from fpdf import FPDF
import os

class PDFReport(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", size=12)

    def add_text(self, text, style):
        if "bold" in style:
            self.set_font("Arial", size=12, style="B")
        else:
            self.set_font("Arial", size=12, style="")

        align = "L"
        if "center" in style:
            align = "C"

        self.cell(0, 10, txt=text, ln=True, align=align)

    def add_list(self, items):
        self.set_font("Arial", size=12)
        for item in items:
            self.cell(5)
            self.cell(0, 10, f"• {item}", ln=True)

    def add_table(self, data_dict, title):
        self.cell(40, 10, txt=title.replace("_", " ").title(), ln=True)
        for key, value in data_dict.items():
            self.set_font("Arial", style="B")
            self.cell(40, 10, txt=key.replace("_", " ").title(), border=1)
            self.set_font("Arial", style="")
            self.cell(0, 10, txt=str(value), border=1, ln=True)
        self.ln()

    def add_list_table(self, items):
        if not items:
            return
        headers = items[0].keys()
        col_width = self.w / len(headers) - 10

        self.set_font("Arial", style="B")
        for header in headers:
            self.cell(col_width, 10, str(header.replace("_", " ").title()), 1)
        self.ln()

        self.set_font("Arial", style="")
        for row in items:
            for header in headers:
                self.cell(col_width, 10, str(row[header]), 1)
            self.ln()

    def add_image(self, image_path, width=150):
        if os.path.exists(image_path):
            self.image(image_path, w=width)
            self.ln(10)
