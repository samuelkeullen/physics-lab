"""
Lagrange.py
Define funções da Lagrangiana para sistemas mecânicos simples
Autor: Seu Nome
"""

import numpy as np

def energia_cinetica(m: float, l: float, theta_dot: float) -> float:
    """Energia cinética: T = (1/2) m l^2 (θ̇)^2"""
    return 0.5 * m * (l ** 2) * (theta_dot ** 2)

def energia_potencial(m: float, g: float, l: float, theta: float) -> float:
    """Energia potencial: V = m g l (1 - cos(θ))"""
    return m * g * l * (1 - np.cos(theta))

def lagrangiana(m: float, g: float, l: float, theta: float, theta_dot: float) -> float:
    """Lagrangiana: L = T - V"""
    T = energia_cinetica(m, l, theta_dot)
    V = energia_potencial(m, g, l, theta)
    return T - V
