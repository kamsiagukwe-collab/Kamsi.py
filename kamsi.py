print("Choose a Formula: ")
print("1. Speed (v = d/t)")
print("2. Density (p = m /V)")
print("3. Pressure (p = F / A)")
print("4. Work (W = F * D)")
print("5. Power (P = W / t)")

x = int(input("Enter 1-5: "))

if x == 1:
    d = float(input("Distance (m): "))
    t = float(input("Time (s): "))
    v = d / t
    print("Speed=", v , "m/s")

elif x == 2:
    m = float(input("Mass (kg): "))
    v = float(input("Volume (m^3): "))
    density = m / v
    print("Density =", density, "kg/m^3")

elif x == 3:
    F = float(input("Force (N): "))
    A = float(input("Area (m^2): "))
    pressure = F / A
    print("Pressure =", pressure, "Pa")

elif x == 4:
    F = float(input("Force (N): "))
    d = float(input("Distance (m): "))
    work = F * d
    print("Work =", work, "J")

elif x == 5:
    W = float(input("Work (J): "))
    t = float(input("Time (s): "))
    power = W / t
    print("Power =", power, "W")

else:
    print("Invalid choice")