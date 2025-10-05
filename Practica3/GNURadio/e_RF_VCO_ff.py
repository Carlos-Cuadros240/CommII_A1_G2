import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):
    """
    Oscilador Controlado por Voltaje de RF (RF VCO):
    
    Genera una señal senoidal modulada en amplitud y fase, con frecuencia central fija (fc).
    
    Entradas:
        - Entrada superior (A): Amplitud instantánea de la señal (float).
        - Entrada inferior (Q): Modulación instantánea en fase (radianes, float).
    
    Salida:
        - Señal senoidal modulada (float).
    
    Parámetros:
        - fc: Frecuencia central en Hz (default: 128000 Hz).
        - samp_rate: Frecuencia de muestreo (default: 320000 muestras/s).
    
    Nota:
        Se recomienda amplitudes positivas y modulaciones de fase entre -π y π para evitar discontinuidades.
    """

    def __init__(self, fc=128000, samp_rate=320000):  
        # Inicializa el bloque y establece sus parámetros y señales
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],  # dos entradas: amplitud y fase
            out_sig=[np.float32]              # una salida: señal modulada
        )
        self.fc = fc                          # frecuencia central del oscilador
        self.samp_rate = samp_rate            # tasa de muestreo del sistema
        self.n_m = 0                          # índice inicial de muestras

    def work(self, input_items, output_items):
        # Recupera las entradas: amplitud (A) y fase (Q)
        A = input_items[0]  # Señal de amplitud instantánea
        Q = input_items[1]  # Señal de modulación de fase instantánea
        y = output_items[0] # Señal de salida (resultado)
        
        # Determina el número de muestras en esta iteración
        N = len(A)
        
        # Genera el vector índice de muestras, desde n_m hasta (n_m + N - 1)
        n = np.linspace(self.n_m, self.n_m + N - 1, N)
        
        # Actualiza el contador de muestras totales procesadas
        self.n_m += N
        
        # Calcula la salida modulada según la ecuación del VCO:
        # y[n] = A[n] * cos(2π * fc * n / samp_rate + Q[n])
        y[:] = A * np.cos(2 * math.pi * self.fc * n / self.samp_rate + Q)
        
        # Retorna el número de muestras generadas en la salida
        return len(output_items[0])
