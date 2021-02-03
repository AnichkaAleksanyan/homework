import modul

n=int(input("number: "))
print(modul.factorial(n))


r = float(input("r = "))
h = float(input("h = "))
valume = modul.valume_cylinder(r,h)
print(valume)

area = modul.area_cylinder(r,h)
print(area)



r = float(input("r = "))
print(modul.valume_sphere(r))
print(modul.area_sphere(r))
 


degree = float(input("degree: "))
print(modul.convert_degree_to_radian(degree))


x = int(input("number = "))
print(modul.primes_numbers(x))






