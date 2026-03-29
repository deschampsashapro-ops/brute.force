import tkinter as tk
import matplotlib.pyplot as plt
from cs_stats import get_cs2_stats, extract_main_stats, API_KEY

def show_graph(kills, deaths):
    labels = ["Kills", "Deaths"]
    values = [kills, deaths]

    plt.bar(labels, values)
    plt.title("Kills vs Deaths")
    plt.show()

def fetch_stats():
    steam_id = entry.get()
    data = get_cs2_stats(API_KEY, steam_id)
    kills, deaths, kd, hs = extract_main_stats(data)

    result_label.config(
        text=f"Kills: {kills}\nDeaths: {deaths}\nK/D: {kd}\nHS%: {hs}"
    )

    show_graph(kills, deaths)

root = tk.Tk()
root.title("CS2 Stats Analyzer")
root.geometry("400x300")

tk.Label(root, text="Enter Steam ID64:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Get Stats", command=fetch_stats).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()