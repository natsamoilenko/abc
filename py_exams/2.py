
def  print_list(a):
    print(a[1:3])
    print(a[4:])
    print(a[:5])

    print(a[len(a)-1])
    print(a[-1])

def print_dict(d):
    print(d)
    print(d.keys())
    print(d.values())

    for k in d.keys():
        print(k)
        print(d[k])

    print(d['username'])


print_list([1,2,3,4,5,6,7,8,9])
print_list([1,2,3,4,7,44,3,2,8,9])
print_list([1,2,3,4,5,6])

print_dict({'username': 'samoilenko', 'password': '************'})