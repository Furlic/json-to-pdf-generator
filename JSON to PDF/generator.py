from pdf_renderer import PDFReport
from plotter import generate_line, generate_pie, generate_bar


def generate_pdf(data, config, output_path):
    pdf = PDFReport()
    pdf.add_page()

    for key, value in data.items():
        settings = config.get(key, {"action": "skip"})
        action = settings.get("action", "skip")

        if action == "skip":
            continue

        elif action == "text":
            show_title = settings.get("show_title", "on")
            if show_title == "on":
                pdf.add_text(f"{key.replace("_", " ")}: {value}", style=settings.get("style", "normal_left"))
            else:
                pdf.add_text(value, style=settings.get("style", "normal_left"))

        elif action == "table":
            if isinstance(value, dict):
                pdf.add_table(value, title= settings.get("title"))
            else:
                print(f"Warning: 'table' action expected dict at '{key}', got {type(value).__name__}")

        elif action == "plot":
            plot_path = f"output/{key}.png"
            plot_type = settings.get("type", "line")
            title = settings.get("title", key)

            if plot_type == "line":
                generate_line(title, value, plot_path)
            elif plot_type == "pie":
                generate_pie(title, value, plot_path)
            elif plot_type == "bar":
                generate_bar(title, value, plot_path)
            else:
                print(f"Warning: Unknown plot type '{plot_type}' for '{key}'")
                continue

            pdf.add_image(plot_path)

        elif action == "list_table":
            pdf.add_list_table(value)

        elif action == "list":
            pdf.add_list(value)

        else:
            print(f"Warning: Unknown action '{action}' for key '{key}'")

    pdf.output(output_path)
