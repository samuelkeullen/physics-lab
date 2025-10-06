"""
Euler_Lagrange.py
Equação do movimento para o pêndulo via método de Euler-Lagrange
Autor: Seu Nome
"""

import numpy as np

def euler_lagrange_pendulo(g: float, l: float, theta: float) -> float:
    """
    Equação de movimento do pêndulo simples:
    θ¨ + (g/l) * sin(θ) = 0
    Retorna a aceleração angular θ¨.
    """
    return - (g / l) * np.sin(theta)
