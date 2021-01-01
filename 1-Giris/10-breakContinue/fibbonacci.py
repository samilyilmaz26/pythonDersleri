max = int(input("Son sayi "))
birincisayi = 1

ikincisayi = 1

fibonacci = [birincisayi,ikincisayi]
for i in range(max):


    birincisayi,ikincisayi = ikincisayi,birincisayi+ ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)
