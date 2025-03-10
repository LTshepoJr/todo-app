fileRead=open('Storage-Texts/todo-app-storage.txt', 'r')
fileReadLines=fileRead.readlines()
fileRead.close()
while True:
    userAction=input("Choose between add, show / display, edit, complete or exit: ").lower().strip()
    match userAction:
        case 'add':
            userAddition=input('Enter a todo: ').strip()
            fileReadLines.append(userAddition.capitalize()+'\n')
            fileOverWrite=open('Storage-Texts/todo-app-storage.txt', 'w')
            fileOverWrite.writelines(fileReadLines)
            fileOverWrite.close()
            print('Successfully added!!')
        case 'show' | 'display':
            for index,todo in enumerate(fileReadLines):
                print(f'{index+1}. {todo.capitalize()}')
        case 'edit': #crashes
            userEdit=int(input('Enter the number you want edit: '))
            print(f'You are going to change {todos[userEdit - 1]}.')
            userNewTodo=input('What is your new todo?: ').strip()
            todos[userEdit-1]=userNewTodo
            print('Successfully edited!!')
        case 'complete': #crashes
            popNumber=int(input('Enter the number you completed: '))
            print(f'You completed: {todos.pop(popNumber-1)}')
            print('Successfully removed!!')
        case 'exit':
            break

print('Bye!')