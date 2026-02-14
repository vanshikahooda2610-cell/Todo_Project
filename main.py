from task_manager import TaskManager


def main():
    manager = TaskManager()
    
    
    while True:
        print("===== ADVANCED TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Completed Task")
        print("4. Delete Task")
        print("5. Exit")
                                                                                                                                                                                                                                            
        choice = input ("Choose option (1-5): ")
        
        if choice == "1":
            manager.view_tasks()
            
        elif choice == "2":
            title = input("Enter task title: ")
            priority = input("Enter priority (Low/Medium/High): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(title, priority, due_date)
            print("Task added successfully!\n")  
            
        elif choice == "3":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                manager.complete_task(index)
                print("Task marked as completed!\n")
            except ValueError:
                print("Please enter a valid number.\n")
                
        elif choice == "4":
             manager.view_tasks()
             try:
                 index = int (input("Enter task number to delete: ")) - 1
                 manager.delete_task(index)
                 print("Task delete successfully!\n")
             except ValueError: 
                 print("Please enter a valid number.\n")
                 
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.\n")
            
            
if __name__ == "__main__":
    main()
                 
            
                      
            