#!/usr/bin/python
import os 
import re
import subprocess
import sys
#import MySQLdb
from configparser import SafeConfigParser
import glob

def findconfig():
#	parser = SafeConfigParser()
#	candidates = ['nightfallconfig.ini','hosts']
#	found = parser.read(candidates)
#	missing = set(candidates) - set(found)
#	print('Found config files : ', sorted(found))
#	print('Missing files 	  : ', sorted(missing))
	global computeIp  
	global commanagementIp  
	global computeFqdn  
	global computeName  
	global comgateway  
	global comnetmask  
	global comconip
	global comcontrollerip
	#iwillbereplaced=getconfig
	
#	if int(len(missing)) == 1:
#		print("Run python3 setup.py first " )
#		sys.exit()		
			

def status():
	os.system("if [ $? -eq 0 ]; then \n\t echo SUCCESS \n\telse \n\techo FAILED \n\texit\n\tfi")
	
def dbfunc():
	import MySQLdb
	global db 
	global cur
	db = MySQLdb.connect(host="localhost",user="root",passwd="root")
	cur = db.cursor()
	
print("                                                                                                    ")
print("                                                                                                    ")
print("                                              `..---..`                                             ")
print("                                          :oydmmmmddmmdhs+.                                         ")
print("                                        :hdddmmddddddddddddh+`                                      ")
print("                                     `/hdddddmmdddddddddmmmmmh/                                     ")
print("                                   `-dddddddddhhddmmmmddmddddhdy`                                   ")
print("                                   `hdddddddddddddddddddmmddddddy                                   ")
print("                                   .ddddddmdyhhddhdddmmddddddmddd:                                  ")
print("                                   -ddsyddddhdhddddddddddddddhshd:                                  ")
print("                                   `dh  `:ohdddddddmdddddho-`  om`                                  ")
print("                                    yd:     -+yddmmmmdho:     `hy                                   ")
print("                                    -dd+-`     `:hdd+`     `.:yd-                                   ")
print("                                     .ymdmdhyyyhd+/:hdhyyhhddhhy                                    ")
print("                                     +dddhddhddd+`s.-mmddddddddy                                    ")
print("                                     odddy/. oddhsdhsmmmh-``+ddo                                    ")
print("                                      //-:`  oddhhhhhsdds   ::`                                     ")
print("                                             -dyod+hh/dh.                                           ")
print("                                             `dhod+hyods                                            ")
print("                                             `dh+dodhsds                                            ")
print("                                              dd+d+dysd+                                            ")
print("                                              hd/d/dssd/                                            ")
print("                                              +y:d:h/sd-                                            ")
print("                                                 ` `                                                ")
print("                                           Project Nightfall                                        ")
print("   AN AUTOMATED SCRIPT FOR INSTALLATION OF OPENSTACK OCATA MULTI-NODE ON UBUNTU [ ON A NETWORK ]    ")
print("            NOT TO BE USED AT PRODUCTION SITE [ NOT MEANT TO STEAL SOMEONE'S JOB ]                  ")
print("                                BY MEGHA BANERJEE AND MANOJ C CHOUDHARY                             ")
print(" Run this in root ")
print(" Minimum Requirements : 4 GB Ram , 2 Bridge Network interfaces , virtualization checked , Number of cores per processor = 3  ")# MenuCODE
findconfig()


#menu()

#Interface Configuration 
def interfaceConfig():
	global networkInterface1
	global networkInterface2
	global managementIp
#	global bridgeCreation
	os.system("ip a | cat > tempconfig")
	with open('tempconfig', 'r') as myfile:
   		 data=myfile.read()

	confi = re.findall(r'ens\d\d', data)
	networkInterface1 =(confi[0])
	networkInterface2 = (confi[2])

	#print(networkInterface1)
	#print(networkInterface2)
	os.system("rm tempconfig")
	#networkInterface1 = "ens34"
	#etworkInterface2 = "ens33"
	findconfig()	
#	controllerIp = input("Enter Controller Ip (example : 192.168.0.35 ) : ") 
#	controllerNetmask = input("Enter Controller Ip Netmask ( example : 255.255.255.0 ) : ")
#	controllerGateway = input("Enter Controller Gateway ( example : 192.168.0.1 ) : ")
#	managementIp = input("Enter the Management Ip for openstack services ( example : 100.100.100.35 ) : ")
#	managementNetmask = input("Enter the Management Ip Netmask ( example : 255.255.255.0 ) : ")
	text = "# This file describes the network interfaces available on your system\n# and how to activate them. For more information, see interfaces(5).\n\nsource /etc/network/interfaces.d/* \n\n# The loopback network interface\n\nauto lo\niface lo inet loopback\n\nauto "+networkInterface1+"\niface "+networkInterface1+" inet static\naddress "+computeIp+"\nnetmask "+comnetmask+"\ngateway "+comgateway+"\ndns-nameservers 8.8.8.8\n\n#OpenStack management network (used by Openstack services like Nova,etc)\nauto "+networkInterface2+"\niface "+networkInterface2+" inet static\naddress "+commanagementIp+"\nnetmask "+comnetmask+"\n\n\n"
	saveFile = open('/etc/network/interfaces','w')
	saveFile.write(text)
	saveFile.close()
	
	

#installation of basic Services for deploying openstack private cloud
def prereq():
	print(" Runnig basic configuration ")
	os.system("apt update -y -qq")
	os.system("apt upgrade -y -qq")
	os.system("apt install chrony -y -qq")
	os.system("apt install openssh-server -y ")
	os.system("apt install python-mysqldb -y")
#	os.system("sudo apt-get install python3-pip -y")
#	os.system("sudo pip3 install PyMySQL")
	os.system("apt install software-properties-common -y ")
	os.system("add-apt-repository cloud-archive:ocata -y")
#	os.system("apt install python-openstackclient -y")
	os.system("apt update -y && apt dist-upgrade -y")
#	os.system("apt install python-pymysql -y")
	os.system("apt install vim -y")
	#print(" Enter the details ") 
	#contimes()
	#comtimes()
	os.system("cp /etc/hosts /etc/hosts.old")
	os.system("cat hosts >> /etc/hosts")
	os.system("cat /etc/hosts")
	os.system("cp /etc/hostname /etc/hostname.old")
	os.system("rm /etc/hostname")
	findconfig()
	hostnametext = computeName
	hostfile = open('/etc/hostname','w')
	hostfile.write(hostnametext)
	hostfile.close()
	print("\n")
	status()
	os.system("cat /etc/hostname")
	print("\n")
	os.system("ip a")	
	os.system("cp /etc/network/interfaces /etc/network/interface.old")
	os.system("rm /etc/network/interfaces")
	status()
	interfaceConfig()
	os.system("cat /etc/network/interfaces")
	#os.system(bridgeCreation)
	os.system("sudo sed -i -re 's/#net.ipv4.conf.default.rp_filter=1/net.ipv4.conf.default.rp_filter=0/g' /etc/sysctl.conf ")	
	os.system("sudo sed -i -re 's/#net.ipv4.conf.all.rp_filter=1/net.ipv4.conf.all.rp_filter=0/g' /etc/sysctl.conf ")
	os.system("sudo sed -i -re 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf ")
	status()
	os.system("sysctl -p ")
	status()
#	useless = input("Machine will restart now and Run the script for Installation and configuration of Mysql and RabbitMQ ( Enter to confirm ) ")
	#os.system("init 6")
	os.system("init 6")
#	restarttext = "ip addr flush "+networkInterface1+" && systemctl restart networking.service"
#	restarttext2 = "ip addr flush "+networkInterface2+" && systemctl restart networking.service"
#	os.system(restarttext)
#	os.system(restarttext2)
#	os.system("ip addr flush ens34 && systemctl restart networking.service")
	#menu()
prereq()
