import tkinter as tk

# Grid settings
W, H = 5, 5
CELL_SIZE = 80

# Obstacles, Tasks, and Agent Position
obstacles = {(1, 1), (2, 4), (3, 4)}
tasks = {(0, 2), (2, 1), (3, 0)}
agent = [0, 0]

# Create the main window
root = tk.Tk()
root.title("Reflex Agent Grid (Tkinter)")

canvas = tk.Canvas(root, width=W*CELL_SIZE, height=H*CELL_SIZE + 120, bg="white")
canvas.pack()

# Draw the grid and items
def draw_grid():
    canvas.delete("all")

    # Draw grid cells
    for x in range(W):
        for y in range(H):
            x1 = x * CELL_SIZE
            y1 = y * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="gray", width=1)

            pos = (x, y)
            if pos in obstacles:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                canvas.create_text((x1+x2)//2, (y1+y2)//2, text="X", fill="white", font=("Arial", 24))
            elif pos in tasks:
                canvas.create_rectangle(x1, y1, x2, y2, fill="saddlebrown")
                canvas.create_text((x1+x2)//2, (y1+y2)//2, text="T", fill="white", font=("Arial", 24))
            elif pos == tuple(agent):
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                canvas.create_text((x1+x2)//2, (y1+y2)//2, text="A", fill="white", font=("Arial", 24))

    # Check win condition
    if not tasks:
        canvas.create_text(W * CELL_SIZE // 2, H * CELL_SIZE + 40,
                           text="All tasks done!", fill="green", font=("Arial", 20, "bold"))

# Validate agent move
def is_valid(x, y):
    return 0 <= x < W and 0 <= y < H and (x, y) not in obstacles

# Handle movement
def move(dx, dy):
    new_x = agent[0] + dx
    new_y = agent[1] + dy
    if is_valid(new_x, new_y):
        agent[0], agent[1] = new_x, new_y
        if tuple(agent) in tasks:
            tasks.remove(tuple(agent))
        draw_grid()

# Button controls
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_up = tk.Button(btn_frame, text="↑", width=4, height=2, command=lambda: move(0, -1))
btn_down = tk.Button(btn_frame, text="↓", width=4, height=2, command=lambda: move(0, 1))
btn_left = tk.Button(btn_frame, text="←", width=4, height=2, command=lambda: move(-1, 0))
btn_right = tk.Button(btn_frame, text="→", width=4, height=2, command=lambda: move(1, 0))

# Layout the buttons
btn_up.grid(row=0, column=1)
btn_left.grid(row=1, column=0)
btn_down.grid(row=1, column=1)
btn_right.grid(row=1, column=2)

# Initial draw
draw_grid()

# Start the GUI loop
root.mainloop()
