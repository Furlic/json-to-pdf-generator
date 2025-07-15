🧾 JSON to PDF Report Generator
This project allows you to interactively convert a JSON file into a nicely formatted PDF report, complete with text, tables, bullet lists, and charts. Ideal for dashboards, summaries, and auto-generated documentation.

📦 Features
📝 Text blocks with alignment & style options

📊 Plot types: line, bar, and pie (via matplotlib)

📋 Tables from dictionaries and structured lists

• Bullet lists from primitive arrays

👤 Fully interactive: user selects how to render each field

🧠 Saves a reusable config to template_config.json

⚙️ Implemented in pure Python using fpdf and matplotlib

🚀 How to Run
Install dependencies (if not already installed):

bash
Copy
Edit
pip install matplotlib fpdf
Put your JSON file at data/input.json.
Example:

json
Copy
Edit
{
  "report_title": "Sales Report Q2 2025",
  "report_date": "2025-07-06",
  "summary": {
    "Revenue": 150000,
    "Expenses": 90000,
    "Profit": 60000
  },
  "monthly_sales": {
    "April": 40000,
    "May": 50000,
    "June": 60000
  },
  "category_sales": {
    "Electronics": 80000,
    "Clothing": 40000,
    "Home": 30000
  },
  "top_products": [
    { "name": "Laptop", "units": 200, "revenue": 50000 },
    { "name": "Phone", "units": 300, "revenue": 45000 }
  ],
  "notes": "Sales increased slightly compared to Q1."
}
Run the main script:

bash
Copy
Edit
python main.py
Follow the interactive prompts
The tool will ask how to render each field (text, table, chart, etc.)

Your report will be saved to output/report.pdf

📁 Project Structure
graphql
Copy
Edit
.
├── analyzer.py           # Analyzes JSON and prompts for user input
├── generator.py          # Applies config to generate the final PDF
├── pdf_renderer.py       # Adds text, tables, images, lists via FPDF
├── plotter.py            # Handles matplotlib chart generation
├── main.py               # Entry point
├── data/
│   └── input.json        # Your input data
├── output/
│   └── report.pdf        # Generated PDF goes here
└── config/
    └── template_config.json  # Stores your render preferences
⚠️ Notes
The JSON file should be flat (single-level keys).

plot actions require numeric values (int or float).

list_table supports only lists of dicts with identical keys.

📜 License
MIT License — free to use, modify, and share.

