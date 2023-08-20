def pesquisa_binaria(data, target, low, high):
    mid = (low+high)//2
    print(mid)
    if low>high:
        return False
    if data[mid] == target:
        return True
    if data[mid]<target:
        pesquisa_binaria(data, target, mid+1, high)
    else:
        pesquisa_binaria(data, target, low, mid-1)
print(pesquisa_binaria([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],7 ,0, 15))

def reorganiza(data, target, low, high):
    if low>high:
        print(data)
        return data
    if data[low]>target:
        f = data.pop(low)
        data.append(f)
        reorganiza(data, target, low, high-1)
    else:
        reorganiza(data, target, low+1, high)
reorganiza([0,1,5,3,4,6],4,0,6)