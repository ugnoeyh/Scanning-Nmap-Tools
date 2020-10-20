import nmap
import socket
scanner=nmap.PortScanner()

print ("nmap Scanner ")                                 
ip_addr=input("enter the ip address ")									# ip 입력
print("you have entered the IP address : ",ip_addr)
type(ip_addr)
resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan										
                2)UDP Scan
                3)Comprehensive Scan 
	        4)List Scan 
	        5)Ping Scan 
	        6)banner grabbing
		    \n""")								
print("you have selected option:",resp)

#SYN STEALTH Scan
if resp=='1':
	print( "NMap Version: ",scanner.nmap_version())
	scanner.scan(ip_addr,'1-1024','-v -sS ')							
	print(scanner.command_line())
	print(scanner.scaninfo())
	print("IP Status: ",scanner[ip_addr].state()) 
	print(scanner[ip_addr].all_protocols()) 
	try:
		print("Open ports",scanner[ip_addr]['tcp'].keys())
	except(Exception):
		print("No Ports open")

#udp scan
elif resp=='2':
	print("Wait for a moment...")				    					
	print("NMap Version: ",scanner.nmap_version())
	scanner.scan(ip_addr,'1-8080','-v -sU ')
	print(scanner.command_line())
	print(scanner.scaninfo())
	print("IP Status: ",scanner[ip_addr].state()) 
	print(scanner[ip_addr].all_protocols()) 
	try:
		print ("Open ports",scanner[ip_addr]['udp'].keys())
		if scanner[ip_addr].has_tcp(22):
			print(scanner[ip_addr].tcp(22))
	except(Exception):
		print("No Ports Open")

#comprehensive scan
elif resp=='3':
	print("NMap Version: ",scanner.nmap_version())							
	scanner.scan(ip_addr,'1-8080','-vv -sS -sV -sC -A -O ')
	print(scanner.command_line())
	print(scanner.scaninfo())
	print("IP Status: ",scanner[ip_addr].state()) 
	print(scanner[ip_addr].all_protocols()) 
	try:
		print ("Open ports",scanner[ip_addr]['tcp'].keys())
		if scanner[ip_addr].has_tcp(22):
			print(scanner[ip_addr].tcp(22))
	except(Exception):
		print("No Ports Open")

#list scan
elif resp=='4':                                                              
	print("NMap Version: ",scanner.nmap_version())
	scanner.scan(ip_addr,'1-8080','-v -sT -A -sV ')
	print(scanner.command_line())									
	print(scanner.scaninfo())
	print("IP Status: ",scanner[ip_addr].state()) 
	print(scanner[ip_addr].all_protocols()) 
	
	try:
		print("Open ports",scanner[ip_addr]['tcp'].keys())
		if scanner[ip_addr].has_tcp(22):
			print(scanner[ip_addr].tcp(22))
	except(Exception):
		print("No Ports Open")

#Ping Scan 
elif resp=='5':
	print("NMap Version: ",scanner.nmap_version())
	scanner.scan(ip_addr,'1-8080','-v ')
	print(scanner.command_line())									
	print(scanner.scaninfo())
	print("IP Status: ",scanner[ip_addr].state()) 
	print(scanner[ip_addr].all_protocols()) 
	print(scanner.csv())

#banner grabbing of specific port
elif resp=='6':
	t_port = int(input("Enter Port: "))
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	try:
		sock.connect((ip_addr,t_port))								
		sock.send((('GET HTTP/1.1 \r\n').encode('utf-8')))
		ret = sock.recv(1024)
		print( '[+]' + (ret).decode('utf-8'))	
	except(Exception):
		print("Connection can't formed on the given port") 

else:
	exit(0)												
