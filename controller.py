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

def menu():
	print(" MENU [ blank for all ]")
	print(" 1. Basic Configuration ")
	print(" 2. Installation of Mysql and RabbitMQ ")
	print(" 3. Installation and configuration of keystone ")
	print(" 4. Installation and configuration of Glance ")
	print(" 5. Installation and configuration of Neutron ")
	print(" 6. Installation and configuration of Nova ")
	print(" 7. Installation of Horizon : ")
	print(" Exit")

menu()
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
#def prereq():
#	print(" Runnig basic configuration ")
#	os.system("apt update -y -qq")
#	os.system("apt upgrade -y -qq")
#	os.system("apt install chrony -y -qq")
#	os.system("apt install openssh-server -y ")
#	os.system("apt install python-mysqldb -y")
#	os.system("sudo apt-get install python3-pip -y")
#	os.system("sudo pip3 install PyMySQL")
#	os.system("apt install software-properties-common -y ")
#	os.system("add-apt-repository cloud-archive:ocata -y")
#	os.system("apt install python-openstackclient -y")
#	os.system("apt update -y && apt dist-upgrade -y")
#	os.system("apt install python-pymysql -y")
#	os.system("apt install python-openstackclient -y")
#	os.system("apt-get install -y openvswitch-switch")
#	os.system("ovs-vsctl add-br br-ex")
#	os.system("apt install vim -y")
	#print(" Enter the details ") 
	#contimes()
	#comtimes()
#	os.system("cp /etc/hosts /etc/hosts.old")
#	os.system("cat hosts >> /etc/hosts")
#	os.system("cat /etc/hosts")
#	os.system("sudo sed -i -re 's/ubuntu/controller/g' /etc/hostname ")
#	print("\n")
#	status()
#	os.system("cat /etc/hostname")
#	print("\n")
#	os.system("ip a")	
#	os.system("cp /etc/network/interfaces /etc/network/interface.old")
#	os.system("rm /etc/network/interfaces")
#	status()
#	interfaceConfig()
#	os.system("cat /etc/network/interfaces")
#	os.system(bridgeCreation)
#	os.system("sudo sed -i -re 's/#net.ipv4.conf.default.rp_filter=1/net.ipv4.conf.default.rp_filter=0/g' /etc/sysctl.conf ")	
#	os.system("sudo sed -i -re 's/#net.ipv4.conf.all.rp_filter=1/net.ipv4.conf.all.rp_filter=0/g' /etc/sysctl.conf ")
#	os.system("sudo sed -i -re 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf ")
#	status()
#	os.system("sysctl -p ")
#	status()
##	useless = input("Machine will restart now and Run the script for Installation and configuration of Mysql and RabbitMQ ( Enter to confirm ) ")
	#os.system("init 6")
#	os.system("ip addr flush ens33 && systemctl restart networking.service")
#	os.system("ip addr flush ens34 && systemctl restart networking.service")
#	mymyq()

#Installation of Mysql and RabbitMQ Server
def mymq():
	print(" Running Installation of Mysql and RabbitMQ ")
	os.system(" apt install mariadb-server python-pymysql -y ")
	mysqlContent= "[mysqld] \nbind-address = 0.0.0.0 \n \ndefault-storage-engine = innodb \ninnodb_file_per_table = on \n max_connections = 4096 \ncollation-server = utf8_general_ci \ncharacter-set-server = utf8\n"
	saveFile = open('/etc/mysql/mariadb.conf.d/99-openstack.cnf','w')
	saveFile.write(mysqlContent)
	saveFile.close()
	status()
	os.system("service mysql restart ")
	#print("Installation of the mysql, Configure the database as your requirement")
	#os.system("mysql_secure_installation")
	mysqlInstall = "#!/bin/bash \nmysql_secure_installation <<EOF \nn \nroot \nroot \ny \ny \ny \ny \ny \nEOF \n"
	saveFile = open('temp.sh','w')
	saveFile.write(mysqlInstall)
	saveFile.close()
	os.system("chmod a+x temp.sh")
	os.system("./temp.sh")
	os.system("rm temp.sh")
	os.system("apt install rabbitmq-server -y")
	os.system("rabbitmqctl add_user openstack rabbit")
	status()
	os.system(" rabbitmqctl set_permissions openstack \".*\" \".*\" \".*\" ")
	status()
	os.system("apt install memcached python-memcache -y")
	os.system("sudo sed -i -re 's/127.0.0.1/0.0.0.0/g' /etc/memcached.conf ")
	status()
	os.system("service memcached restart")
	keystone()
	
def need():
	
	global controllerIp1
	global managementIp1
	controllerIp1 = controllerIp
	managementIp1 = conmanagementIp
		
def creds():
#       global permission
#       global permission1
#       global permission2
#       global permission3
#       global permission4
        global permission5
#       global permission6
#       permission = "export OS_USERNAME=admin"
#       permission1 = "export OS_PASSWORD=admin_pass"
#       permission2 = "export OS_PROJECT_NAME= admin"
#       permission3 = "export OS_USER_DOMAIN_NAME=Default"
#       permission4 = "export OS_PROJECT_DOMAIN_NAME=Default"
        permission5 = "http://" + controllerIp1 + ":5000/v3"
#       permission6 = "export OS_IDENTITY_API_VERSION=3"
        #os.system(permission)
        #os.system(permission1)
        #os.system(permission2)
        #os.system(permission3)
        #os.system(permission4)
        #os.system(permission5)
        #os.system(permission6)
        os.environ["OS_USERNAME"] = "admin"
        os.environ["OS_PASSWORD"] = "admin_pass"
        os.environ["OS_PROJECT_NAME"] = "admin"
        os.environ["OS_USER_DOMAIN_NAME"] = "Default"
        os.environ["OS_PROJECT_DOMAIN_NAME"] = "Default"
        os.environ["OS_AUTH_URL"] = permission5
        os.environ["OS_IDENTITY_API_VERSION"] = "3"


def keypro():
	dbfunc()
	cur.execute("CREATE DATABASE keystone; ")
	cur.execute("GRANT ALL ON keystone.* TO 'keystoneUser'@'%' IDENTIFIED BY 'keystonePass'; ")
#	cur.execute("quit; ")
	#print("Copy paste these commands in mysql and login with password : root \n")
	#print("CREATE DATABASE keystone; \n")
#	print("GRANT ALL ON keystone.* TO 'keystoneUser'@'%' IDENTIFIED BY 'keystonePass'; \n")
#	print("quit; \n")
	#os.system("apt install python-openstackclient -y")
#	os.system("mysql -u root -p")
	#con1 = 'connection = mysql+pymysql://keystoneUser:keystonePass@'+ managementIp1 +'/keystone'
	#os.system("sudo sed -i -re 's/[database]/[database]\n"+con1+"/g' /etc/keystone/keystone.conf ")
	#os.system("sudo sed -i -re 's/#provider = fernet/provider = fernet/g' /etc/keystone/keystone.conf ")
	keyconf = "\n[DEFAULT]\n[assignment]\n[auth]\n[cache]\n[catalog]\n[cors]\n[cors.subdomain]\n[credential]\n[database]\nconnection = mysql+pymysql://keystoneUser:keystonePass@"+ managementIp1 +"/keystone\n[domain_config]\n[endpoint_filter]\n[endpoint_policy]\n[eventlet_server]\n[extra_headers]\n[federation]\n[fernet_tokens]\n[healthcheck]\n[identity]\n[identity_mapping]\n[kvs]\n[ldap]\n[matchmaker_redis]\n[memcache]\n[oauth1]\n[oslo_messaging_amqp]\n[oslo_messaging_kafka]\n[oslo_messaging_notifications]\n[oslo_messaging_rabbit]\n[oslo_messaging_zmq]\n[oslo_middleware]\n[oslo_policy]\n[paste_deploy]\n[policy]\n[profiler]\n[resource]\n[revoke]\n[role]\n[saml]\n[security_compliance]\n[shadow_users]\n[signing]\n[token]\nprovider = fernet\n[tokenless_auth]\n[trust]\n"
	#os.system("sudo sed -i -re 's/[database]/[database]\n"+con1+"/g' /etc/keystone/keystone.conf ")
	#os.system("sudo sed -i -re 's/#provider = fernet/provider = fernet/g' /etc/keystone/keystone.conf ")
	saveFile = open('/etc/keystone/keystone.conf','w')
	saveFile.write(keyconf)
	saveFile.close()
	status()
	os.system("su -s /bin/sh -c \"keystone-manage db_sync\" keystone")
	os.system("keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone")
	os.system("keystone-manage credential_setup --keystone-user keystone --keystone-group keystone")
	command1 = "keystone-manage bootstrap --bootstrap-password admin_pass --bootstrap-admin-url http://"+managementIp1+":35357/v3/ --bootstrap-internal-url http://"+managementIp1+":35357/v3/ --bootstrap-public-url http://"+controllerIp1+":5000/v3/ --bootstrap-region-id RegionOne"
	os.system(command1)
#	credFile= "export OS_USERNAME=admin \nexport OS_PASSWORD=admin_pass\nexport OS_PROJECT_NAME=admin\nexport OS_USER_DOMAIN_NAME=Default\nexport OS_PROJECT_DOMAIN_NAME=Default\nexport OS_AUTH_URL=http://"+controllerIp1+":35357/v3\nexport OS_IDENTITY_API_VERSION=3"
#	saveFile = open('creds','w')
#	saveFile.write(credFile)
#	saveFile.close()	
#	os.system("sudo -s")
#	os.system("source creds")
#	os.system("source creds")
	creds()
	os.system("openstack project create --domain default --description \"Service Project\" service")
	os.system("openstack project create --domain default --description \"Demo Project\" demo")
	os.system("openstack user create --domain default --password demo_pass demo")
	os.system("openstack role create user")
	os.system("openstack role add --project demo --user demo user")
	democredFile= "export OS_PROJECT_DOMAIN_NAME=default \n export OS_USER_DOMAIN_NAME=default \n export OS_PROJECT_NAME=demo \n export OS_USERNAME=demo \n export OS_PASSWORD=demo_pass \n export OS_AUTH_URL=http://" + controllerIp1 + ":5000/v3 \nexport OS_IDENTITY_API_VERSION=3 \n export OS_IMAGE_API_VERSION=2"
	saveFile = open('/home/ubuntu/democreds','w')
	saveFile.write(democredFile)
	saveFile.close()
	status()
	os.system("openstack user list")
	glance()

def keystone():
#	global controllerIp1
#	global managementIp1
	print(" Running Installation of Keystone ")
	os.system("apt install python-pip -y")
	os.system("apt install python3-pip -y")
	os.system("pip install PyMySQL")
	os.system("pip3 install PyMySQL")
	os.system("pip install --upgrade pip")
	os.system("apt install keystone -y")
	os.system("sudo apt-get install python3-mysqldb -y")
	need()
#	controllerIp1 = input("Enter the controller Ip ( example : 192.168.0.35 ) : ")
#	managementIp1 = input("Enter the Management Ip ( example : 100.100.100.35 ) : ")
	keypro()

def glanceproc():
	creds()
	status()
	os.system("openstack user create --domain default --password service_pass glance")
	os.system("openstack role add --project service --user glance admin")
	os.system("openstack service create --name glance --description \"OpenStack Image service\" image")	
	glancepublic = "openstack endpoint create --region RegionOne image public http://" + controllerIp1 + ":9292"
	glanceinternal = "openstack endpoint create --region RegionOne image internal http://" + managementIp1 + ":9292"
	glanceadmin = "openstack endpoint create --region RegionOne image admin http://"+ managementIp1 +":9292"
	os.system(glancepublic)
	os.system(glanceinternal)
	os.system(glanceadmin)
	os.system("apt install glance -y")
#	print("Copy paste these commands in mysql and login with password : root \n\n")
#	print("CREATE DATABASE glance; \nGRANT ALL ON glance.* TO 'glanceUser'@'%' IDENTIFIED BY 'glancePass'; \n\nquit;")
#	os.system("mysql -u root -p")
	dbfunc()
	cur.execute("CREATE DATABASE glance; ")
	cur.execute("GRANT ALL ON glance.* TO 'glanceUser'@'%' IDENTIFIED BY 'glancePass'; ")
	os.system("rm /etc/glance/glance-api.conf")
	os.system("rm /etc/glance/glance-registry.conf")
	glanceApi = "[DEFAULT]\n[cors]\n[cors.subdomain]\n[database]\nconnection = mysql+pymysql://glanceUser:glancePass@"+managementIp1+"/glance\nbackend = sqlalchemy\n[glance_store]\nstores = file,http\ndefault_store = file\nfilesystem_store_datadir = /var/lib/glance/images/ \n[image_format]\ndisk_formats = ami,ari,aki,vhd,vhdx,vmdk,raw,qcow2,vdi,iso,ploop.root-tar\n[keystone_authtoken]\nauth_uri = http://"+managementIp1+":5000\nauth_url = http://"+managementIp1+":35357\nmemcached_servers = "+managementIp1+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = glance\npassword = service_pass\n[matchmaker_redis]\n[oslo_concurrency]\n[oslo_messaging_amqp]\n[oslo_messaging_kafka]\n[oslo_messaging_notifications]\n[oslo_messaging_rabbit]\n[oslo_messaging_zmq]\n[oslo_middleware]\n[oslo_policy]\n[paste_deploy]\nflavor = keystone\n[profiler]\n[store_type_location_strategy]\n[task]\n[taskflow_executor]\n"
	saveFile = open('/etc/glance/glance-api.conf','w')
	saveFile.write(glanceApi)
	saveFile.close()	
	glanceRegistry = "[DEFAULT]\n[database]\nconnection = mysql+pymysql://glanceUser:glancePass@"+managementIp1+"/glance\nbackend = sqlalchemy\n[keystone_authtoken]\nauth_uri = http://"+managementIp1+":5000\nauth_url = http://"+managementIp1+":35357\nmemcached_servers = "+managementIp1+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = glance\npassword = service_pass\n[matchmaker_redis]\n[oslo_messaging_amqp]\n[oslo_messaging_kafka]\n[oslo_messaging_notifications]\n[oslo_messaging_rabbit]\n[oslo_messaging_zmq]\n[oslo_policy]\n[paste_deploy]\nflavor = keystone\n[profiler]\n"
	saveFile = open('/etc/glance/glance-registry.conf','w')	
	saveFile.write(glanceRegistry)
	saveFile.close()
	os.system("su -s /bin/sh -c \"glance-manage db_sync\" glance")
	os.system("service glance-registry restart")
	os.system("service glance-api restart")
	os.system("wget http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img")
	os.system("openstack image create \"cirros\"  --file cirros-0.3.4-x86_64-disk.img --disk-format qcow2 --container-format bare --public")
	os.system("openstack image list")
	neutron()	

def glance():
	print("Running Installation of Glance \n")	
	need()
	creds()
	glanceproc()	

def neutronproc():
	creds()
	os.system("openstack user create --domain default --password service_pass neutron")
	os.system("openstack role add --project service --user neutron admin")
	os.system("openstack service create --name neutron --description \"OpenStack Networking\" network")
	os.system("openstack endpoint create --region RegionOne network public http://"+controllerIp1+":9696")
	os.system("openstack endpoint create --region RegionOne network internal http://"+managementIp1+":9696")
	os.system("openstack endpoint create --region RegionOne network admin http://"+managementIp1+":9696")
	os.system("apt-get install neutron-server neutron-dhcp-agent neutron-plugin-openvswitch-agent neutron-l3-agent dnsmasq python-neutronclient -y")
	dbfunc()
	cur.execute("CREATE DATABASE neutron;")
	cur.execute("GRANT ALL ON neutron.* TO 'neutronUser'@'%' IDENTIFIED BY 'neutronPass';")	
#	cur.execute("quit;")
	os.system("service neutron-server restart")
	os.system("service neutron-openvswitch-agent restart;")
	os.system("service neutron-metadata-agent restart;")
	os.system("service neutron-dhcp-agent restart;")
	os.system("service neutron-l3-agent restart;")
	os.system("rm /etc/neutron/l3_agent.ini")
	os.system("rm /etc/neutron/dhcp_agent.ini")
	os.system("rm /etc/neutron/plugins/ml2/ml2_conf.ini")
	os.system("rm /etc/neutron/plugins/ml2/openvswitch_agent.ini")
	os.system("rm /etc/neutron/metadata_agent.ini")
	os.system("rm /etc/neutron/neutron.conf")
	l3AgentConfig = "[DEFAULT]\ninterface_driver = neutron.agent.linux.interface.OVSInterfaceDriver\nexternal_network_bridge =  br-ex\nrouter_delete_namespaces = True\nverbose = True\n[agent]\n[ovs]\n"
	saveFile = open('/etc/neutron/l3_agent.ini','w')
	saveFile.write(l3AgentConfig)
	saveFile.close()
	dhcpAgentConfig = "[DEFAULT]interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver  \ndhcp_driver = neutron.agent.linux.dhcp.Dnsmasq\nverbose = True\nenable_isolated_metadata = True\n[agent][ovs]"
	saveFile = open('/etc/neutron/dhcp_agent.ini','w')
	saveFile.write(dhcpAgentConfig)
	saveFile.close()
	ml2Config = "[DEFAULT]\nverbose = true\n[ml2]\ntype_drivers = vxlan\ntenant_network_types = vxlan\nmechanism_drivers = openvswitch,l2population\nextension_drivers = port_security\n[ml2_type_flat]\n[ml2_type_geneve]\n[ml2_type_gre]\n[ml2_type_vlan]\n[ml2_type_vxlan]\nvni_ranges = 1:2000\nvxlan_group = 239.1.1.1\n[securitygroup]\nenable_ipset = true \n"
	saveFile = open('/etc/neutron/plugins/ml2/ml2_conf.ini','w')
	saveFile.write(ml2Config)
	saveFile.close()
	openvswitchAgentConfig = "[DEFAULT]\nverbose = true\n[agent]\ntunnel_types = vxlan\nl2population = True\n\n[ovs]\nlocal_ip = "+managementIp1+"\nbridge_mappings = external:br-ex\nenable_tunneling = True\nvxlan_udp_port = 4789\ntunnel_types = vxlan\ntunnel_id_ranges = 1:2000\ntunnel_network_types = vxlan\n\n[securitygroup]\nfirewall_driver = neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver\nenable_security_group = True\n\n[xenapi]\n\n"
	saveFile = open('/etc/neutron/plugins/ml2/openvswitch_agent.ini','w')
	saveFile.write(openvswitchAgentConfig)
	saveFile.close()
	metadataAgentConfig = "[DEFAULT]\n# The Neutron user information for accessing the Neutron API.\nauth_uri = http://"+managementIp1+":5000\nauth_url = http://"+managementIp1+":35357\nmemcached_servers = "+managementIp1+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = neutron\npassword = service_pass\nnova_metadata_ip = "+managementIp1+"\nmetadata_proxy_shared_secret = mystack\nverbose = True  \n\n[agent]\n\n[cache]\n\n"
	saveFile = open('/etc/neutron/metadata_agent.ini','w')
	saveFile.write(metadataAgentConfig)
	neutronConfig = "[DEFAULT]\ncore_plugin = ml2\nservice_plugins = router\nallow_overlapping_ips = true\nverbose = true\nauth_strategy = keystone\ntransport_url = rabbit://openstack:rabbit@"+managementIp1+"\nnotify_nova_on_port_status_changes = True\nnotify_nova_on_port_data_changes = True\n\n[agent]\n\nroot_helper = sudo /usr/bin/neutron-rootwrap /etc/neutron/rootwrap.conf\n\n[cors]\n\n[cors.subdomain]\n\n[database]\nconnection = mysql+pymysql://neutronUser:neutronPass@"+managementIp1+"/neutron\n[keystone_authtoken]\nauth_uri = http://"+managementIp1+":5000\nauth_url = http://"+managementIp1+":35357\nmemcached_servers = "+managementIp1+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = neutron\npassword = service_pass\n\n[matchmaker_redis]\n\n[nova]\nauth_url = http://"+managementIp1+":35357\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nregion_name = RegionOne\nproject_name = service\nusername = nova\npassword = service_pass\n\n[oslo_concurrency]\nlock_path = /var/lib/neutron/tmp\n[oslo_messaging_amqp]\n\n[oslo_messaging_kafka]\n\n[oslo_messaging_notifications]\n\n[oslo_messaging_rabbit]\n\n[oslo_messaging_zmq]\n\n[oslo_middleware]\n\n[oslo_policy]\n\n[qos]\n\n[quotas]\n\n[ssl]\n\n"
	saveFile = open('/etc/neutron/neutron.conf','w')
	saveFile.write(neutronConfig)
	saveFile.close()
	os.system("service neutron-server restart;")
	os.system("service neutron-openvswitch-agent restart;")
	os.system("service neutron-metadata-agent restart;")
	os.system("service neutron-dhcp-agent restart;")
	os.system("service neutron-l3-agent restart;")
	os.system("service dnsmasq restart;")
	os.system("su -s /bin/sh -c \"neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head\" neutron")
	os.system("openstack network agent list")
	nova()

def novaproc():
	creds()
	os.system("openstack user create --domain default --password service_pass nova")
	os.system("openstack role add --project service --user nova admin")
	os.system("openstack service create --name nova --description \"OpenStack Compute\" compute")
	novaPublic = "openstack endpoint create --region RegionOne compute public http://"+controllerIp1+":8774/v2.1"
	novaInternal = "openstack endpoint create --region RegionOne compute internal http://"+managementIp1+":8774/v2.1"
	novaAdmin = "openstack endpoint create --region RegionOne compute admin http://"+managementIp1+":8774/v2.1"
	os.system(novaPublic)
	os.system(novaInternal)
	os.system(novaAdmin)
	os.system("openstack user create --domain default --password service_pass placement")
	os.system("openstack role add --project service --user placement admin")
	os.system("openstack service create --name placement --description \"OpenStack Compute\" placement")
	placementPublic = "openstack endpoint create --region RegionOne placement public http://"+controllerIp1+":8778"
	placementInternal = "openstack endpoint create --region RegionOne placement internal http://"+managementIp1+":8778"
	placementAdmin = "openstack endpoint create --region RegionOne placement admin http://"+managementIp1+":8778"
	os.system("apt-get install nova-api nova-cert nova-conductor nova-consoleauth nova-novncproxy nova-scheduler python-novaclient nova-console -y")
	os.system("apt install nova-placement-api -y")
	dbfunc()
	cur.execute("CREATE DATABASE nova;")
	cur.execute("GRANT ALL ON nova.* TO 'novaUser'@'%' IDENTIFIED BY 'novaPass';")
	cur.execute("CREATE DATABASE nova_api;")
	cur.execute("GRANT ALL ON nova_api.* TO 'novaUser'@'%' IDENTIFIED BY 'novaPass';")
	cur.execute("CREATE DATABASE nova_cell0;")
	cur.execute("GRANT ALL ON nova_cell0.* TO 'novaUser'@'%' IDENTIFIED BY 'novaPass';")
	novaConfig = "[DEFAULT]\ndhcpbridge_flagfile=/etc/nova/nova.conf\ndhcpbridge=/usr/bin/nova-dhcpbridge\nforce_dhcp_release=true\nstate_path=/var/lib/nova\nenabled_apis=osapi_compute,metadata \nmy_ip = "+managementIp1+"\nuse_neutron = True\nfirewall_driver = nova.virt.firewall.NoopFirewallDriver\ntransport_url = rabbit://openstack:rabbit@"+managementIp1+"\n\n\nlog_dir=/var/log/nova\n[api]\nauth_strategy = keystone\n[api_database]\nconnection=mysql+pymysql://novaUser:novaPass@"+managementIp1+"/nova_api\n[barbican]\n[cache]\n[cells]\nenable=False\n[cinder]\nos_region_name = RegionOne\n[cloudpipe]\n[conductor]\n[console]\n[consoleauth]\n[cors]\n[cors.subdomain]\n[crypto]\n[database]\nconnection=mysql+pymysql://novaUser:novaPass@"+managementIp1+"/nova\n[ephemeral_storage_encryption]\n[filter_scheduler]\n[glance]\napi_servers = http://"+managementIp1+":9292\n[guestfs]\n[healthcheck]\n[hyperv]\n[image_file_url]\n[ironic]\n[key_manager]\n[keystone_authtoken]\nauth_uri = http://"+managementIp1+":5000\nauth_url = http://"+managementIp1+":35357\nmemcached_servers = "+managementIp1+":11211\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nproject_name = service\nusername = nova\npassword = service_pass\n\n[libvirt]\n[matchmaker_redis]\n[metrics]\n[mks]\n[neutron]\nservice_metadata_proxy = True\nmetadata_proxy_shared_secret = mystack\nurl = http://"+managementIp1+":9696\nauth_url = http://"+managementIp1+":35357\nauth_type = password\nproject_domain_name = default\nuser_domain_name = default\nregion_name = RegionOne\nproject_name = service\nusername = neutron\npassword = service_pass\n\n[notifications]\n[osapi_v21]\n[oslo_concurrency]\nlock_path = /var/lib/nova/tmp\n[oslo_messaging_amqp]\n[oslo_messaging_kafka]\n[oslo_messaging_notifications]\n[oslo_messaging_rabbit]\n[oslo_messaging_zmq]\n[oslo_middleware]\n[oslo_policy]\n[pci]\n[placement]\nos_region_name = RegionOne\nproject_domain_name = Default\nproject_name = service\nauth_type = password\nuser_domain_name = Default\nauth_url = http://"+managementIp1+":35357/v3\nusername = placement\npassword = service_pass\n\n\n[quota]\n[rdp]\n[remote_debug]\n[scheduler]\n[serial_console]\n[service_user]\n[spice]\n[ssl]\n[trusted_computing]\n[upgrade_levels]\n[vendordata_dynamic_auth]\n[vmware]\n[vnc]\nvnc_enabled = True\nvncserver_listen = 0.0.0.0\nvncserver_proxyclient_address = "+managementIp1+"\nnovncproxy_base_url = http://"+controllerIp1+":6080/vnc_auto.html\n\n\n[workarounds]\n[wsgi]\napi_paste_config=/etc/nova/api-paste.ini\n[xenserver]\n[xvp]\n"
	saveFile = open('/etc/nova/nova.conf','w')
	saveFile.write(novaConfig)
	saveFile.close()
	os.system("su -s /bin/sh -c \"nova-manage api_db sync\" nova")	
	status()
	os.system("su -s /bin/sh -c \"nova-manage cell_v2 map_cell0\" nova")
	status()
	os.system("su -s /bin/sh -c \"nova-manage cell_v2 create_cell --name=cell1 --verbose\" nova")
	status()
	os.system("su -s /bin/sh -c \"nova-manage db sync\" nova")
	status()
	os.system("nova-manage cell_v2 list_cells")
	os.system("service nova-api restart")
	os.system("service nova-consoleauth restart")
	os.system("service nova-scheduler restart")
	os.system("service nova-conductor restart")
	os.system("service nova-novncproxy restart")
	os.system("openstack compute service list")
	status()
	horizon()

def horizonproc():
	os.system("apt-get install openstack-dashboard -y")
	with open('/etc/openstack-dashboard/local_settings.py', 'r') as myfile:
		data=myfile.read().replace('OPENSTACK_HOST = "127.0.0.1"', 'OPENSTACK_HOST = "'+str(controllerIp1)+'"')
		data=data.replace('OPENSTACK_KEYSTONE_URL = "http://%s:5000/v2.0" % OPENSTACK_HOST', 'OPENSTACK_KEYSTONE_URL = "http://%s:5000/v3" % OPENSTACK_HOST')
		data=data.replace('OPENSTACK_KEYSTONE_DEFAULT_ROLE = "_member_"', 'OPENSTACK_KEYSTONE_DEFAULT_ROLE = "user"')
		data=data.replace('CACHES = {\n    \'default\': {\n        \'BACKEND\': \'django.core.cache.backends.memcached.MemcachedCache\',\n        \'LOCATION\': \'127.0.0.1:11211\',\n    },\n}', 'SESSION_ENGINE = \'django.contrib.sessions.backends.cache\'\n\nCACHES = {\n    \'default\': {\n         \'BACKEND\': \'django.core.cache.backends.memcached.MemcachedCache\',\n         \'LOCATION\': \''+managementIp1+':11211\',\n    }\n}\n')	
		data=data.replace('#OPENSTACK_API_VERSIONS = {\n#    "data-processing": 1.1,\n#    "identity": 3,\n#    "image": 2,\n#    "volume": 2,\n#    "compute": 2,\n#}', 'OPENSTACK_API_VERSIONS = {\n    "data-processing": 1.1,\n    "identity": 3,\n    "volume": 2,\n    "compute": 2,\n}\n')
		data=data.replace('#OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = \'Default\'', 'OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = \'default\'')

	with open('/etc/openstack-dashboard/local_settings.py','w') as editfile:
		editfile.write(data)
	os.system("chown www-data /var/lib/openstack-dashboard/secret_key")
	os.system("service apache2 reload;")
	print("You can access openstack dashboard by visiting "+controllerIp1+"/horizon")
	print("Username : admin")
	print("Password : admin_pass")

def horizon():
	print("\nRunning Installation of Horizon\n")
	need()
	creds()
	horizonproc()	

def nova():
	print("Running Installation of Nova \n")
	need()
	creds()
	novaproc()	

def neutron():
	print("Running Installation of Neutron \n")
	need()
	creds()
	neutronproc()



#prereq()
mymq()
keystone()
glance()
neutron()
nova()
horizon()
#menu1 = input("\nSelect from the menu above ")
#if menu1 =="":
#	prereq()
#
#elif menu1 =="1":
#	print("\nBasic Configuration selected ")
#	prereq()

#elif menu1 =="2":
#	print("\nInstallation of Mysql and RabbitMQ selected ")
#	mymq()
#
#if menu1 =="3":
#	print("\nInstallation of Keystone selected ")
#	keystone()
#
#if menu1 =="4":
#	print("\nInstallation of Glance selected ")
#	glance()
#
#if menu1 =="5":
#	print("\nInstallation of Neutron selected ")
#	neutron()
#if menu1 =="6":
#	print("\nInstallation of Nova Selected ")
#	nova()
#if menu1 =="7":
#	print("\nInstallation of Horizon Selected ")
#	horizon()
