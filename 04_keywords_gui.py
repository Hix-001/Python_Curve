import keyword
import tkinter as tk
from tkinter import ttk

# 1. The Alphabetical Keyword Database
keyword_definitions = {
    "False": "Boolean value representing logical falsity.",
    "None": "A special constant representing the absence of a value or a null state.",
    "True": "Boolean value representing logical truth.",
    "and": "Logical AND operator; returns True if both expressions are true.",
    "as": "Used to create an alias (alternate name) when importing modules.",
    "assert": "Used for debugging; tests a condition and raises an error if it's False.",
    "async": "Declares a function as an asynchronous coroutine.",
    "await": "Suspends the execution of an async function until a result arrives.",
    "break": "Instantly terminates the current loop and jumps out of it.",
    "class": "Used to define a new user-defined object-oriented class.",
    "continue": "Skips the rest of the current loop iteration and moves to the next one.",
    "def": "Used to define a new function.",
    "del": "Deletes references to objects, variables, or list elements.",
    "elif": "Short for 'else if'; checks a condition if the previous 'if' failed.",
    "else": "Executes a block of code if none of the preceding conditions are met.",
    "except": "Catches and handles specific exceptions/errors raised in a try block.",
    "finally": "A block of code that always runs after try/except, no matter what.",
    "for": "Used to create a counting or iterative loop over a sequence.",
    "from": "Used to import specific parts or functions from a module.",
    "global": "Declares that a variable inside a function refers to a global variable.",
    "if": "Used to create a conditional statement to check a logical state.",
    "import": "Pulls external modules or libraries into the current script.",
    "in": "Checks if a value is present inside a sequence (like a list or string).",
    "is": "Tests if two variables point to the exact same object in memory.",
    "lambda": "Used to create short, anonymous, single-line functions.",
    "nonlocal": "Declares a variable inside a nested function belongs to the outer function.",
    "not": "Logical NOT operator; inverts a boolean value (True becomes False).",
    "or": "Logical OR operator; returns True if at least one expression is true.",
    "pass": "A null statement; acts as a placeholder where code is syntactically required.",
    "raise": "Forcibly triggers an exception or error manually.",
    "return": "Exits a function and passes a specified value back to the caller.",
    "try": "Starts a block of code to monitor for potential runtime errors.",
    "while": "Creates a loop that continues running as long as a condition stays True.",
    "with": "Simplifies exception handling by encapsulating clean-up tasks (e.g., closing files).",
    "yield": "Pauses a function and returns a generator value instead of exiting."
}

# 2. Initialize the main GUI window
root = tk.Tk()
root.title("Python Keywords Database")
root.geometry("700x500")
root.configure(bg="#0f172a") # Slate-dark premium background

# 3. Add a modern title label
title_label = tk.Label(
    root, 
    text="🐍 PYTHON KEYWORDS MATRIX", 
    font=("Helvetica", 16, "bold"), 
    fg="#06b6d4", # Cyan accent
    bg="#0f172a",
    pady=15
)
title_label.pack()

# 4. Create a styling container for the data grid (Treeview)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", 
                background="#1e293b", 
                foreground="#f8fafc", 
                fieldbackground="#1e293b",
                rowheight=30,
                font=("Helvetica", 11))
style.configure("Treeview.Heading", 
                background="#334155", 
                foreground="#06b6d4", 
                font=("Helvetica", 11, "bold"))

# 5. Build the Table Grid Layout
columns = ("keyword", "meaning")
table = ttk.Treeview(root, columns=columns, show="headings", style="Treeview")

table.heading("keyword", text="Keyword")
table.heading("meaning", text="Meaning / Use Case")

table.column("keyword", width=150, anchor="center")
table.column("meaning", width=500, anchor="w")

# 6. Inject the sorted system keywords directly into the UI rows
for kw in sorted(keyword.kwlist):
    definition = keyword_definitions.get(kw, "Reserved system keyword.")
    table.insert("", tk.END, values=(kw, definition))

# 7. Add a scrollbar so you can navigate easily
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

# Pack everything onto the UI layout
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(15, 0), pady=15)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 15), pady=15)

# Keep the window persistent on screen
root.mainloop()