from relativity_formulas.general import gravitational_time_dilation

# Dados do exercício
delta_t = 1.0          # tempo no relógio da Terra (s)
phi = -4.0e7           # potencial gravitacional do satélite (J/kg)
c = 3.0e8              # velocidade da luz (m/s)

print("=== Relatividade Geral: Dilatação Gravitacional do Tempo ===")
print(f"Tempo na Terra (Δt)     : {delta_t:.12f} s")
print(f"Potencial gravitacional Φ: {phi:.3e} J/kg")
print(f"Velocidade da luz (c)   : {c:.3e} m/s\n")

# Passos intermediários
c2 = c**2
print("Passos intermediários:")
print(f"1. c² = {c2:.3e} (m²/s²)")

phi_over_c2 = phi / c2
print(f"2. Φ / c² = {phi:.3e} / {c2:.3e} = {phi_over_c2:.12f}")

factor = 1 - phi_over_c2
print(f"3. Fator 1 - Φ/c² = {factor:.12f}\n")

# Cálculo final usando a função
delta_t_sat = gravitational_time_dilation(delta_t, phi, c)
print("Resultado final:")
print(f"Δtₛ (satélite) = {delta_t_sat:.12f} s")
