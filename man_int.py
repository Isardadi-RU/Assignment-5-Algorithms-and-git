# Ísar Daði Pálsson

# Það eru tvö gildi, value og max value. Value fær gildi í byrjun frá notanda og max_value fær 0 
# og á meðan value er hærra en 0, þá rennur það í gegnum while lykkju.
# þegar value er hærra en max value, þá verður max value jafnt og gildið fyrir value
# þannig að max value hækkar upp í value þegar það er hærra.

value = int(input("Input a value: "))
max_value = 0

while value > 0:
    value = int(input("Input a value: "))
    if value > max_value:
        max_value = value
print("The highest input was: ",max_value)