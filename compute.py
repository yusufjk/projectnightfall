#!/usr/bin/python
import os 
import re
import subprocess
import sys
#import MySQLdb
from configparser import SafeConfigParser
import glob

def findconfig():
	parser = SafeConfigParser()
	candidates = ['nightfallconfig.ini','hosts']
	found = parser.read(candidates)
	missing = set(candidates) - set(found)
	print('Found config files : ', sorted(found))
	print('Missing files 	  : ', sorted(missing))
	global computeIp  
	global commanagementIp  
	global computeFqdn  
	global computeName  
	global comgateway  
	global comnetmask  
	global comconip
	global comcontrollerip
	#iwillbereplaced=getconfig
	
	if int(len(missing)) == 2:
		print("Run python3 setup.py ")	
	if int(len(missing)) == 1:
		print("Run python3 setup.py ")
		sys.exit()		
			

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
	text = "# This file describes the network interfaces available on your system\n# and how to activate them. For more information, see interfaces(5).\n\nsource /etc/network/interfaces.d/* \n\n# The loopback network interface\n\nauto lo\niface lo inet loopback\n\nauto "+networkInterface1+"\niface "+networkInterface1+" inet static\naddress "+computeIp+"\nnetmask "+comnetmask+"\ngateway "+comgateway+"\ndns-nameservers 8.8.8.8\n\n#OpenStack management network (used by Openstack services like Nova,etc)\nauto "+networkInterface2+"\niface "+networkInterface2+" inet static\naddress "+conmanagementIp+"\nnetmask "+connetmask+"\n\n\n"
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
	os.system("cp hosts /etc/hosts")
	os.system("cat /etc/hosts")
	os.system("cp /etc/hostname /etc/hostname.old")
	os.system("rm /etc/hostname")
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
	os.system(bridgeCreation)
	os.system("sudo sed -i -re 's/#net.ipv4.conf.default.rp_filter=1/net.ipv4.conf.default.rp_filter=0/g' /etc/sysctl.conf ")	
	os.system("sudo sed -i -re 's/#net.ipv4.conf.all.rp_filter=1/net.ipv4.conf.all.rp_filter=0/g' /etc/sysctl.conf ")
	os.system("sudo sed -i -re 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf ")
	status()
	os.system("sysctl -p ")
	status()
#	useless = input("Machine will restart now and Run the script for Installation and configuration of Mysql and RabbitMQ ( Enter to confirm ) ")
	#os.system("init 6")
	restarttext = "ip addr flush "+networkInterface1+" && systemctl restart networking.service"
	restarttext2 = "ip addr flush "+networkInterface2+" && systemctl restart networking.service"
	os.system(restarttext)
	os.system(restarttext2)
#	os.system("ip addr flush ens34 && systemctl restart networking.service")
	

def neutronproc():
	os.system("apt-get install neutron-plugin-openvswitch-agent python-mysqldb python-neutronclient")
	os.system("rm /etc/neutron/plugins/ml2/openvswitch_agent.ini")
	os.system("rm /etc/neutron/neutron.conf")
	openvswitchAgentConfig = "[DEFAULT]\nverbose = true\n[agent]\ntunnel_types = vxlan\nl2population = True\n[ovs]\nlocal_ip = "+commanagementIp+"\nenable_tunneling = True\nvxlan_udp_port = 4789\ntunnel_types = vxlan\ntunnel_id_ranges = 1:2000\ntunnel_network_types = vxlan\n[securitygroup]\nfirewall_driver = neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver\nenable_security_group = True\n[xenapi]\n"
	saveFile = open('/etc/neutron/plugins/ml2/openvswitch_agent.ini','w')
	saveFile.write(openvswitchAgentConfig)
	saveFile.close()
	neutronConfig = "[DEFAULT]\n\ncore_plugin = ml2\nservice_plugins = router\nallow_overlapping_ips = true\nverbose = true\nauth_strategy = keystone\ntransport_url = rabbit://openstack:rabbit@"+comcontrollerip+"\n\nnotify_nova_on_port_status_changes = True\nnotify_nova_on_port_data_changes = True\n\n[agent]\n\nroot_helper = sudo /usr/bin/neutron-rootwrap /etc/neutron/rootwrap.conf\n\n[cors]\n\n[cors.subdomain]\n\n[database]\n\nconnection = mysql+pymysql://neutronUser:neutronPass@"+comcontrollerip+"/neutron\n\n[keystone_authtoken]\n\nauth_uri = http://"+comcontrollerip+":5000\nauth_url = http://"+comcontrollerip+":35357\nmemcached_servers = "+comcontrollerip+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = neutron\npassword = service_pass\n\n[matchmaker_redis]\n\n[nova]\n\nauth_url = http://"+comcontrollerip+":35357\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nregion_name = RegionOne\nproject_name = service\nusername = nova\npassword = service_pass\n\n[oslo_concurrency]\n\nlock_path = /var/lib/neutron/tmp\n\n[oslo_messaging_amqp]\n\n[oslo_messaging_kafka]\n\n[oslo_messaging_notifications]\n\n[oslo_messaging_rabbit]\n\n[oslo_messaging_zmq]\n\n[oslo_middleware]\n\n[oslo_policy]\n\n[qos]\n\n[quotas]\n\n[ssl]\n"
	saveFile = open('/etc/neutron/neutron.conf','w')
	saveFile.write(neutronConfig)
	saveFile.close()
	os.system("service neutron-openvswitch-agent restart;")
	

def novaproc():
	os.system("apt-get install nova-compute sysfsutils -y")
	os.system("rm /etc/nova/nova-compute.conf")
	os.system("rm /etc/nova/nova.conf")
	novaConfig = "[DEFAULT]\n\nenabled_apis=osapi_compute,metadata \nmy_ip = "+commanagementIp+"\nuse_neutron = True\nfirewall_driver = nova.virt.firewall.NoopFirewallDriver\ntransport_url = rabbit://openstack:rabbit@"+comcontrollerip+"\n\ndhcpbridge_flagfile=/etc/nova/nova.conf\n\ndhcpbridge=/usr/bin/nova-dhcpbridge\n\nforce_dhcp_release=true\n\nstate_path=/var/lib/nova\n\nlog_dir=/var/log/nova\n\n[api]\n\nauth_strategy=keystone\n\n[api_database]\n\nconnection=mysql+pymysql://novaUser:novaPass@"+comcontrollerip+"/nova_api\n\n[barbican]\n\n[cache]\n\n[cells]\n\nenable=False\n\n[cinder]\n\nos_region_name = RegionOne\n\n[cloudpipe]\n\n[conductor]\n\n[console]\n\n[consoleauth]\n\n[cors]\n\n[cors.subdomain]\n\n[crypto]\n\n[database]\n\nconnection=mysql+pymysql://novaUser:novaPass@"+comcontrollerip+"/nova\n\n[ephemeral_storage_encryption]\n\n[filter_scheduler]\n\ndiscover_hosts_in_cells_interval = 300\n\n[glance]\n\napi_servers = http://"+comcontrollerip+":9292\n\n[guestfs]\n\n[healthcheck]\n\n[hyperv]\n\n[image_file_url]\n\n[ironic]\n\n[key_manager]\n\n[keystone_authtoken]\n\nauth_uri = http://"+comcontrollerip+":5000\nauth_url = http://"+comcontrollerip+":35357\nmemcached_servers = "+comcontrollerip+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = nova\npassword = service_pass\n\n[libvirt]\n\n[matchmaker_redis]\n\n[metrics]\n\n[mks]\n\n[neutron]\n\nservice_metadata_proxy = True\nmetadata_proxy_shared_secret = mystack\nurl = http://"+comcontrollerip+":9696\nauth_url = http://"+comcontrollerip+":35357\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nregion_name = RegionOne\nproject_name = service\nusername = neutron\npassword = service_pass\n\n[notifications]\n\n[osapi_v21]\n\n[oslo_concurrency]\n\nlock_path = /var/lib/nova/tmp\n\n[oslo_messaging_amqp]\n\n[oslo_messaging_kafka]\n\n[oslo_messaging_notifications]\n\n[oslo_messaging_rabbit]\n\n[oslo_messaging_zmq]\n\n[oslo_middleware]\n\n[oslo_policy]\n\n[pci]\n\n[placement]\nos_region_name = RegionOne\nproject_domain_name = Default\nproject_name = service\nauth_type = password\nuser_domain_name = Default\nauth_url = http://"+comcontrollerip+":35357/v3\nusername = placement\npassword = service_pass\n\n[quota]\n\n[rdp]\n\n[remote_debug]\n\n[scheduler]\ndiscover_hosts_in_cells_interval = 300\n[serial_console]\n\n[service_user]\n\n[spice]\n\n[ssl]\n\n[trusted_computing]\n\n[upgrade_levels]\n\n[vendordata_dynamic_auth]\n\n[vmware]\n\n[vnc]\n\nvnc_enabled = True\nvncserver_listen = 0.0.0.0\nvncserver_proxyclient_address = "+commanagementIp+"		\nnovncproxy_base_url = http://"+comconip+":6080/vnc_auto.html\n\n[workarounds]\n\n[wsgi]\n\napi_paste_config=/etc/nova/api-paste.ini\n\n[xenserver]\n\n[xvp]\n"
	saveFile = open('/etc/nova/nova.conf','w')
	saveFile.write(novaConfig)
	saveFile.close()
	novacomConfig = "[DEFAULT]\n compute_driver=libvirt.LibvirtDriver\n [libvirt]\n virt_type=qemu\n"
	savefile = open('/etc/nova/nova-compute.conf','w')
	savefile.write(novacomConfig)
	savefile.close()
	os.system("service nova-compute restart")
	status()

def main():
	prereq()
	neutronproc()
	novaproc()

main()
