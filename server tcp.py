import socket , threading , cmath
import symtable as sp     # import package sympy
server_socket =socket.socket()
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(10)
print('server is waiting client')
def first (values):
    res = - value[1] / value[0]
    return str(res)

def second (values):
    a = values[0]
    b = values[1]
    c = values[2]
    print("Equation")
    delta = (b**2) - (4*a*c)
    if delta ==0:
        res = -b / (2*a)
        res = "the one root is :"+str(res)
        return res
    else:
        res1 = str((-b + cmath.sqrt(delta)) / (2*a))
        res2 = str ((-b - cmath.sqrt(delta)) / (2*a))
        return ("the roots are:"+res1+","+res2)

def third (values):
        x = sp.symbol('x')
        f = values[0]*(x**3)+values[1]*(x**2)+values[2]*(x)+values[3]
        res = sp.solve(f)
        res = "the roots are :\n"+str(res[0])+"\n"+str(res[1])+"\n"+str(res[2])
        return res

def excute(cs , cadd):
        cs.send("enter the degree of equation:".encode())
        degree= cs.recv(2048).decode()
        if degree=='1':
            cs.send("equation (a*x+b)".encode())
            i = 0
            constants = ['a' , 'b']
            values = []
            while i <= int(degree):
                msg= 'enter' + constants[i] + ':'
                cs.send(msg.encode())
                var = cs.recv(2048).decode()
                values.append(int(var))
                i += 1
            cs.send('ok'.encode())
            res=first(values)
            res="The Result is: "+ res
            cs.send(res.encode())

        elif degree == '2':
            cs.send('equation (a*x^2 + b*x + c)'.encode())
            constants = ['a' , 'b' , 'c' ]
            values = []
            i=0
            while i <= int(degree):
                msg = 'enter' + constants[i] + ":"
                cs.send(msg.encode())
                var = cs.recv(2048).decode()
                values.append(int(var))
                i+=1
            cs.send('ok'.encode())
            res=second(values)
            cs.send(res.encode())
        elif degree =='3':
            cs.send('equation (a*x^3 + b*x^2 + c*x + d)'.encode())
            constants = ['a', 'b', 'c' , 'd']
            values = []
            i = 0
            while i <= int(degree):
                msg = 'enter' + constants[i] + ":"
                cs.send(msg.encode())
                var = cs.recv(2048).decode()
                values.append(int(var))
                i += 1
            cs.send('ok'.encode())
            res = third(values)
            cs.send(res.encode())
        else:
            cs.send("not exit".encode())
            cs.send("ok".encode())
            cs.send("no result".encode())

        cs.close()

while True:
         cs,cadd = server_socket.accept()
         cs.send("welcome to equation solver server".encode())
         print("new user is connected" , cadd)
         th = threading.thread(target= excute ,arg = (cs,cadd))
         th.start()

         


         
