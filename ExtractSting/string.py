def func():
    string = ['p','a','r','a','l','l','e','l']
    x =(len(string))
    for i in range(x):
        n = i+1   
        for j in range(n,x):
            if string[i] == string[j] :
                return i
func()
