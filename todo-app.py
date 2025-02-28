todos = []
while True:
    userAction=input("Choose between add, show / display, edit, complete or exit: ").lower().strip()
    match userAction:
        case 'add':
            userAddition=input('Enter a todo: ').strip()
            todos.append(userAddition.capitalize())
            fileOverWrite=open('todo-app-storage.txt', 'w')
            fileOverWrite.writelines(todos)
            print('Successfully added!!')
        case 'show' | 'display':
            for index,todo in enumerate(todos):
                print(f'{index+1}. {todo.capitalize()}')
        case 'edit':
            userEdit=int(input('Enter the number you want edit: '))
            print(f'You are going to change {todos[userEdit - 1]}.')
            userNewTodo=input('What is your new todo?: ').strip()
            todos[userEdit-1]=userNewTodo
            print('Successfully edited!!')
        case 'complete':
            popNumber=int(input('Enter the number you completed: '))
            print(f'You completed: {todos.pop(popNumber-1)}')
            print('Successfully removed!!')
        case 'exit':
            break

print('Bye!')