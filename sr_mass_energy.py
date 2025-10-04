from relativity_formulas.special import e_mc_e2
from math import sqrt

m = 2.0 * (10**-27)  # massa da partícula (kg)
c = 3.0 * (10**8)    # velocidade da luz (m/s)
v = 0.8 * c          # velocidade da partícula (m/s)

print("=== Relatividade Especial: Energia-Massa ===")
print(f"Massa (m): {m:.3e} kg")
print(f"Velocidade da luz (c): {c:.3e} m/s")
print(f"Velocidade da partícula (v): {v:.3e} m/s\n")

print("Passos intermediários:")
one_ = v**2 / c**2
print(f"1. v² / c²         = {one_:.6f}")

two_ = 1 - one_
print(f"2. 1 - (v² / c²)   = {two_:.6f}")

three_ = sqrt(two_)
print(f"3. sqrt(1 - v²/c²) = {three_:.6f}\n")

E = e_mc_e2(m, c, v)

print("Resultado final:")
print(f"E = {E:.3e} J")
