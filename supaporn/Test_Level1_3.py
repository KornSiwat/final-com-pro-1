from Pax import *
from Airport import *

# StudentID
# Test_Level1_3

pax1 = Pax(1, "BKK", "CNX", 8, 9)
pax5 = Pax(5, "BKK", "HKT", 9, 10)
print(pax1)
print(pax5)

######################################

bkk = Airport("BKK", 2)
cnx = Airport("CNX", 0)
hkt = Airport("HKT", 0)
print(bkk)

pax1 = Pax(1, "BKK", "CNX", 8, 9)
bkk.add_pax(pax1)
print(bkk)

pax2 = Pax(2, "BKK", "CNX", 8, 9)
bkk.add_pax(pax2)
print(bkk)

pax3 = Pax(3, "BKK", "CNX", 8, 9)
pax4 = Pax(4, "BKK", "CNX", 8, 9)
pax5 = Pax(5, "BKK", "HKT", 9, 10)
pax6 = Pax(6, "BKK", "HKT", 9, 10)
pax7 = Pax(7, "BKK", "HKT", 9, 10)
bkk.add_pax(pax3)
bkk.add_pax(pax4)
bkk.add_pax(pax5)
bkk.add_pax(pax6)
bkk.add_pax(pax7)

print(bkk)

### **** Fill your own code here ****
num_cnx = bkk.count_out_pax('CNX')
num_hkt = bkk.count_out_pax('HKT')
print(f"There are {num_cnx} passengers going to CNX")
### **** Fill your own code here ****
print(f"There are {num_hkt} passengers going to HKT")

######################################

pax8 = Pax(8, "CNX", "BKK", 11, 12)
pax9 = Pax(9, "CNX", "BKK", 11, 12)
pax10 = Pax(10, "CNX", "BKK", 11, 12)
cnx.add_pax(pax8)
cnx.add_pax(pax9)
cnx.add_pax(pax10)

print(cnx)

### **** Fill your own code here ****
num_bkk = cnx.count_out_pax('BKK')
print(f"There are {num_bkk} passengers going to BKK")

######################################

pax11 = Pax(11, "HKT", "BKK", 12, 13)
pax12 = Pax(12, "HKT", "BKK", 12, 13)
hkt.add_pax(pax11)
hkt.add_pax(pax12)

print(hkt)

### **** Fill your own code here ****
num_bkk = hkt.count_out_pax('BKK')
print(f"There are {num_bkk} passengers going to BKK")

######################################


