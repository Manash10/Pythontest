name=input("Enter name: ")
cleaning=input("cleaned: ")
cavity=input("cavity: ")
xray=input("xray: ")

subtotal=0
if cleaning=="y":
    subtotal+=60
if cavity=="y":
    subtotal+=200
if xray=="y":
    subtotal+=100

#discount if applicable
if subtotal > 300:
    subtotal *=1 - 0.10
elif subtotal >200:
    subtotal*= 1- 0.05

total=subtotal+0.15*subtotal

print("Melanie Dental Clinic")
print("---------------------")
print(f"receipt for patient {name}")
print("---------------------")
print(f"Subtotal: {subtotal}")
print("tax: 15%")
print(f"total: {total}")