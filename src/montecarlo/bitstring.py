import numpy as np

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        """
        Return number of bits that are on
        """
        return np.sum(self.config)

    def off(self):
        """
        Return number of bits that are off
        """
        return self.N - np.sum(self.config)

    def flip_site(self,i):
        """
        Flip the bit at site i
        """
        if i >= self.N:
            raise ValueError("The requested bit does not exist")
        if i < 0:
            raise ValueError("The requested bit cannot be negative")
        self.config[i] = 1 - self.config[i]
    
    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        sum = 0

        reversed_list = self.config[::-1]

        for i in range(self.N):
            sum += 2**i * reversed_list[i]

        return sum
 

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """
        if len(s) != self.N:
            raise ValueError("The provided list's lenth cannot be stored here")
        
        self.config = np.array(s)

    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """
        if dec >= 2**self.N:
            raise ValueError("The provided number is too large to be stored here")
        
        if dec < 0:
            raise ValueError("The provided number cannot be negative")
        
        temp_bits=[]

        for i in range(self.N):
            remainder = dec % 2
            temp_bits.append(remainder)
            dec = dec // 2

        temp_bits.reverse()

        self.config = np.array(temp_bits)