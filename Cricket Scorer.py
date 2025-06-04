import tkinter as tk
from tkinter import messagebox

class CricketScoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Scoreboard")

        # Initialize score variables
        self.team_name = tk.StringVar()
        self.runs = 0
        self.wickets = 0
        self.balls = 0
        self.overs = 0

        # Header
        tk.Label(root, text="🏏 Cricket Scoreboard", font=("Helvetica", 20, "bold")).pack(pady=10)

        # Team name entry
        tk.Label(root, text="Enter Team Name:", font=("Helvetica", 12)).pack()
        self.team_entry = tk.Entry(root, textvariable=self.team_name, font=("Helvetica", 12), justify='center')
        self.team_entry.pack(pady=5)

        # Display area
        self.score_display = tk.Label(root, text=self.get_score_text(), font=("Helvetica", 16), bg="#f0f0f0", relief="solid", width=40, height=5)
        self.score_display.pack(pady=15)

        # Run buttons
        run_frame = tk.Frame(root)
        run_frame.pack()
        for run in [0, 1, 2, 3, 4, 6]:
            btn = tk.Button(run_frame, text=f"{run} Run", font=("Helvetica", 12), width=8,
                            command=lambda r=run: self.add_runs(r))
            btn.pack(side='left', padx=5, pady=5)

        # Wicket button
        tk.Button(root, text="Wicket", font=("Helvetica", 12), bg="red", fg="white", width=10,
                  command=self.add_wicket).pack(pady=5)

        # Reset button
        tk.Button(root, text="Reset Match", font=("Helvetica", 12), bg="black", fg="white", width=15,
                  command=self.reset_match).pack(pady=10)

    def get_score_text(self):
        return (f"Team: {self.team_name.get() or '---'}\n"
                f"Score: {self.runs}/{self.wickets}\n"
                f"Overs: {self.overs}.{self.balls % 6}")

    def update_display(self):
        self.score_display.config(text=self.get_score_text())

    def add_runs(self, run):
        if self.wickets >= 10:
            messagebox.showinfo("Innings Over", "All wickets are down!")
            return

        self.runs += run
        self.balls += 1
        if self.balls % 6 == 0:
            self.overs += 1
        self.update_display()

    def add_wicket(self):
        if self.wickets >= 10:
            messagebox.showinfo("Innings Over", "All wickets are down!")
            return

        self.wickets += 1
        self.balls += 1
        if self.balls % 6 == 0:
            self.overs += 1
        self.update_display()

    def reset_match(self):
        confirm = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the match?")
        if confirm:
            self.runs = 0
            self.wickets = 0
            self.balls = 0
            self.overs = 0
            self.team_name.set("")
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = CricketScoreboard(root)
    root.mainloop()
