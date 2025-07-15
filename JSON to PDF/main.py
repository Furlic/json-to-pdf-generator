import json
import os

from analyzer import analyze_json_structure
from generator import generate_pdf

def main():
    json_path = "data/input.json"
    output_pdf = "output/report.pdf"
    config_path = "config/template_config.json"

    os.makedirs("output", exist_ok=True)
    os.makedirs("config", exist_ok=True)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    config = analyze_json_structure(data)

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    generate_pdf(data, config, output_pdf)

    print(f"PDF generated: {output_pdf}")

if __name__ == "__main__":
    main()
