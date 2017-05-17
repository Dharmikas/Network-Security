Have created a parser in python to read the TCPDUMP file in real time basis using os library.

"Network Analyzer.py"
source ip gets the first ip address from where the packet is sent and dest ip is the destination.
Same is the case of source port and dest port.
In SYN flood attack the attacker does not send the ACK message after it has got SYN-ACK message from the server. Making the server ports busy. So the code counts the number of SYN-ACK and SYN messages from a particular ip address and also counts the source i.e. victims ports are open and just 1 or 2 destination ports.
Next comes the ping of death attack. Normal ping requests is of 64 Kb or small, but in ping of death command the packet size is of maybe 65000 or so. The ethernet can support only till 1500 so the packet get fragmented and generates the flag. So the code sees the particular protocol name, packet fragments, flags and packet size to see if the victim is under attack.

"Nmapscan detection.py"
Python code to detect if someone is scanning our pc for open ports.


"NS-3 topology.cc" 
Used to create the topology in deterlab or ns-3/ns-2 simulator.

"TCPdump2.txt"
Example of a tcpdump file extract