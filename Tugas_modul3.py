print("berikut adalah luas kurva f(x) = x^2 + 2x")
n=int(input("Masukkan nilai n :"))
a=1
b=3
dx=(b-a)/n
luas=0
for i in range(1,n+1):
    xi = a+i*dx
    fx = xi**2 + 2*xi
    luas += fx
luas *= dx
print(f"Luas derah dari fungsi x^2 + 2x dengan batas daerah x=1 dan x=3 dan jumlah partisi n={n} dengan luas daerah di bawah kurva :{luas}")