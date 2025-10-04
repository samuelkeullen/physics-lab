# 🧪 Physics Lab – Relatividade em Python

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Experimental-orange.svg)

`physics-lab` é um repositório didático com exercícios de **Relatividade Especial (SR) 🔵** e **Relatividade Geral (GR) 🌌**, implementados em Python.  
Cada exercício inclui **passos detalhados**, **cálculos claros** e **resultados finais**, permitindo compreensão conceitual e prática do comportamento do espaço-tempo.

---

## 📂 Estrutura do Projeto

- `relativity_formulas/` → Módulos com funções de SR e GR:
  - `special.py` → fórmulas de Relatividade Especial (energia, dilatação do tempo, fator de Lorentz)
  - `general.py` → fórmulas de Relatividade Geral (desvio da luz, dilatação gravitacional do tempo)
- Scripts (`sr_*.py`, `gr_*.py`) → exercícios resolvidos com passos intermediários e resultados finais.

---

## 🔵 Exercícios de Relatividade Especial (SR)

| Exercício | Conceito | Fórmula | Script |
|-----------|----------|---------|--------|
| 1 | Energia relativística | `E = mc² / sqrt(1 - v²/c²)` | [`sr_mass_energy.py`](sr_mass_energy.py) |
| 2 | Dilatação do tempo | `Δt = Δt₀ * γ, γ = 1 / sqrt(1 - v²/c²)` | [`sr_time_dilation.py`](sr_time_dilation.py) |
| 3 | Energia de fissão | Energia por fissão × número de fissões | [`sr_fission_energy_hiroshima.py`](sr_fission_energy_hiroshima.py) |

> **Nota:** As fórmulas de SR são **exatas** no espaço-tempo plano. Conceitos chave: fator de Lorentz, energia relativística e equivalência massa-energia.

---

## 🌌 Exercícios de Relatividade Geral (GR)

| Exercício | Conceito | Fórmula aproximada | Script |
|-----------|----------|-----------------|--------|
| 1 | Desvio da luz pela gravidade | `θ ≈ 4GM / (c²R)` | [`gr_light_deflection.py`](gr_light_deflection.py) |
| 2 | Dilatação gravitacional do tempo | `Δt_s ≈ Δt * (1 - Φ / c²)` | [`gr_gravitational_time.py`](gr_gravitational_time.py) |

> **Nota:** As fórmulas de GR são **aproximações de campo fraco**. GR envolve a curvatura do espaço-tempo e é naturalmente mais complexo que SR.

---

## 📝 Boas práticas nos scripts

- Passos intermediários exibidos de forma legível.
- Resultados finais com notação científica ou arredondamento adequado.
- Funções reutilizáveis em `relativity_formulas`, separadas por teoria (SR ou GR).
- Código pronto para **aprendizado, testes e experimentação**.

---

## ⚡ Requisitos

- Python 3.8+
- Nenhuma biblioteca externa (apenas `math`)
- Executar scripts via terminal:

```bash
python sr_mass_energy.py
python sr_time_dilation.py
python sr_fission_energy_hiroshima.py
python gr_light_deflection.py
python gr_gravitational_time.py