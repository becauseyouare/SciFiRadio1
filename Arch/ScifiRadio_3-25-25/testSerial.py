import serial

try:
    #open serial port
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2, xonxoff=False)
    # , rtscts=False, dsrdtr=False  Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
    print(f"Port {ser.name} open: {ser.is_open} \n")
    while True:

        ser.flushInput()
        ser.flushOutput()

        #sendData
        #ser.write(48)
        #print(" sent 0 \r")

        # receive data
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                print(f"Received: {data} ")
                if data.isdigit():
                    n = int(data) / 2
                    print(f"half = {n}")
    #                break
      #data_raw = ser.readline()
      #print(data_raw)
        
#except ValueError:
 #   print("Invalid input: cannot convert to integer")
    
except KeyboardInterrupt:
    ser.close()


'''
except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print(f"Port {ser.name} closed.")
'''
    
