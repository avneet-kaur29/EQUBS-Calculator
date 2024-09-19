import math
class Calculations:
    # constants
    avogadros_number = 6.02214076e+23
    diamond_lattice_constant = 3.567095
    c_per_unit_cell = 8
    molar_mass_12c = 12
    molar_mass_13c = 13

    diamond_lattice_constant_cm = diamond_lattice_constant * 1e-8
    ml_per_l = 1000

    def combined_molar_mass(self, percent_13):
        return ((percent_13/100) * self.molar_mass_13c) + (((100-percent_13)/100) * self.molar_mass_12c)

    # volume of spherical nd in cm^3 given diameter in nm
    def volume(self, diameter):
        diameter = diameter * 1e-7
        return (4/3) * math.pi * (diameter/2)**3

    # density = (atoms per unit cell * molar mass)/(avogadro's number * lattice constant^3)
    def diamond_density(self, percent_13):
        return (self.c_per_unit_cell * self.combined_molar_mass(percent_13))/(self.avogadros_number * (self.diamond_lattice_constant_cm**3))

    # num_density = (ppm/10^6)*((avogadro's number * density)/molar mass)
    def number_density(self, percent_13, nv_density):
        return (nv_density/1e+6)*((self.avogadros_number * self.diamond_density(percent_13))/self.combined_molar_mass(percent_13))

    # nvs/nd = num_density * vol
    def nvs_per_nd(self, percent_13, nv_density, nd_diameter):
        return self.number_density(percent_13, nv_density) * self.volume(nd_diameter)

    # mass per ND = density of diamond * volume of ND
    def mass_per_nd(self, percent_13, nd_diameter):
        return self.diamond_density(percent_13) * self.volume(nd_diameter)

    # molar concentration = dispersion * 1000 / (mass per nd * avogadro's number)
    def molar_concentration(self, percent_13, dispersion, nd_diameter):
        return (dispersion)/(self.mass_per_nd(percent_13, nd_diameter) * self.avogadros_number)


