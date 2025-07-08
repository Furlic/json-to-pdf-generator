import json
import plotter
from fpdf import FPDF

json_path = "data/sales_report.json"
with open(json_path) as json_data:
    data = json.load(json_data)

#creating pdf
pdf = FPDF()
pdf.add_page()

#title
title = data["report_title"]
date = data["report_date"]
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, title, ln=True, align="C")
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, f"Date: {date}", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)

#monthly sales
monthly_sales = data["monthly_sales"]
plotter.plot_monthly_sales(monthly_sales, "output/monthly_sales.png")

#Category sales
category_sales = data["category_sales"]
plotter.plot_category_sales(category_sales, "output/category_sales_distribution.png")

#visualisation
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Visualizations", ln=True)
pdf.ln(5)

pdf.image("output/monthly_sales.png", x=10, w=180)
pdf.ln(10)

pdf.image("output/category_sales_distribution.png", x=10, w=180)
pdf.ln(10)

#summary
summary = data["summary"]
pdf.cell(200, 10, txt="Summary", ln=True)
for key, value in summary.items():
    label = key.replace("_", " ").title()
    pdf.cell(200, 10, txt=f"{label}: {value}", ln=True)

pdf.ln(10)
pdf.multi_cell(0, 8, f"Notes:{data["notes"]}")

#top products
pdf.add_page()
pdf.cell(0, 10, "Top Products", ln=True)
headers = ["Name", "Units Sold", "Revenue", "Unit Price"]
for header in headers:
    pdf.cell(48, 8, header, border=1)
pdf.ln()

for product in data["top_products"]:
    pdf.cell(48, 8, product["name"], border=1)
    pdf.cell(48, 8, str(product["units_sold"]), border=1)
    pdf.cell(48, 8, f"${product["revenue"]}", border=1)
    pdf.cell(48, 8, f"${product["unit_price"]}", border=1)
    pdf.ln()

pdf.output("output/report.pdf")