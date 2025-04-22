print("Tìm số palindrome lớn nhất được lập từ tích của hai số có n chữ số")
print("nhập n: ")
n=int(input())
s=[]
start=int(str(1)+((n-1)*str(0)))
end=int(n*str(9))
for i in range(start,end+1):
    for j in range(start,end+1):
        a= i*j
        b=str(a)
        if a==int(b[::-1]):
            s.append(a)
print("số palindrome lớn nhất là:",max(s))