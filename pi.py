
from smbus import SMBus

address = 0x6 # bus addressess
bus = SMBus(1) # indicates /dev/ic2-1

ic = 1

print ("Lights will ON on 1,2 or 0 will turn OFF ")
while ic == 1:
    
	Light = input("=> ")

	if Light == "1":
		bus.write_byte(address, 0x1)
		
	elif Light == "0":
		bus.write_byte(address, 0x0)
		print("Thanks!! ")
		break
		
	elif Light == "2":
		bus.write_byte(address, 0x2) 
	
	else:
		ic = 0
		
        
	print ("Press 1,2 to turn on Lights and 0 to turn off.")
	


