from pymodbus.client.tcp import ModbusTcpClient
from pymodbus.exceptions import ConnectionException

class ModbusForMungJin:
    def __init__(self, host="10.5.5.100", port=6502):
        self.host = host
        self.port = port
        self.client = ModbusTcpClient(self.host, self.port)

    # Robot (Server) - PC (Client) Modbus Connection
    def connect(self):
        self.client.connect()

    # Robot (Server) - PC (Client) Modbus Termination
    def close(self):
        self.client.close()

    # Write Digital Input
    def write_di(self, address, value):
        result = self.client.write_coil(address, value)
        return result
    
    # Write multiple digital inputs (same value)
    def write_multiple_di(self, start_address, value, count):
        values = [value] * count
        result = self.client.write_coils(start_address, values)
        return result
    
    # Reading Digital Input
    def read_di(self, address, count=1):
        result = self.client.read_coils(address, count)
        return result.bits
    
    # Reading Digital Output
    def read_do(self, address, bit=1):
        result = self.client.read_discrete_inputs(address, bit)
        return result.bits
    
    # Write analog input
    def write_ai(self, address, values, slave=0):
        result = self.client.write_registers(address, values, slave)
        return result
    
    # Reading analog input
    def read_ai(self, address, count=1):
        result = self.client.read_holding_registers(address, count)
        return result.registers

    # Reading analog Output 
    def read_ao(self, address, count=1):
        result = self.client.read_input_registers(address, count)
        return result.registers
    
# if __name__ == "__main__":

#     robot = ModbusConnection(host='192.168.0.120', port=6502) # host -> robot ip address
   
#     robot.connect()
    
#     robot.close()