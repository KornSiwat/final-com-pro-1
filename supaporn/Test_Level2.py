from Pax import *
from Airport import *
from Plane import *

# StudentID
# Name

def test_level2_more(bkk, cnx, hkt, plane_1, plane_2):

    print("######### Test more ###########")

    pax13 = Pax(13, "BKK", "HKT", 16, 17)
    pax14 = Pax(14, "BKK", "CNX", 17, 18)
    pax15 = Pax(15, "BKK", "HKT", 16, 17)
    pax16 = Pax(16, "BKK", "CNX", 17, 18)
    pax17 = Pax(17, "BKK", "HKT", 16, 17)
    pax18 = Pax(18, "BKK", "CNX", 17, 18)
    bkk.add_pax(pax13)
    bkk.add_pax(pax14)
    bkk.add_pax(pax15)
    bkk.add_pax(pax16)
    bkk.add_pax(pax17)
    bkk.add_pax(pax18)
    
    pax19 = Pax(19, "CNX", "BKK", 20, 21)
    pax20 = Pax(20, "HKT", "BKK", 21, 22)
    pax21 = Pax(21, "HKT", "BKK", 21, 22)
    pax22 = Pax(22, "CNX", "BKK", 20, 21)
    pax23 = Pax(23, "HKT", "BKK", 21, 22)
    cnx.add_pax(pax19)
    hkt.add_pax(pax20)
    hkt.add_pax(pax21)
    cnx.add_pax(pax22)
    hkt.add_pax(pax23)

    print("===============================")
    print(">>> Airports")
    print(bkk)
    print()
    print(cnx)
    print()
    print(hkt)
    
    print("===============================")
    print(">>> Schedule")
    plane_1.schedule(bkk,hkt,16,17)
    print(plane_1)

    print(">>> Schedule")
    plane_2.schedule(bkk,cnx,17,18)
    print(plane_2)

    print("============= 16:00 ===========")
    print(">>> Depart")
    plane_1.depart()
    print(plane_1)
    print(bkk)

    print()
    print(">>> Arrive")
    plane_1.arrive()
    print(plane_1)
    print(hkt)

    print()
    print(">>> Schedule")
    plane_1.schedule(hkt,bkk,21,22)
    print(plane_1)

    print("============ 17:00 ============")
    print(">>> Depart")
    plane_2.depart()
    print(plane_2)
    print(bkk)

    print()
    print(">>> Arrive")
    plane_2.arrive()
    print(plane_2)
    print(cnx)

    print()
    print(">>> Schedule")
    plane_2.schedule(cnx,bkk,20,21)
    print(plane_2)

    print("============ 20:00 ============")
    print(">>> Depart")
    plane_2.depart()
    print(plane_2)
    print(cnx)

    print()
    print(">>> Arrive")
    plane_2.arrive()
    print(plane_2)
    print(bkk)

    print("============ 21:00 ============")
    print(">>> Depart")
    plane_1.depart()
    print(plane_1)
    print(hkt)

    print()
    print(">>> Arrive")
    plane_1.arrive()
    print(plane_1)
    print(bkk)

    print("###############################")

def test_level3(plane_1, plane_2):
    print("-------- Cost -------")
    print(" >>> Plane 1  ")
    print(plane_1.get_num_pax_list())
    result = plane_1.compute_cost()
    print(f"Cost = {result:.2f} Baht")
    print(" >>> Plane 2  ")
    print(plane_2.get_num_pax_list())
    result = plane_2.compute_cost()
    print(f"Cost = {result:.2f} Baht")

    print("------ Revenue ------")
    print(" >>> Plane 1  ")
    print(plane_1.get_num_pax_list())
    print(plane_1.get_flight_list())
    revenue_list = plane_1.compute_revenue()
    print(revenue_list)
    print(f"Revenue = {sum(revenue_list):.2f} Baht")
    print(" >>> Plane 2  ")
    print(plane_2.get_num_pax_list())
    print(plane_2.get_flight_list())
    revenue_list = plane_2.compute_revenue()
    print(revenue_list)
    print(f"Revenue = {sum(revenue_list):.2f} Baht")
    print("---------------------")


#####################################

bkk = Airport("BKK", 2)
cnx = Airport("CNX", 0)
hkt = Airport("HKT", 0)

pax1 = Pax(1, "BKK", "CNX", 8, 9)
pax2 = Pax(2, "BKK", "CNX", 8, 9)
pax3 = Pax(3, "BKK", "CNX", 8, 9)
pax4 = Pax(4, "BKK", "CNX", 8, 9)
bkk.add_pax(pax1)
bkk.add_pax(pax2)
bkk.add_pax(pax3)
bkk.add_pax(pax4)

pax5 = Pax(5, "BKK", "HKT", 9, 10)
pax6 = Pax(6, "BKK", "HKT", 9, 10)
pax7 = Pax(7, "BKK", "HKT", 9, 10)
bkk.add_pax(pax5)
bkk.add_pax(pax6)
bkk.add_pax(pax7)

pax8 = Pax(8, "CNX", "BKK", 11, 12)
pax9 = Pax(9, "CNX", "BKK", 11, 12)
pax10 = Pax(10, "CNX", "BKK", 11, 12)
cnx.add_pax(pax8)
cnx.add_pax(pax9)
cnx.add_pax(pax10)

pax11 = Pax(11, "HKT", "BKK", 12, 13)
pax12 = Pax(12, "HKT", "BKK", 12, 13)
hkt.add_pax(pax11)
hkt.add_pax(pax12)

#####################################
print("============================")

plane_1 = Plane("C172", 1)
plane_2 = Plane("B200", 2)

print(">>> Schedule")
plane_1.schedule(bkk,cnx,8,9)
plane_2.schedule(bkk,hkt,9,10)
print(plane_1)
print(plane_2)

print("=========== 8:00 ===========")
print(">>> Depart")
plane_1.depart()
print(plane_1)
print(bkk)

print()
print(">>> Arrive")
plane_1.arrive()
print(plane_1)
print(cnx)

print()
print(">>> Schedule")
plane_1.schedule(cnx,bkk,11,12)
print(plane_1)

print("=========== 9:00 ===========")

print(">>> Depart")
plane_2.depart()
print(plane_2)
print(bkk)

print()
print(">>> Arrive")
plane_2.arrive()
print(plane_2)
print(hkt)

print()
print(">>> Schedule")
plane_2.schedule(hkt,bkk,12,13)
print(plane_2)

print("========== 11:00 ===========")

print(">>> Depart")
plane_1.depart()
print(plane_1)
print(cnx)

print()
print(">>> Arrive")
plane_1.arrive()
print(plane_1)
print(bkk)

print("========== 12:00 ===========")

print(">>> Depart")
plane_2.depart()
print(plane_2)
print(hkt)

print()
print(">>> Arrive")
plane_2.arrive()
print(plane_2)
print(bkk)

#####################################
# Uncomment this part if you want more output to test for Level 2

# print("===============================")
# test_level2_more(bkk, cnx, hkt, plane_1, plane_2)
# print("===============================")

#####################################
# Uncomment this part if you want to test Level 3

# print("===============================")
# test_level3(plane_1, plane_2)
# print("===============================")

#####################################


