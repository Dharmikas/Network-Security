import sys
import os
import re
buff=[]
dic={}


class Pingofdeath(object):
	c=None
	def __init__(self):
		self.id=None
		self.offset=None
		self.flag=None
		self.protocol=None
		self.length=None
		self.tcpflags=None
		self.source_ip=None
		
		
		# Dictionaries
		self.dic_icmp={}
		self.syn_dic={}
		
		
	def extractingdata(self):
		for line in sys.stdin:
			line.strip()
			self.source_ip = re.findall('[0-9]*[.][0-9]*[.][0-9]*[.][0-9]*\s>\s([0-9]*[.][0-9]*[.][0-9]*[.][0-9]*)',line)
			if self.source_ip:
				c=self.source_ip
			self.id = re.findall('^[0-9].*id\s([^ ]*)[,]',line)
			self.offset = re.findall('^[0-9].*offset\s([^ ]*)[,]',line)
			self.flags = re.findall('^[0-9].*flags\s[[]([^ ]*)[]][,]',line)
			
			
			self.tcpflags= re.findall('.*Flags\s[[]([^ ]*)[]][,]',line)
			self.protocol = re.findall('^[0-9].*proto\s([^ ]*)',line)
			self.length = re.findall('^[0-9].*length\s([^ ]*)[)]',line)
			if len(self.id)!=0:
				if self.protocol == ['ICMP']:
					if self.flags==['+'] and self.length==['1500']:
						for i in self.id:
							if i in self.dic_icmp:
								self.dic_icmp[i]+=1
							else:
								self.dic_icmp[i]=1
								
				
			
			if len(self.tcpflags)!=0:
				for i in self.tcpflags:
					if i in self.syn_dic:
						self.syn_dic[i]+=1
					else:
						self.syn_dic[i]=1

			for i in self.dic_icmp:
				if self.dic_icmp[i]>=4:
					print "May be under ping of death ID:",i , c
								
			#print "ICMP",self.dic_icmp
			#print "SYN:", self.syn_dic
			if "S" in self.syn_dic and "A" not in self.syn_dic:
				print "Warning: SYN flood attack going on"
				os.system("sudo ip link set ens33 down")

			

ping=Pingofdeath()	
ping.extractingdata()
