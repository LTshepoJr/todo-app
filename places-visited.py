def readFileText(place):
    with open(f'Storage-Texts/places-visited-{place}.txt',
              'r') as file:
        fileList=file.readlines()
        return fileList

def writeFileText(user, regionArray):
    with open('Storage-Texts/places-visited-'
              f'{'countries' if user=='country' else 'cities'}.txt',
              'w') as file:
        file.writelines(regionArray)

def userAdditionFunction(regionArray, userChoose):
    region = input(f'Enter a {userChoose}: ').strip()
    regionArray.append(region.title()+'\n')
    writeFileText(userChoose, regionArray)
    
def userEditFunction(regionArray, userEdit, number):
    print(f'You are going to change {regionArray[number - 1].strip('\n')}')
    newPlace = input(f'Enter new {userEdit}: ').title()
    regionArray[number - 1] = newPlace+'\n'
    writeFileText(userEdit, regionArray)
    
def userVisitFunction(regionArray, userVisit, number):
    print(f'You visited: {regionArray.pop(number - 1).strip('\n')}')
    writeFileText(userVisit, regionArray)
    
def userDisplayFunction(regionArray):
    for index, item in enumerate(regionArray):
        print(f'{index + 1}. {item.strip('\n')}')
        
def stripLineBreak(array):
    return [list.strip('\n') for list in array]

while True:
    
    userAction=input('Choose between add, show / display, edit, visited or exit: ').lower().strip()
    
    match userAction:
        case 'add':
            userAddition = input('Choose between country or city: ').lower().strip()
            match userAddition:
                case 'country':
                    userAdditionFunction(readFileText('countries'),
                                         userAddition)
                    print('Successfully added!!')
                case 'city':
                    userAdditionFunction(readFileText('cities'),
                                         userAddition)
                    print('Successfully added!!')

        case 'edit':
            userEdit=input('Edit country or city?: ').lower().strip()
            number=int(input('Enter a number: '))
            match userEdit:
                case 'city':
                    userEditFunction(readFileText('cities'),
                                     userEdit,
                                     number)
                    print('Successfully edited!!')
                case 'country':
                    userEditFunction(readFileText('countries'),
                                     userEdit,
                                     number)
                    print('Successfully edited!!')
            
        case 'visited':
            userVisit=input('Country or city visited?: ').lower().strip()
            number=int(input('Enter a number: '))
            match userVisit:
                case 'city':
                    userVisitFunction(readFileText('cities'),
                                      userVisit,
                                      number)
                    print('Successfully removed!!')
                case 'country':
                    userVisitFunction(readFileText('countries'),
                                      userVisit,
                                      number)
                    print('Successfully removed!!')

        case 'show' | 'display':
            userDisplay=input('Show country, city or both?: ').lower().strip()
            match userDisplay:
                case 'country':
                    userDisplayFunction(readFileText('countries'))
                case 'city':
                    userDisplayFunction(readFileText('cities'))
                case 'both':
                    print(f'Countries: {stripLineBreak(readFileText('countries'))}//',
                          f'//Cities: {stripLineBreak(readFileText('cities'))}')
            
        case 'exit':
            break

print('Bye!')