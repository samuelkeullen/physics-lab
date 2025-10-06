"""
pendulo_main.py
Aplica as equações do pêndulo simples, calculando o período exato e aproximado
Autor: Seu Nome
"""

import numpy as np
from mechanic_formulas.Lagrange import lagrangiana
from mechanic_formulas.Euler_Lagrange import euler_lagrange_pendulo

# === Dados do problema ===
l = 0.5       # comprimento [m]
g = 9.81      # gravidade [m/s²]
theta0_deg = 10  # ângulo inicial em graus
theta0 = np.deg2rad(theta0_deg)  # conversão para radianos
m = 1.0       # massa arbitrária [kg]

print(f"Ângulo inicial (rad): {theta0:.5f}")

# === (a) Equação do movimento ===
print("\n(a) Equação do movimento via Euler–Lagrange:")
print("θ¨ + (g/l) * sin(θ) = 0")

# === (b) Aproximação de pequeno ângulo ===
T_aprox = 2 * np.pi * np.sqrt(l / g)
print(f"\n(b) Período aproximado (pequeno ângulo): T = {T_aprox:.4f} s")

# === (c) Período exato via série de K(k) ===
theta_half = theta0 / 2
k = np.sin(theta_half)
k2 = k ** 2

# Série de K(k)
Kk = (np.pi / 2) * (
    1 + (1/4) * k2 +
    (9/64) * k2**2 +
    (25/256) * k2**3 +
    (1225/16384) * k2**4
)

T_exato = 4 * np.sqrt(l / g) * Kk

print("\n(c) Período exato via série de K(k):")
print(f"k = {k:.6f}")
print(f"K(k) = {Kk:.6f}")
print(f"T_exato = {T_exato:.4f} s")

# === (d) Erro percentual ===
erro_percentual = abs((T_exato - T_aprox) / T_exato) * 100
erro_segundos = abs(T_exato - T_aprox)

print("\n(d) Comparação e validação:")
print(f"Erro em segundos: {erro_segundos:.5f} s")
print(f"Erro percentual: {erro_percentual:.3f}%")

# === Verificação de hipótese ===
if erro_percentual < 1:
    print("✅ Hipótese de pequeno ângulo é aceitável (<1%)")
else:
    print("⚠️ Hipótese de pequeno ângulo NÃO é aceitável")
