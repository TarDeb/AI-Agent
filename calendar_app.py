import tkinter as tk
import calendar
from datetime import datetime

class CalendarApp(tk.Tk):
    """Simple GUI app to display monthly calendars."""

    def __init__(self):
        super().__init__()
        self.title("Calendar App")
        self.geometry("260x240")

        # Controls for month and year selection
        now = datetime.now()
        self.month_var = tk.IntVar(value=now.month)
        self.year_var = tk.IntVar(value=now.year)

        month_spin = tk.Spinbox(self, from_=1, to=12, textvariable=self.month_var, width=5)
        year_spin = tk.Spinbox(self, from_=1900, to=2100, textvariable=self.year_var, width=5)
        show_button = tk.Button(self, text="Show Calendar", command=self.show_calendar)

        month_spin.pack(pady=5)
        year_spin.pack(pady=5)
        show_button.pack(pady=5)

        self.calendar_text = tk.Text(self, width=20, height=8)
        self.calendar_text.pack(padx=5, pady=5)

        self.show_calendar()

    def show_calendar(self):
        """Update the calendar display for the selected month/year."""
        month = self.month_var.get()
        year = self.year_var.get()
        cal_output = calendar.month(year, month)
        self.calendar_text.delete("1.0", tk.END)
        self.calendar_text.insert(tk.END, cal_output)


def main():
    app = CalendarApp()
    app.mainloop()


if __name__ == "__main__":
    main()
