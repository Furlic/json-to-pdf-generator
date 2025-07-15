import matplotlib.pyplot as plt

def generate_line(title, data, path):
    x_values = data.keys()
    y_values = data.values()

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='royalblue')

    plt.title(title.replace("_", " ").title())
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def generate_pie(title, data, path):
    categories = data.keys()
    values = data.values()

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)

    plt.title(title.replace("_", " ").title())
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def generate_bar(title, data, path):
    categories = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color='seagreen')

    plt.title(title.replace("_", " ").title())
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.grid(axis="y")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()