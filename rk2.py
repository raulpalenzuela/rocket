y_0 = 1
v_0 = 10
g = 9.8
h = 0.1
t = 0

y = [y_0]
v = [v_0]

while t < 1:
    # Compute K values for position y and velocity v
    K1_y = h * v[-1]
    K1_v = h * (-g)

    K2_y = h * (v[-1] + 0.5 * K1_v)
    K2_v = h * (-g)

    K3_y = h * (v[-1] + 0.5 * K2_v)
    K3_v = h * (-g)

    K4_y = h * (v[-1] + K3_v)
    K4_v = h * (-g)

    # Update y and v
    y_next = y[-1] + (K1_y + 2*(K2_y + K3_y) + K4_y) / 6
    v_next = v[-1] + (K1_v + 2*(K2_v + K3_v) + K4_v) / 6
    print(y_next)

    y.append(y_next)
    v.append(v_next)

    t += h

    #print("t =", t, "; y =", y_next, "; v =", v_next)

# Theoretical results
#print("Max y =", y_0 + 0.5 * v_0**2 / g, "; at t =", v_0 / g)
