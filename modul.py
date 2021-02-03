from math import pi


def factorial(num):
	res = 1
	for i in range(1,num+1):
		res*=i
	return res
	

def valume_cylinder(r,h):
	valume = pi*r**2*h
	return valume		


def area_cylinder(r,h):	
	area = 2*pi*r*h+2*pi*r**2
	return area 


def valume_sphere(r):
	valume = 4/3*pi*r**2
	return valume


def area_sphere(r):
	area = 4*pi*r**2
	return area	


def convert_degree_to_radian(degree):
	radian = degree/57.3
	return radian


def primes_numbers(x):

	for i in range(2,x):
		for j in range(2,i):
			if i%j == 0:
				break
		else:
			print(i)
