countries = []
cities=[]
while True:
    userAction=input("Choose between show, add or exit: ").lower()
    match userAction:
        case 'add':
            userChooses = input("Choose between country or city: ").lower()
            match userChooses:
                case 'country':
                    country=input('Enter a country: ')
                    countries.append(country.title())
                    print('You chose country')
                case 'city':
                    city = input('Enter a city: ')
                    cities.append(city.title())
                    print('You chose city')
        case 'show':
            userPlace=input("Show country, city or both?: ").lower()
            match userPlace:
                case 'country':
                    print(countries)
                case 'city':
                    print(cities)
                case 'both':
                    print(countries, cities)
        case 'exit':
            break
print('Bye!')