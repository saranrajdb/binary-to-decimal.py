def decimalToBinary(n): 
    if(n >=1): 
        decimalToBinary(n//2) 
    print(n%2, end='')
decimalToBinary(5)

print()

m=4
print(bin(m).replace("0b",""))

k='1000'
print(int(k,2))


