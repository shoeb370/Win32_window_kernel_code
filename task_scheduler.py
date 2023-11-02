#This code is related to get the status related to the task scheduler
# importing packages
import win32com.client

#method to get the status  of the task
def list_tasks(task_name):
    scheduler = win32com.client.Dispatch("Schedule.Service") # calling Scheduler services # creating instance of scheduler sevices
    scheduler.Connect() #Connecting the schdeuler
    folder = scheduler.GetFolder("\\")  # Root folder

    for task in folder.GetTasks(0):
        # print(task) # this task variable contains the status and details of every task mentioned in the task scheduler
        if task.Name == task_name: return task.State
        

# List all tasks in the root folder
task_name = "Name on taks scheduler"
task_status = list_tasks(task_name) # calling functions


if task_status == 4: # checking the status is running or not 
    print(f"The task '{task_name}' is running.")
else:
    print(f"The task '{task_name}' is not running.")
