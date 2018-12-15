# Student ID: 6110546640

###############################################################
# This count_pax() is for level 1.2
def count_pax(origin,destination):
    pax_origin = ["BKK","CNX","BKK","HKT","BKK","BKK","CNX","CNX","HKT","HKT","CNX","BKK","BKK","BKK","BKK","CNX","CNX"]
    pax_dest =   ["CNX","BKK","HKT","BKK","CNX","CNX","HKT","BKK","BKK","CNX","BKK","HKT","CNX","CNX","HKT","HKT","BKK"]
    result = []
    for i in range(len(pax_origin)):
        if pax_origin[i] == origin and pax_dest[i] == destination:
            result.append(i+1)
    return result

###############################################################
# Add your own code for level 1.1
cost = {
    'B200' : 18000,
    'C172' : 12000
}
revenue = {
    'B200' : {
        'CNX': 12000,
        'HKT': 15000
    },
    'C172' : {
        'CNX': 8000,
        'HKT': 10000
    }
}

def revenue_calculation(plane_type,dest,pax_no):
    result = (revenue[plane_type][dest] * pax_no)
    return result

while True:
    choice = input('(C)ost/ (R)evenue/ (Q)uit? ')
    if choice == 'C':
        plane_type = input('Plane type (B200/C172)? ') 
        print(f'Cost = {cost[plane_type]:.2f} Baht')
    elif choice == 'R':
        plane_type = input('Plane type (B200/C172)? ') 
        destination = input('Destination (CNX/HKT)? ')
        pax_no = int(input("Num pax? "))
        print(f'Revenue = {revenue_calculation(plane_type,destination,pax_no):.2f} Baht')
    elif choice == 'Q':
        break
    else:
        print("Please choose valid choice")
###############################################################
# Add your own code for level 1.2

origin = input('Origin? ')
destination = input('Destination? ')
result = count_pax(origin,destination)
print(f"Number of passengers from {origin} to {destination} = {len(result)}")
print("They are passengers with ID:",end='')
for i in result:
    print(f" {i},", end='')
print('')