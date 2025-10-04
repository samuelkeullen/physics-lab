from math import pi

def light_deflection_angle(M: float, R: float, G: float = 6.674e-11, c: float = 3e8) -> float:
    """
    Calcula o desvio angular da luz pela curvatura do espaço-tempo próximo a uma massa.
    
    Fórmula: θ ≈ 4GM / (c²R)

    Parâmetros:
        M : massa do objeto (kg)
        R : raio de aproximação (m)
        G : constante gravitacional (padrão = 6.674 × 10⁻¹¹)
        c : velocidade da luz (padrão = 3.0 × 10⁸)

    Retorna:
        θ (radianos)
    """
    return (4 * G * M) / (c**2 * R)


def gravitational_time_dilation(delta_t: float, phi: float, c: float) -> float:
    """
    Calcula o intervalo de tempo dilatado em um potencial gravitacional fraco.

    Fórmula aproximada (campo fraco):
        Δtₛ ≈ Δt * (1 - Φ / c²)

    Parâmetros:
        delta_t : intervalo de tempo no relógio de referência (Δt)
        phi     : potencial gravitacional no ponto considerado (Φ, J/kg)
        c       : velocidade da luz (m/s)

    Retorna:
        Intervalo de tempo medido pelo relógio no potencial Φ (Δtₛ)
    """
    return delta_t * (1 - phi / c**2)

# Aditionally


def to_degrees(radians: float) -> float:
    return radians * 180 / pi

def to_arcseconds(radians: float) -> float:
    return to_degrees(radians) * 3600
