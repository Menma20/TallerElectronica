from myhdl import block, always_comb, instance, delay, Signal, intbv

def read_table(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    # Se convierte a tupla para que MyHDL pueda sintetizar la ROM
    return tuple([int(line, 2) for line in lines if line.strip()])

@block
def seven_segment_decoder(din, sseg, table):
    @always_comb
    def logic():
        sseg.next = table[int(din)]
    return logic

@block
def testbench():
    # Entorno de pruebas encapsulado (estándar moderno de MyHDL)
    tabla_verdad = read_table("tabla.txt")
    din = Signal(intbv(0)[4:])
    sseg = Signal(intbv(0)[7:])
    
    dut = seven_segment_decoder(din, sseg, tabla_verdad)
    
    @instance
    def stimulus():
        for i in range(16):
            din.next = i
            yield delay(10)
            
    return dut, stimulus

if __name__ == '__main__':
    # 1. Simulación y VCD usando el API moderno
    tb = testbench()
    tb.config_sim(trace=True)
    tb.run_sim()
    print("Simulacion terminada. Archivo testbench.vcd generado.")
    
    # 2. Generar VHDL
    tabla_verdad = read_table("tabla.txt")
    din = Signal(intbv(0)[4:])
    sseg = Signal(intbv(0)[7:])
    dec = seven_segment_decoder(din, sseg, tabla_verdad)
    dec.convert(hdl='VHDL')
    print("Archivo VHDL generado.")