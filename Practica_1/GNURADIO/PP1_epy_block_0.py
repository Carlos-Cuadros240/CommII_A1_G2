import numpy as np
from gnuradio import gr

# BLOQUE ACUMULADOR

class blk(gr.sync_block):
    def __init__(self):
        # Solo argumentos por defecto aquí
        gr.sync_block.__init__(
            self,
            name='e_Acum',             
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.accumulator = 0.0          # Estado interno para acumulación continua

    def work(self, input_items, output_items):
        x = input_items[0]              # Señal de entrada
        y = output_items[0]             # Señal de salida acumulada

        # Acumular de forma continua
        for i in range(len(x)):
            self.accumulator += x[i]
            y[i] = self.accumulator

        return len(y)


