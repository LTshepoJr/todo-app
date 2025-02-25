todos = []
while True:
    userAction=input("Choose between add, show / display, edit or exit: ").lower().strip()
    match userAction:
        case 'add':
            userAddition=input('Enter a todo: ').strip()
            todos.append(userAddition.capitalize())
        case 'show' | 'display':
            for index,todo in enumerate(todos):
                print(f'{index+1} {todo.capitalize()}')
        case 'edit':
            userEdit=int(input('Enter the number you want edit: '))
            print(f'You are going to change {todos[userEdit - 1]}.')
            userNewTodo=input('What is your new todo?: ').strip()
            todos[userEdit-1]=userNewTodo
        case 'exit':
            break

print('Bye!')