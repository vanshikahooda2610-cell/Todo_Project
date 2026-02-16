# 📝 Advanced To-Do List Application (Python CLI)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)


A command-line based To-Do List application built using Python.  
This project allows users to manage daily tasks efficiently with persistent storage using JSON.

## Project Overview

The To-Do List Application is a command-line based project developed using Python to help users manage their daily tasks efficiently. This application allows users to organize their work by adding, viewing, updating, and deleting tasks. It also supports task completion status, priority levels, and due dates, making it easier to track and manage responsibilities.

This project was developed as part of my internship at **CodeSoft** to strengthen my understanding of Python programming, file handling, and project structure.

---

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Set task priority (High / Medium / Low)
* Add optional due dates
* Data persistence using JSON (tasks are saved even after closing the program)
* Simple and user-friendly command-line interface

---

## How the Application Works

1. When the program starts, it loads existing tasks from a `tasks.json` file.
2. The user is presented with a menu to choose an action.
3. Based on the selected option, the user can:

   * Add a new task
   * View current tasks
   * Mark a task as completed
   * Delete a task
4. Every change is automatically saved to the JSON file.
5. When the program is reopened, all previously saved tasks are loaded.

---

## Project Structure

```
Todo_Project/
│
├── main.py              # User interface and menu handling
├── task_manager.py      # Task management logic (add, delete, update, save)
├── tasks.json           # Stores task data
├── README.md            # Project documentation
└── .gitignore           # Files ignored by Git
```

---

## Technologies Used

* Python
* JSON (for data storage)
* VS Code
* Git & GitHub

---

## Learning Outcomes

Through this project, I learned:

* Python fundamentals and modular programming
* File handling using JSON
* Error handling and input validation
* Working with Git and GitHub
* Structuring a real-world project

---

## Future Improvements

* Add a graphical user interface (GUI)
* Add task search and filtering options
* Add reminders or notifications
* Use a database like SQLite instead of JSON

---

## Author

Vanshika Hooda
Aspiring Cyber Security Engineer
