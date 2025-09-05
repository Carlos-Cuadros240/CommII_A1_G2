import numpy as np
from gnuradio import gr

# BLOQUE DE ACUMULACIÓN DIFERENCIAL

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diff',               # Nombre del bloque
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior = 0.0         # Estado: última suma acumulada

    def work(self, input_items, output_items):
        x = input_items[0]               # Señal de entrada
        y = output_items[0]              # Señal de salida
        N = len(x)

        # Cálculo de la acumulación diferencial
        acumulado = np.cumsum(x) + self.acum_anterior
        y[:] = acumulado - self.acum_anterior

        # Guardamos el nuevo valor acumulado total para el siguiente bloque
        self.acum_anterior = acumulado[-1]

        return len(y)

