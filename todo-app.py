countries = []
cities=[]
while True:
    userAction=input("Choose between show / display, add or exit: ").lower().strip()
    match userAction:
        case 'add':
            userChooses = input("Choose between country or city: ").lower().strip()
            match userChooses:
                case 'country':
                    country=input('Enter a country: ').strip()
                    countries.append(country.title())
                    print('You chose country')
                case 'city':
                    city = input('Enter a city: ').strip()
                    cities.append(city.title())
                    print('You chose city')
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
        case 'exit':
            break
print('Bye!')