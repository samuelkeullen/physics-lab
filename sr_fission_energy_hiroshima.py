from relativity_formulas.special import e_mc_e2

# Dados do exercício
mass_u235 = 5.0           # kg
molar_mass_u235 = 0.235   # kg/mol
avogadro = 6.022e23       # átomos/mol
fraction_fissioned = 0.01 # 1%
energy_per_fission_j = 200e6 * 1.602e-19  # J

tnt_equivalence_j = 4.184e12  # 1 kt TNT = 4.184e12 J

print("=== Relatividade Especial: Energia de Fissão ===")
print(f"Massa de U-235           : {mass_u235:.3f} kg")
print(f"Fração de átomos fissionados : {fraction_fissioned:.2%}")
print(f"Energia por fissão       : {energy_per_fission_j:.3e} J\n")

# Passos intermediários
moles = mass_u235 / molar_mass_u235
print(f"1. Número de moles de U-235  = {moles:.4f} mol")

total_atoms = moles * avogadro
print(f"2. Número total de átomos    = {total_atoms:.3e} átomos")

fissions = total_atoms * fraction_fissioned
print(f"3. Número de fissões (1%)    = {fissions:.3e} átomos\n")

# Energia total liberada
total_energy = fissions * energy_per_fission_j
kt_tnt = total_energy / tnt_equivalence_j

print("Resultado final:")
print(f"Energia total liberada E_total = {total_energy:.3e} J")
print(f"Equivalente em kilotons de TNT = {kt_tnt:.2f} kt")
