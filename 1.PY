# print("TO DO LIST")
# status=input("enter the status")
# if status=="completed":
#     add=input("what yo want to add")
#     if add>="a" and add<="z":
#         print("yo have completed your work",add)
# elif status=="incomplete":
#     print("you incomplete these type of work")
# elif status=="in-progress":
#     print("your progress work is")        
    



# print("TO DO TASKS")
# a=[]
# # user=input("how many tasks you want to do today")
# status=input("enter the status")
# if status=="completed":
#     add=input("what yo want to add")
#     if add>="a" and add<="z":
#         a.append(add)
#         print("you  have completed your work",a)
#         delete=input("do you want to delete somthing")
#         if delete=="yes":
#             a.pop(0)
#             print(a)       
# elif status=="incomplete":
#     print("you incomplete these type of work")
# elif status=="in-progress":
#     print("your progress work is")


# print("TO DO TASKS")
# print("1.completed")
# print("2.in-progress")
# print("3.incomplete")
# completed=[]
# in_progress=[]
# incompleted=[]
# i=0
# status=3
# status=int(input("enter the option:"))
# if status==1:
#     print("1.completed")
#     add=input("what you have completed: ")
#     if add>="a"and add<="z":
#         completed.append(add)
#         print(completed)            
# if status==2:
#     print("2.in-progress")
#     progress=input("what is your in_progress")
#     if progress>="a" and progress<="z":
#         in_progress.append(progress)
#         print(in_progress)    
# if status==3:
#     print("3.incomplete")
#     incomplete=input("eneter your incomplete work")
#     if incomplete>="a" and incomplete<="z":
#         incomplete.append(incompleted)
#         print(incompleted)




# def delete(task,status):
#     d=input("which task  u want to delete ")
#     i=0
#     while i<(len(task)):
#         task.pop(i)
#         print(task)
#         i+=1


    
task=[]
status=[]
user=int(input("enter the how many task you are doing"))
i=0
while i<user:
    t=input("enter the task")
    task.append(t)
    # print(task)
    s=input("enter the status")
    status.append(s)
    # print(status)
    i+=1
c=0
l=len(task)
l=len(status)
while c<l:
    print(task[c],"=",status[c])
    c+=1
user=input("what you want to do")
if user=="add":
    task1=input("enter the task u want to add")
    status2=input("enter the status u want to add")
    task.append(task1)
    status.append(status2)
c=0
l=len(task)
l=len(status)
while c<l:

    print(task[c],"=",status[c])
    c+=1
user1=input("what you want to do")
if user1=="remove":
    task3=input("which task u want to delete ")
    status3=input("which status u want to delete")
    task.remove(task3)
    status.remove(status3)
c=0
p=len(task)
p=len(status)
while c<p:
    print(task[c],"=",status[c])
    c+=1    

# user3=input("what u want to do")
# if user=="edit":
#     # task4=input("which task u want to delete ")
#     status4=input("which status u want to delete")
#     # task.remove(task4)
#     status.edit(status4)