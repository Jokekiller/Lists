#Harry Robinson
#19-12-2014
#Temperature list

weekly_temperature = []
for temperature in range(7):
    temperature = float(input("Enter the temperature: "))
    weekly_temperature.append(temperature)
average_temperature = (sum(weekly_temperature))/7
print("The average temperature this week is {0} degrees".format(average_temperature))

