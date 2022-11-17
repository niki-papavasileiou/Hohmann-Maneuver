import math

m = 398000 
Rearth= 6371

Api = int(input("Initial Orbit's Apogee: \n"))
Pei = int(input("Initial orbit's Perigee: \n"))

Apf = int(input("Final Orbit's Apogee: \n"))
Pef = int(input("Final orbit's Perigee: \n"))



Ap1 = Api + Rearth
Pe1 = Pei + Rearth
isemimajor_axis = (Ap1 + Pe1)/2
print ("----------Initial orbit----------\n\n")
print (" semimajor axis:" ,isemimajor_axis, "km\n" )

iorbit_energy = -(m/(2*isemimajor_axis))
print (" orbit energy:" ,iorbit_energy, "MJ/kg\n")

ei = (Ap1 - Pe1)/(Ap1 + Pe1)
print (" eccentricity:",ei,"\n" )


Ap2 = Apf + Rearth
Pe2 = Pef + Rearth 

fsemimajor_axis = (Ap2 + Pe2)/2
print ("----------Final orbit----------\n\n")
print (" semimajor axis:" ,fsemimajor_axis, "km\n" )

forbit_energy = -(m/(2*fsemimajor_axis))
print (" orbit energy:" ,forbit_energy, "MJ/kg\n")

ef = (Ap2 - Pe2)/(Ap2 + Pe2)
print (" eccentricity:",ef,"\n" )



Ap = Ap2 
Pe = Pe1

tsemimajor_axis = (Ap + Pe)/2
print ("----------Transfer orbit----------\n\n")
print (" semimajor axis:" ,tsemimajor_axis, "km\n" )

torbit_energy = -(m/(2*tsemimajor_axis))
print (" orbit energy:" ,torbit_energy, "MJ/kg\n")

et = (Ap - Pe)/(Ap + Pe)
print (" eccentricity:",et,"\n" )



print ("----------Maneuver 1----------\n\n")

ispeed = math.sqrt(abs(2*((m/Pe1)+iorbit_energy)))
fspeed= math.sqrt(abs(2*((m/Pe)+torbit_energy)))
DVi = abs(fspeed-ispeed)

print("Initial speed: ",ispeed,"km/s\n")
print("Final speed: ",fspeed,"km/s\n")
print("DV: ",DVi,"km/s\n")



print ("----------Maneuver 2----------\n\n")

ispeed2 = math.sqrt(abs(2*((m/Ap)+torbit_energy)))
fspeed2 = math.sqrt(abs(2*((m/Ap)+forbit_energy)))
DVii = abs(fspeed2-ispeed2)

print("Initial speed: ",ispeed2,"km/s\n")
print("Final speed: ",fspeed2,"km/s\n")
print("DV: ",DVii,"km/s\n")



print ("----------TOTAL DV----------\n\n")
DV_total = DVi +DVii

print("Total DV:",DV_total, "km/s")



