from .isinghamiltonian import IsingHamiltonian

class MonteCarlo:
    def __init__(self, ham: IsingHamiltonian):
        self.ham = ham

    