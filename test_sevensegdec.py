import pytest
from myhdl import Signal, intbv, Simulation, delay, instance
from sevensegdec import read_table, seven_segment_decoder 

tabla_verdad = read_table("tabla.txt")

@pytest.mark.parametrize("entrada_val", range(16))
def test_decodificador_casos(entrada_val):
    din = Signal(intbv(0)[4:])
    sseg = Signal(intbv(0)[7:])
    
    instancia_decodificador = seven_segment_decoder(din, sseg, tabla_verdad)
    
    @instance
    def test_logic():
        din.next = entrada_val 
        yield delay(10)        
        
        valor_esperado = int(tabla_verdad[entrada_val])
        
        # Asercion limpia de Pytest
        assert sseg == valor_esperado, f"Fallo en caso {entrada_val}. Esperado: {valor_esperado}, Obtenido: {sseg}"
        
    sim = Simulation(instancia_decodificador, test_logic)
    sim.run(20)