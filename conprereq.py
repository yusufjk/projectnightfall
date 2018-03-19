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
	# Configure all the hosts configurations
	#global controllerIp = (parser.get('controller_config','controllerIp0'))
	#global conmanagementIp = (parser.get('controller_config','managementIp0'))
	#global controllerFqdn = (parser.get('controller_config','controllerFqdn0')) 
	#global controllerName = (parser.get('controller_config','controllerName0'))
	#global congateway = (parser.get('controller_config','gateway0'))
	#global connetmask = (parser.get('controller_config','netmask'))
	
	global controllerIp  
	global conmanagementIp  
	global controllerFqdn  
	global controllerName  
	global congateway  
	global connetmask  
	#global computeIp = (parser.get('compute_config','computeIp0'))
	#global commanagementIp = (parser.get('compute_config','managementIp0'))
	#global computeFqdn = (parser.get('compute_config','computeFqdn0'))
	#global computeName = (parser.get('compute_config','computeName0'))
	#global comgateway = (parser.get('compute_config','gateway0'))
	#global comnetmask = (parser.get('compute_config','netmask'))
	#iwillbereplaced=getconfig

#	if int(len(missing)) == 2:
#		print("Run python3 setup.py ")
#		sys.exit()		
#	if int(len(missing)) == 1:
#		print("Run python3 setup.py ")
#		sys.exit()
	

def status():
	os.system("if [ $? -eq 0 ]; then \n\t echo SUCCESS \n\telse \n\techo FAILED \n\texit\n\tfi")
	
#def dbfunc():
#	import MySQLdb
#	global db 
#	global cur
#	db = MySQLdb.connect(host="localhost",user="root",passwd="root")
#	cur = db.cursor()
	
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

#def menu():
#	print(" MENU [ blank for all ]")
#	print(" 1. Basic Configuration ")
#	print(" 2. Installation of Mysql and RabbitMQ ")
#	print(" 3. Installation and configuration of keystone ")
#	print(" 4. Installation and configuration of Glance ")
#	print(" 5. Installation and configuration of Neutron ")
#	print(" 6. Installation and configuration of Nova ")
#	print(" 7. Installation of Horizon : ")
#	print(" Exit")

#menu()
#Configuration for compute 
#def comtimes():
#	findconfig()
#	global computeIp
#	global computeName
#	global ComputeFqdn
#	computetimes = 0
#	computetimes = input("Enter the number of computes hostname and ip to be configured : ")
#	count = 0 
#	while (count < int(computetimes) ):
#		computetext = "" 
#		computeIp = input("Enter compute ip which you desire ( example : 192.168.0.36 ) : ")
#		computeName = input("Enter compute name which you desire ( example : compute ) : ")
#		computeFqdn = input("Enter compute fully qualified domain name ( example : compute.nightfall.com ) : ")
#	computetext = '\n'+computeIp+'\t'+computeFqdn+'\t\t'+computeName
#	appendFile = open('/etc/hosts','a')
#	appendFile.write(computetext)
#	appendFile.close()
#		count = count + 1
	
#Configuration for controller
#def contimes():
#	findconfig()
#	global controllerIp
#	global controllerName
#	global controllerFqdn
#	controllertimes = 0
#	controllertimes = input("Enter the number of controller hostname and ip to be configured : ")
#	count1 = 0
#	while (count1 < int(controllertimes) ):
#		controllertext = ""
#		controllerIp = input("Enter ccntroller ip which you desire ( example : 192.168.0.35 ) : ")
#		controllerName = input("Enter controller name which you desire ( example : controller ) : ")
#		controllerFqdn = input("Enter controller fully qualified domain name ( example : controller.nightfall.com ) : ")
#	controllertext = '\n'+controllerIp+'\t'+controllerFqdn+'\t'+controllerName
#	appendFile = open('/etc/hosts','a')
#	appendFile.write(controllertext)
#	appendFile.close()
#		count1 = count1 + 1

#Interface Configuration 
def interfaceConfig():
	global networkInterface1
	global networkInterface2
	global managementIp
	global bridgeCreation
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
	text = "# This file describes the network interfaces available on your system\n# and how to activate them. For more information, see interfaces(5).\n\nsource /etc/network/interfaces.d/* \n\n# The loopback network interface\n\nauto lo\niface lo inet loopback\n\nauto "+networkInterface1+"\niface "+networkInterface1+" inet manual\nup ifconfig $IFACE 0.0.0.0 up\nupip link set $IFACE promisc on\ndownip link set $IFACE promisc off\ndown ifconfig $IFACE down\n\nauto br-ex\niface br-ex inet static\naddress "+controllerIp+"\nnetmask "+connetmask+"\ngateway "+congateway+"\ndns-nameservers 8.8.8.8\n\n#OpenStack management network (used by Openstack services like Nova,etc)\nauto "+networkInterface2+"\niface "+networkInterface2+" inet static\naddress "+conmanagementIp+"\nnetmask "+connetmask+"\n"
	saveFile = open('/etc/network/interfaces','w')
	saveFile.write(text)
	saveFile.close()
	bridgeCreation = 'ovs-vsctl add-port br-ex ' + networkInterface1 
	

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
	os.system("apt install python-openstackclient -y")
	os.system("apt-get install -y openvswitch-switch")
	os.system("ovs-vsctl add-br br-ex")
	os.system("apt install vim -y")
	#print(" Enter the details ") 
	#contimes()
	#comtimes()
	os.system("cp /etc/hosts /etc/hosts.old")
	os.system("cp hosts /etc/hosts")
	os.system("cat /etc/hosts")
	os.system("sudo sed -i -re 's/ubuntu/controller/g' /etc/hostname ")
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
	os.system(bridgeCreation)
	os.system("sudo sed -i -re 's/#net.ipv4.conf.default.rp_filter=1/net.ipv4.conf.default.rp_filter=0/g' /etc/sysctl.conf ")	
	os.system("sudo sed -i -re 's/#net.ipv4.conf.all.rp_filter=1/net.ipv4.conf.all.rp_filter=0/g' /etc/sysctl.conf ")
	os.system("sudo sed -i -re 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf ")
	status()
	os.system("sysctl -p ")
	status()
#	useless = input("Machine will restart now and Run the script for Installation and configuration of Mysql and RabbitMQ ( Enter to confirm ) ")
	os.system("init 6")
#	os.system("ip addr flush ens33 && systemctl restart networking.service")
#	os.system("ip addr flush ens34 && systemctl restart networking.service")
#	menu()

prereq()
