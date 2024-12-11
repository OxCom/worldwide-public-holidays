from datetime import date
import holidays

country = 'DE'
year = '2024'

hList = holidays.country_holidays(country)

for date, name in sorted(hList)
    print(date, name)
