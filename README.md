# 📝 Console-Based To-Do List (Python)

A simple console-based To-Do List application written in Python.  
This app allows you to **add, remove, and view tasks**, while storing them in a text file so your tasks are saved between sessions.

---

## 📂 Project Structure
to-do-list/
│
├── tasks.txt # File where tasks are stored
├── todo.py # Main Python script
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Features
- View all tasks in your to-do list
- Add new tasks
- Remove tasks by number
- Tasks are stored in a `tasks.txt` file for persistence
- Lightweight and runs directly in the terminal

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/to-do-list.git
   cd to-do-list
Run the script:

bash
Copy code
python todo.py
📋 Usage
When you run the program, you’ll see a menu:

mathematica
Copy code
==== To-Do List Menu ====
1. View tasks
2. Add task
3. Remove task
4. Exit
Option 1 → View all tasks

Option 2 → Add a new task

Option 3 → Remove an existing task

Option 4 → Exit the program (tasks are auto-saved)

💾 Data Storage
All tasks are stored in tasks.txt.

On startup, tasks are loaded from this file.

On adding/removing tasks, the file is updated automatically.

🛠 Requirements
Python 3.x (no extra dependencies required)

📌 Example
pgsql
Copy code
==== To-Do List Menu ====
1. View tasks
2. Add task
3. Remove task
4. Exit
Choose an option (1-4): 2
Enter a new task: Finish homework
✔ Task 'Finish homework' added.
