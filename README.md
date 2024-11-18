# Task Manager CLI Application

## Description
A Python-based Command-Line Interface (CLI) application to manage tasks. Users can add tasks, view them, delete tasks, and mark them as completed. Tasks are stored in a `tasks.json` file for persistence. The application also includes a simple login system with dummy credentials for access control.

---

## Features
- **User Authentication**: Simple login using pre-defined credentials (`pyspiders@example.com` / `py@123`).
- **Add Tasks**: Add new tasks with a title.
- **View Tasks**: Display all tasks with their ID, title, and completion status.
- **Delete Tasks**: Remove tasks using their ID.
- **Mark Tasks as Complete**: Update the status of a task to "COMPLETED."
- **Persistent Storage**: Tasks are saved to a `tasks.json` file and loaded when the application starts.

---

## Usage Instructions

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run
1. Clone or download the project.
2. Navigate to the project directory.
3. Run the application using the command:
   ```bash
   python <task-manager>.py
