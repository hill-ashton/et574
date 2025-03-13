#lab1_4.py – Ashton Hill
price, discountPercent, = 99.99, 25
markdown=(price*discountPercent)/100
price -= markdown
print(round(price,2))