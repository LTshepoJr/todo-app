countries = []
cities=[]
def userAdditionFunction(userChoose, regionArray):
    region = input(f'Enter a {userChoose}: ').strip()
    return regionArray.append(region.title())
def userDisplayFunction(regionArray):
    for index, item in enumerate(regionArray):
        print(f'{index + 1}. {item}')
def userEditFunction(number, regionArray, userEdit):
    print(f'You are going to change {regionArray[number - 1]}')
    newCity = input(f'Enter new {userEdit}: ').title()
    regionArray[number - 1] = newCity
def userVisitFunction(regionArray, number):
    print(f'You have visited: {regionArray.pop(number - 1)}')
while True:
    userAction=input("Choose between add, show / display, edit, visited or exit: ").lower().strip()
    match userAction:
        case 'add':
            userAddition = input("Choose between country or city: ").lower().strip()
            match userAddition:
                case 'country':
                    userAdditionFunction(userAddition, countries)
                case 'city':
                    userAdditionFunction(userAddition, cities)
            print('Successfully added!!')
        case 'show' | 'display':
            userDisplay=input("Show country, city or both?: ").lower().strip()
            match userDisplay:
                case 'country':
                    userDisplayFunction(countries)
                case 'city':
                    userDisplayFunction(cities)
                case 'both':
                    print(f'Countries: {countries}//', f'//Cities: {cities}')
        case 'edit':
            userEdit=input('Edit country or city?: ').lower().strip()
            number=int(input('Enter a number: '))
            match userEdit:
                case 'city':
                    userEditFunction(number, cities, userEdit)
                case 'country':
                    userEditFunction(number, countries, userEdit)
            print('Successfully edited!!')
        case 'visited':
            userVisit=input('Country or city visited?: ').lower().strip()
            number=int(input('Enter a number: '))
            match userVisit:
                case 'city':
                    userVisitFunction(cities, number)
                case 'country':
                    userVisitFunction(countries, number)
            print('Successfully removed!!')
        case 'exit':
            break

print('Bye!')