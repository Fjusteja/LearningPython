"BMI Calculator"
import time
print("Perhitungan BMI (Body Mass Index)")
print("---------------------------------")
BB = input("Masukan BB anda (Kilogram) : ")
BB = float(BB)
TB = input("Masukan TB anda (Meter) : ")
TB = float(TB)
print("---------------------------------")
BMI = BB/(TB**2)
print (f"BMI anda = {BMI:.2f} kg/m^2")
time.sleep(1)
print("BMI normal antara 18.5 - 25 kg/m^2")
time.sleep(1)
BBI = dict()
BBI['Min']=18.5*(TB**2)
BBI['Max']=25*(TB**2)

print(f"BB ideal anda antara "
      f"{BBI['Min']:.2f} dan {BBI['Max']:.2f} ")
time.sleep(1)
print("Terima Kasih ^_^b")
time.sleep(6)