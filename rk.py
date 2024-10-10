y_0 = 1
h = 0.1
t = 0
v_0 = 10
g = 9.8

def f(t):
    return v_0 - g * t

y = [y_0]

while t < 1:
    K_1 = h*f(t)
    K_2 = h*f(t+0.5*h)
    K_3 = h*f(t+0.5*h)
    K_4 = h*f(t+h)

    y_next = y[-1] + 1/6*(K_1 + 2*(K_2+K_3) + K_4)
    print(y_next)
    t += h

    #print("t =", t, "; y =", y_next)
    
print("Max y =", y_0 + 0.5*v_0**2/g, "; at t =", v_0/g)