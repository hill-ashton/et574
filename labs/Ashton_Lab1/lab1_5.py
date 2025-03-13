#lab1_5.py – Ashton Hill
odo1,odo2,gallons=23456,23678,10
diff=(odo2-odo1)
mpg=(diff/10)
print("Distance Traveled: ",diff," Miles\nGallon Used: ",gallons," Gallons\nHow many miles per gallon did the car average between two fillings?\nAnswer: ",('%.3f'%mpg)," Miles/Gallon")