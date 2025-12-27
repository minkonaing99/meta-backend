#global Scope
my_global = 10

def fn1():
    enclose_v = 8
    def fn2():
        local_v = 5
        print("Access to global ", my_global)
        print("Access to local ", local_v)
        print("Access to enclose ", enclose_v)
    fn2()

fn1()
print("Access to local ", local_v)
print("Access to enclose ", enclose_v)
    
    

print(local_v)