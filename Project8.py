task_names = []
task_time = []
task_is_done = []

def help():
  help_text = """
      Tasks:
      - add: Adds a new task.
      - remove: Removes a specified task.
      - edit: Edits a task by name.
      - search: Searches for a task.
      - display: Displays all tasks.
      - mark: Marks a task.
      - help: Displays this help text.
      - exit: Exits the program.
      """
  print(help_text)

def add(name):
    if name not in task_names:
      task_names.append(name)
      task_is_done.append(False)
      task_time.append(None)
      print("Added Successfully!")
    else:
      print(f"{name}:This Tasks Already Exists!")

def display():
  if len(task_names) == 0:
      print("Empty!")
  for i, p in enumerate(task_names):
    status_task = "Not Done"
    done = task_is_done[i]
    time = task_time[i]
    if done:
      status_task = "Done"
    print(f" {i+1}) Task: {p} ==> Status: {status_task}, Duration Time: {time} Hours")

def remove(name):
  if name in task_names:
    ind = task_names.index(name)
    task_names.pop(ind)
    task_is_done.pop(ind)
    task_time.pop(ind)
    print("Removed Succesfully!")
  else:
    print(f"{name}: Task Not Found!")

def edit(old_name):
  if old_name in task_names:
      new_name = input("Please Insert New Name: ") 
      if new_name not in task_names: 
        ind = task_names.index(old_name) 
        task_names[ind] = new_name 
        print("Edited!")
      else:
        print(f"{new_name} : This Task Already Exists!")
  else:
      print(f"{old_name}: This Task Not Found!")

def search(name):
  if name in task_names:
      ind = task_names.index(name)
      done = task_is_done[ind]
      time = task_time[ind]
      status_task="Not Done"
      if done:
        status_task="Done"
        print(f"{name} ==> Status: {status_task}, Duration: {time}")
  else:
      print(f"{name} : Task Not Found!")

def mark(name):
  if name in task_names:
      ind = task_names.index(name)
      if task_is_done[ind]:
        print("Task is already marked as done")
      else:
        start_time = input(f"Start time of {name} in the format HH:MM : ")
        end_time = input(f"End time of {name} in the format HH:MM :")
        start_time_parts = start_time.split(':')
        end_time_parts = end_time.split(':')

        start_hours = int(start_time_parts[0])
        start_minute = int(start_time_parts[1])
        
        end_hours = int(end_time_parts[0])
        end_minute = int(end_time_parts[1])

        duration_minutes = (end_hours*60 + end_minute) - (start_hours*60 + start_minute)
        duration_hours = duration_minutes // 60
        duration_minutes %= 60

        duration_str = f"{duration_hours:02d}:{duration_minutes:02d}"
        
        task_time[ind] = duration_str
        task_is_done[ind] = True
        print("Marked as Done!")
  else:
      print(f"{name}: Task Not Found!")

def details():
  total = len(task_names)
  totla_minutes = 0
  not_done = task_is_done.count(False)
  done = task_is_done.count(True)
  
  for duration in task_time:
      if duration:
        hours,minutes = duration.split(":")
        totla_minutes += int(hours) * 60 + int(minutes)
        hours_worked = totla_minutes / 60
  print(f"Total Tasks: {total}\nHours worked : {hours_worked}\nCompleted Tasks: {done}\nUncompleted Tasks: {not_done}")
      
      
for i in range(200):
  answer = input("help, add, display, remove, edit, search, mark, details, exit: ")
  if answer == "help":
    help()
  elif answer == "add":
    name = input("Insert Task Name: ")
    add(name)
  elif answer == "display":
    display()
  elif answer == "remove":
    name = input("Insert Task Name: ")
    remove(name)
  elif answer == "edit":
    old_name = input("Insert Task Name: ") 
    edit(old_name)
  elif answer == "search":
    name = input("Insert Task Name: ")
    search(name)
  elif answer == "mark":
    name = input("Insert Task Name: ")
    mark(name)
  elif answer == "details":
    details()
  elif answer == "":
    continue
  elif answer == "exit":
    break
  else:
    print(f"{answer}: Command Not Found!")
