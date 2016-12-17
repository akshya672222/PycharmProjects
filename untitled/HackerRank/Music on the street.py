n = int(input(''))
coordinates = input('').split()
distance_hours = input('').split()

m = int(distance_hours[0])
h_min = int(distance_hours[1])
h_max = int(distance_hours[2])

interval = int(coordinates[-1]) - int(coordinates[0])
remaining = m - interval

if remaining == (h_min*2):
    result = int(coordinates[0]) - h_min
elif remaining == (h_max*2):
    result = int(coordinates[0]) - h_max
else:
    if remaining < (h_min + h_max):
        result = int(coordinates[0]) - (remaining - h_min)
    else:
        result = int(coordinates[0]) - (remaining - h_max)
print(result)

