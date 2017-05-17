import sys
import os
import re

sourceip_arr=[]
destip_arr=[]
srcport_arr=[]
destport_arr=[]

sourceip_dic={}
destip_dic={}
srcport_dic={}
destport_dic={}
flags_dic={}

class nmapscan(object):
	def __init__(self):
		self.source_ip=None
		self.dest_ip=None
		self.source_port=None
		self.dest_port=None
		self.flag=None
		self.syn_dic={}
		self.linelen=0
	def extractingdata(self):
		for line in sys.stdin:
			line.strip()
			self.linelen=self.linelen+1
			self.source_ip = re.findall('^[0-9].*IP\s([0-9]*[.][0-9]*[.][0-9]*[.][0-9]*)[.].*\s>',line)
			self.dest_ip = re.findall('^[0-9].*>\s([0-9]*[.][0-9]*[.][0-9]*[.][0-9]*)[.][0-9]*',line)
			self.source_port = re.findall('^[0-9].*IP\s[0-9]*[.][0-9]*[.][0-9]*[.][0-9]*[.]([^ ]*)\s>',line)
			self.dest_port = re.findall('^[0-9].*>\s[0-9]*[.][0-9]*[.][0-9]*[.][0-9]*[.]([0-9]*):',line)
			self.flags= re.findall('^[0-9].*Flags\s[[]([^ ]*)[]][,]',line)

			print self.linelen,self.source_ip,self.dest_ip,self.source_port,self.dest_port
			
			if self.flags:
				for a in self.flags:
					if a not in flags_dic:
						flags_dic[a]=1
					else:
						flags_dic[a]+=1
			
			if self.dest_ip:
				for i in self.dest_ip:
					destip_arr.append(i)
					
					if i not in destip_dic:
						destip_dic[i]=1
					else:
						destip_dic[i]+=1
					
					
			if self.source_ip:
				for j in self.source_ip:
					sourceip_arr.append(j)
					
					if j not in sourceip_dic:
						sourceip_dic[j]=1
					else:
						sourceip_dic[j]+=1
					
					
			if self.source_port:
				for k in self.source_port:
					srcport_arr.append(k)
					
					if k not in srcport_dic:
						srcport_dic[k]=1
					else:
						srcport_dic[k]+=1
					
			if self.dest_port:
				for l in self.dest_port:
					destport_arr.append(l)
					
					
					if l not in destport_dic:
						destport_dic[l]=1
					else:
						destport_dic[l]+=1
			for i in flags_dic:
				if i == 'R.':
					print "NMAP -sX SCAN"
				if i == 'PSH.':
					print "NMAP -sT SCAN"


ping=nmapscan()
ping.extractingdata()



