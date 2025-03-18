fileRead=open('Storage-Texts/todo-app-storage.txt', 'r') # Opens the text file.
fileReadLines=fileRead.readlines() # This variable returns a list.
fileRead.close()
def fileOverWrite(): #This function updates the text file.
    fileOverWrite = open('Storage-Texts/todo-app-storage.txt', 'w')
    fileOverWrite.writelines(fileReadLines)
    fileOverWrite.close()
while True:
    userAction=input("Choose between add, show / display, edit, complete or exit: ").lower().strip()
    match userAction:
        case 'add': # Case for adding a to do.
            userAddition=input('Enter a todo: ').strip()
            fileReadLines.append(userAddition.capitalize()+'\n')
            fileOverWrite()
            print('Successfully added!!')
        case 'show' | 'display': # Case for showing a to do.
            for index,todo in enumerate(fileReadLines, 1):
                print(f'{index}. {todo.capitalize().strip('\n')}')
        case 'edit': # Case for editing a to do.
            userEdit=int(input('Enter the number you want edit: '))
            print(f'You are going to change {fileReadLines[userEdit - 1].strip('\n')}.')
            userNewTodo=input('What is your new todo?: ').strip()
            fileReadLines[userEdit-1]=userNewTodo
            fileOverWrite()
            print('Successfully edited!!')
        case 'complete': # Case for removing a to do.
            popNumber=int(input('Enter the number you completed: '))
            print(f'You completed: {fileReadLines.pop(popNumber-1)}')
            fileOverWrite()
            print('Successfully removed!!')
        case 'exit':
            break

print('Bye!')