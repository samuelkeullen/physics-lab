from math import sqrt

def e_mc_e2(mass: float, c: float, v: float) -> float:
    """
    Calcula a energia relativística de uma partícula em movimento.

    Fórmula:
        E = (m * c^2) / sqrt(1 - v^2 / c^2)

    Onde:
        m : massa em repouso (kg)
        c : velocidade da luz (m/s)
        v : velocidade da partícula (m/s)

    Retorna:
        Energia relativística (Joules)

    Observação:
        - Para v << c, a expressão se aproxima da clássica E ≈ mc^2.
        - Para v → c, o denominador tende a zero e a energia cresce muito.
    """
    return (mass * c**2) / sqrt(1 - (v**2 / c**2))


from math import sqrt

def lorentz_factor(v: float, c: float) -> float:
    """
    Calcula o fator de Lorentz (γ) para uma velocidade v.

    Fórmula:
        γ = 1 / sqrt(1 - v² / c²)

    Parâmetros:
        v : velocidade do objeto (m/s)
        c : velocidade da luz (m/s)

    Retorna:
        Fator de Lorentz (adimensional)
    """
    return 1 / sqrt(1 - (v**2 / c**2))
