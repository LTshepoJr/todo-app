def read_file_text(place):
    with open(f'Storage-Texts/places-visited-{place}.txt',
              'r') as file:
        file_list=file.readlines()
        return file_list

def write_file_text(user, region_array):
    with open('Storage-Texts/places-visited-'
              f'{'countries' 
              if user=='country'
              else 'cities'
              if user=='city'
              else ''}.txt',
              'w') as file:
        file.writelines(region_array)

def user_addition_function(region_array, user_choose):
    region = str(input(f'Enter a {user_choose}: ').strip())
    region_array.append(region.title() + '\n')
    write_file_text(user_choose, region_array)
    
def user_edit_function(region_array, user_edit, edit_number):
    print(f'You are going to change {region_array[edit_number - 1].strip('\n')}')
    new_place = input(f'Enter new {user_edit}: ').title()
    region_array[number - 1] = new_place + '\n'
    write_file_text(user_edit, region_array)
    
def user_visit_function(region_array, user_visit, visit_number):
    print(f'You visited: {region_array.pop(visit_number - 1).strip('\n')}')
    write_file_text(user_visit, region_array)
    
def user_display_function(region_array):
    for index, item in enumerate(region_array):
        print(f'{index + 1}. {item.strip('\n')}')
        
def strip_line_break(array):
    return [LIST.strip('\n') for LIST in array]

while True:
    
    userAction=input(
'''Choose between add, show / display, edit, visited or exit.
(You can include city or country): ''').lower().strip()
    
    if ' ' in userAction:
        userChooses=userAction.split()[0].lower()
        userPlace=userAction.split()[1].lower()
        if userPlace=='country' or 'cities':
            if userChooses=='add':
                user_addition_function(read_file_text(f'countries'
                                                    if userPlace=='country'
                                                    else 'cities' 
                                                    if userPlace=='city' 
                                                    else ''),
                                       userPlace)
                print('Successfully added!!')
            elif userChooses=='edit':
                number=int(input('Enter a number: '))
                user_edit_function(read_file_text(f'countries'
                                                    if userPlace=='country'
                                                    else 'cities' 
                                                    if userPlace=='city' 
                                                    else ''),
                                   userPlace,
                                   number)
                print('Successfully edited!!')
            elif userChooses=='visited':
                number=int(input('Enter a number: '))
                user_visit_function(read_file_text(f'countries'
                                                    if userPlace=='country'
                                                    else 'cities' 
                                                    if userPlace=='city' 
                                                    else ''),
                                    userPlace,
                                    number)
                print('Successfully removed!!')
            elif userChooses=='show' or 'display':
                if userAction.split()[1]!='both':
                    user_display_function(read_file_text(f'countries'
                                                    if userPlace=='country'
                                                    else 'cities' 
                                                    if userPlace=='city' 
                                                    else ''))
                else:
                    print(f'Countries: {strip_line_break(read_file_text('countries'))}//',
                            f'//Cities: {strip_line_break(read_file_text('cities'))}')
    else:
        match userAction:
            case 'add':
                userAddition = input('Choose between country or city: ').lower().strip()
                match userAddition:
                    case 'country':
                        user_addition_function(read_file_text('countries'),
                                               userAddition)
                        print('Successfully added!!')
                    case 'city':
                        user_addition_function(read_file_text('cities'),
                                               userAddition)
                        print('Successfully added!!')

            case 'edit':
                userEdit=input('Edit country or city?: ').lower().strip()
                number=int(input('Enter a number: '))
                match userEdit:
                    case 'city':
                        user_edit_function(read_file_text('cities'),
                                           userEdit,
                                           number)
                        print('Successfully edited!!')
                    case 'country':
                        user_edit_function(read_file_text('countries'),
                                           userEdit,
                                           number)
                        print('Successfully edited!!')
                
            case 'visited':
                userVisit=input('Country or city visited?: ').lower().strip()
                number=int(input('Enter a number: '))
                match userVisit:
                    case 'city':
                        user_visit_function(read_file_text('cities'),
                                            userVisit,
                                            number)
                        print('Successfully removed!!')
                    case 'country':
                        user_visit_function(read_file_text('countries'),
                                            userVisit,
                                            number)
                        print('Successfully removed!!')

            case 'show' | 'display':
                userDisplay=input('Show country, city or both?: ').lower().strip()
                match userDisplay:
                    case 'country':
                        user_display_function(read_file_text('countries'))
                    case 'city':
                        user_display_function(read_file_text('cities'))
                    case 'both':
                        print(f'Countries: {strip_line_break(read_file_text('countries'))}//',
                            f'//Cities: {strip_line_break(read_file_text('cities'))}')
                
            case 'exit':
                break

print('Bye!')