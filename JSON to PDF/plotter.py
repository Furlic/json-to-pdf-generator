import matplotlib.pyplot as plt

def plot_monthly_sales(monthly_data, path):
    months = monthly_data.keys()
    values = monthly_data.values()

    plt.figure(figsize=(8, 5))
    plt.plot(months, values, marker='o', linestyle='-', color='royalblue')

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales (USD)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_category_sales(category_data, path):
    categories = category_data.keys()
    revenues = category_data.values()

    plt.figure(figsize=(6, 6))
    plt.pie(revenues, labels=categories, autopct='%1.1f%%', startangle=140)

    plt.title("Category Sales Distribution")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()