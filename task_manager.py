import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()
        
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name,"r")as file:
                return json.load(file)
        return []
    
    def save_task(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)
            
    def add_task(self, title, priority, due_date):
        task = {
            "title" : title,
            "priority" : priority,
            "due_date" : due_date,
            "completed" : False,
            "created_at" : str(datetime.now())
            
        } 
        self.tasks.append(task)
        self.save_tasks()
        
    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
            return
        
        for index, task in enumerate(self.tasks):
            status ="\u2714" if task["completed"] else " "
            print(f"\nTask {index + 1}")
            print(f"Title: {task['title']}")  
            print(f"Priority: {task['priority']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Completed: [{status}]")
            
    def completed_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task number.")
            
    def delete_task(self, index):
        if 0<= index <len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Invalid task number.")                         
        
                      
        