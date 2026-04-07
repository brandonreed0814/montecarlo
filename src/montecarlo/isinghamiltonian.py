import numpy as np
import networkx as nx
import math
from .bitstring import BitString

class IsingHamiltonian:
    def __init__(self, G: nx.Graph):

        self.G = G
        self.mus = np.zeros(len(G.nodes))

    def energy(self, bs: BitString):
        
        total_energy = 0

        for e in self.G.edges:
            weight = self.G.edges[e].get('weight', 1.0)
            
            spin_i = 2 * bs.config[e[0]] - 1
            spin_j = 2 * bs.config[e[1]] - 1
            
            total_energy += weight * spin_i * spin_j
        
        for i in self.G.nodes:
            spin_i = 2 * bs.config[i] - 1
            total_energy += self.mus[i] * spin_i

        return total_energy
    
    def set_mu(self, mus: np.array):
        if len(mus) != len(self.G.nodes):
            raise ValueError("Mus do not match the number of nodes")
        self.mus = mus

    def compute_average_values(self, T: float):
        N = len(self.G.nodes)
        Z = 0.0
        E_sum = 0.0
        M_sum = 0.0
        EE_sum = 0.0
        MM_sum = 0.0

        # Create a temporary BitString to iterate through states
        tmp_bs = BitString(N)

        for i in range(2**N):
            tmp_bs.set_integer_config(i)

            E_i = self.energy(tmp_bs)
            # Magnetization is sum of spins (2*bits - 1)
            M_i = tmp_bs.on() - tmp_bs.off()
            
            weight = math.exp(-E_i / T)
            Z += weight
            E_sum += E_i * weight
            M_sum += M_i * weight
            EE_sum += (E_i**2) * weight
            MM_sum += (M_i**2) * weight

        # Final Averages
        E = E_sum / Z
        M = M_sum / Z
        EE = EE_sum / Z
        MM = MM_sum / Z
        
        # Heat Capacity and Magnetic Susceptibility
        HC = (EE - E**2) / (T**2)
        MS = (MM - M**2) / T
            
        return E, M, HC, MS