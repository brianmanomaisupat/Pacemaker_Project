import serial
import struct
from time import sleep
from serial_communication import SerialCommunication

'''def send_packet(ser):
        red_enable = struct.pack('B', 255)
        green_enable = struct.pack('B', 255)
        blue_enable = struct.pack('B', 255)
        off_time = struct.pack('f', 3.0)
        switch_time = struct.pack('H', 200)
        packet = b"\x16\x55" + red_enable + green_enable + blue_enable + off_time + switch_time
        ser.write(packet)
        print(packet.hex())

def receive(s):
    packet = b"\x16\x22" + b'\x00'*9
    s.write(packet)
    data = s.read(9)
    print(data[0])
    print(data[1])
    print(data[2])
    print(struct.unpack('f', data[3:7])[0])
    print(struct.unpack('H', data[7:9])[0])'''
    
def main():
    red_enable = 1
    green_enable = 0
    blue_enable = 0
    off_time = 3.0
    switch_time = 200

    values = [red_enable, green_enable, blue_enable, off_time, switch_time]

    yes = SerialCommunication()
    yes.send_packet(values)


if __name__ == "__main__":
    main()