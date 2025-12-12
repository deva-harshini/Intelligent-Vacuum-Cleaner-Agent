import tkinter as tk
import time
import threading
import random

#                 VACUUM ENVIRONMENT CLASS
class VacuumEnvironment:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def randomize_grid(self):
        """Generates a random pattern of dirty and clean cells."""
        for r in range(self.size):
            for c in range(self.size):
                self.grid[r][c] = random.choice([0, 1])  # random clean or dirty

        # Ensure at least 1 dirty cell exists
        if all(self.grid[r][c] == 0 for r in range(self.size) for c in range(self.size)):
            rr = random.randint(0, self.size - 1)
            cc = random.randint(0, self.size - 1)
            self.grid[rr][cc] = 1

    def is_dirty(self, r, c):
        return self.grid[r][c] == 1

    def clean_cell(self, r, c):
        self.grid[r][c] = 0

    def all_clean(self):
        return all(self.grid[r][c] == 0 
                   for r in range(self.size) 
                   for c in range(self.size))


#                 GUI + AGENT CONTROLLER
class VacuumAgentGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Intelligent Vacuum Cleaner Agent - Advanced GUI")
        self.master.geometry("700x750")
        self.master.configure(bg="#ECECEC")

        self.size = 3
        self.cell_size = 150
        self.delay = 0.7
        self.running = False

        # Environment
        self.env = VacuumEnvironment(self.size)
        self.env.randomize_grid()

        # Agent position
        self.agent_pos = (0, 0)

        # GUI Layout
        self.create_widgets()
        self.draw_grid(initial=True)

    def create_widgets(self):

        # Title Label (OUTSIDE GRID)
        self.state_label = tk.Label(
            self.master, 
            text="INITIAL STATE DIAGRAM",
            font=("Arial", 20, "bold"),
            bg="#ECECEC"
        )
        self.state_label.pack(pady=10)

        # Canvas for grid display
        self.canvas = tk.Canvas(
            self.master, 
            width=self.size * self.cell_size,
            height=self.size * self.cell_size,
            bg="white",
            highlightthickness=2,
            highlightbackground="black"
        )
        self.canvas.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(self.master, bg="#ECECEC")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(
            btn_frame, text="START", font=("Arial", 14),
            bg="#4CAF50", fg="white",
            width=10, command=self.start_simulation)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(
            btn_frame, text="STOP", font=("Arial", 14),
            bg="#F44336", fg="white",
            width=10, command=self.stop_simulation)
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.reset_btn = tk.Button(
            btn_frame, text="RESET", font=("Arial", 14),
            bg="#2196F3", fg="white",
            width=10, command=self.reset_environment)
        self.reset_btn.grid(row=0, column=2, padx=10)

    #                GRID DRAWING FUNCTION
    def draw_grid(self, initial=False, final=False):
        self.canvas.delete("all")

        # Update label OUTSIDE the grid
        if initial:
            self.state_label.config(text="INITIAL STATE DIAGRAM")
        elif final:
            self.state_label.config(text="FINAL STATE DIAGRAM")
        else:
            self.state_label.config(text="")

        for r in range(self.size):
            for c in range(self.size):

                if final:
                    color = "#B6E2A1"      # light green final
                elif self.env.grid[r][c] == 1:
                    color = "#FF6B6B"      # red dirty
                else:
                    color = "#4CAF50"      # green clean

                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                self.canvas.create_rectangle(x1, y1, x2, y2,
                                             fill=color, outline="black", width=2)

        # Draw agent
        ar, ac = self.agent_pos
        ax1 = ac * self.cell_size + 40
        ay1 = ar * self.cell_size + 40
        ax2 = ax1 + 70
        ay2 = ay1 + 70
        self.canvas.create_oval(ax1, ay1, ax2, ay2, fill="#1E90FF")

        self.master.update()

    #                 BUTTON ACTION HANDLERS

    def start_simulation(self):
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self.run_agent)
            thread.start()

    def stop_simulation(self):
        self.running = False

    def reset_environment(self):
        self.running = False
        self.env = VacuumEnvironment(self.size)
        self.env.randomize_grid()   # NEW RANDOM GRID EACH TIME
        self.agent_pos = (0, 0)
        self.draw_grid(initial=True)

    #                 AGENT BEHAVIOR FUNCTIONS
    def move_agent(self, new_pos):
        if not self.running:
            return

        self.agent_pos = new_pos
        self.draw_grid()
        time.sleep(self.delay)

    def clean_current(self):
        r, c = self.agent_pos
        if self.env.is_dirty(r, c):
            self.env.clean_cell(r, c)
            self.draw_grid()
            time.sleep(self.delay)

    #                 MAIN INTELLIGENT CONTROL LOGIC

    def run_agent(self):
        self.draw_grid(initial=True)
        time.sleep(1)

        for r in range(self.size):

            cols = range(self.size) if r % 2 == 0 else reversed(range(self.size))

            for c in cols:

                if not self.running:
                    return

                self.move_agent((r, c))
                self.clean_current()

        self.draw_grid(final=True)


#                        RUN PROGRAM
if __name__ == "__main__":
    root = tk.Tk()
    app = VacuumAgentGUI(root)
    root.mainloop()

