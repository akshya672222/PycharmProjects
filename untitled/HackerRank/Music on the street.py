n = int(input(''))
coordinates = input('').split()
distance_hours = input('').split()

m = int(distance_hours[0])
h_min = int(distance_hours[1])
h_max = int(distance_hours[2])

interval = int(coordinates[-1]) - int(coordinates[0])
remaining = m - interval

remaining_max = remaining - h_max

result = int(coordinates[0]) - remaining_max

print(result)
