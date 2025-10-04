from relativity_formulas.general import light_deflection_angle, to_degrees, to_arcseconds

M = 3.0 * 10**30
R = 7.0 * 10**8

radians = light_deflection_angle(M, R)
degrees = to_degrees(radians)
arcseconds = to_arcseconds(radians)

print("=== Relatividade Geral: Desvio da luz ===")
print(f"Massa (M): {M:.3e} kg")   # notação científica
print(f"Raio  (R): {R:.3e} m\n")

print(f"Desvio angular:")
print(f"  Radianos   : {radians:.3e}")
print(f"  Graus      : {degrees:.6f}°")
print(f'  Arcosegundos: {arcseconds:.3f}"')