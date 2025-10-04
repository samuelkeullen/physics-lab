from relativity_formulas.special import lorentz_factor

# Dados do exercício
delta_t0 = 2.0        # tempo próprio (s)
c = 3.0 * 10**8       # velocidade da luz (m/s)
v = 0.6 * c           # velocidade do objeto (60% da velocidade da luz)

print("=== Relatividade Especial: Dilatação do Tempo ===")
print(f"Tempo próprio (Δt₀): {delta_t0:.2f} s")
print(f"Velocidade da luz (c): {c:.3e} m/s")
print(f"Velocidade relativa (v): {v:.3e} m/s\n")

# Passos intermediários
one_ = (v**2) / (c**2)
print("Passos intermediários:")
print(f"1. v² / c²       = {one_:.2f}")

two_ = 1 - one_
print(f"2. 1 - v²/c²     = {two_:.2f}")

three_ = two_**0.5
print(f"3. √(1 - v²/c²)  = {three_:.2f}\n")

# Cálculo final usando a função do fator de Lorentz
delta_t = delta_t0 * lorentz_factor(v, c)

print("Resultado final:")
print(f"Δt = Δt₀ · γ = {delta_t:.2f} s")
