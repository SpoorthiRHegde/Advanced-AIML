from tabulate import tabulate
data = [
    ["SE", 10],
    ["NLP", 10],
    ["IPCV", 10],
    ["BIG DATA", 10],
    ["ROBOTICS", 10],
    ["IPCV LAB", 10],
    ["BLENDER", 10],
    ["PROJECT LAB", 10]
]
headers = ["sub", "marks"]
print(tabulate(data, headers=headers, tablefmt="grid"))
