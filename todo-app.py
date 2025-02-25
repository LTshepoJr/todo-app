countries = []
cities=[]
while True:
    userAction=input("Choose between add, show / display, edit or exit: ").lower().strip()
    match userAction:
        case 'add':
            userChooses = input("Choose between country or city: ").lower().strip()
            match userChooses:
                case 'country':
                    country=input('Enter a country: ').strip()
                    countries.append(country.title())
                case 'city':
                    city = input('Enter a city: ').strip()
                    cities.append(city.title())
        case 'show' | 'display':
            userPlace=input("Show country, city or both?: ").lower().strip()
            match userPlace:
                case 'country':
                    for item in countries:
                        print(item)
                case 'city':
                    for item in cities:
                        print(item)
                case 'both':
                    print(countries, cities)
        case 'edit':
            userChoose=input('Edit country or city?:  ').lower().strip()
            number=int(input('Enter a number: '))
            match userChoose:
                case 'city':
                    print(f'You are going to change {cities[number-1]}')
                    newCity=input('Enter new city: ').title()
                    cities[number-1]=newCity
                case 'country':
                    print(f'You are going to change {countries[number-1]}')
                    newCountry = input('Enter new country: ').title()
                    countries[number - 1]=newCountry
        case 'exit':
            break

print('Bye!')