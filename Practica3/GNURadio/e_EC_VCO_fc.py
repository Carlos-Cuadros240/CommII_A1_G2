import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):
    """
    Oscilador Controlado por Voltaje en Banda Base (CE VCO):
    
    Genera una señal compleja en banda base, modulada en amplitud y fase.
    
    Entradas:
        - Entrada superior (A): Amplitud instantánea de la señal (float).
        - Entrada inferior (Q): Fase instantánea de la señal en radianes (float).
    
    Salida:
        - Señal compleja modulada (I/Q) en banda base (complex).
    
    Nota:
        La señal de salida es ideal para modulaciones digitales o procesamiento en banda base.
    """

    def __init__(self):  
        # Inicialización del bloque
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],   # entradas: amplitud y fase
            out_sig=[np.complex64]             # salida compleja (I/Q)
        )
        
    def work(self, input_items, output_items):
        # Obtiene entradas: amplitud (A) y fase (Q)
        A = input_items[0]   # Señal de amplitud instantánea
        Q = input_items[1]   # Señal de fase instantánea en radianes
        
        # Vector de salida complejo (I/Q)
        y = output_items[0]
        
        # Número de muestras actuales
        N = len(A)
        
        # Genera la señal compleja modulada:
        # salida[n] = A[n] * exp(j * Q[n])
        y[:] = A * np.exp(1j * Q)
        
        # Retorna la cantidad de muestras procesadas
        return len(output_items[0])
