#!/usr/bin/python
import os
import re
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
print("                                         Project Nightfall                                          ")
print("   AN AUTOMATED SCRIPT FOR INSTALLATION OF OPENSTACK OCATA MULTI-NODE ON UBUNTU [ ON A NETWORK ]    ")
print("            NOT TO BE USED AT PRODUCTION SITE [ NOT MEANT TO STEAL SOMEONE'S JOB ]                  ")
print("                                BY MEGHA BANERJEE AND MANOJ C CHOUDHARY                             ")
print("			This script is for basic configuration requirements of openstack 		   ")
print("						Running Script now					   ")
def menu():
	print("Menu")
	print("1.To create Controller and Compute Node script")
	print("2.Run Controller node installation")
	print("3.Run Compute node installation")
	print("4.Sync Compute node to Controller nodes")
	print("Press any to exit")
#	askmenu = input("Enter your choice : ")
#	if int(askmenu) == int("1"):
#		whencalled()
#	if int(askmenu) == int("2"):
#		installcon()
#	if int(askmenu) == int("3"):
#		installcom()
#	if int(askmenu) == int("4"):
#		sync()
#	if int(askmenu) == "":
#		menu()

def getdata():
#	global controllerIp
#	global conmanagementIp
#	global commanagementIp
#	global computeIp
	global netmask 
#	global gateway
	#netmask  = "255.255.255.0"
		

def comtimes():
	getdata()
	global computeIp
	global computeName
	global ComputeFqdn
	computetimes = 0
	computetimes = input("Enter the number of computes hostname and ip to be configured : ")
	computecount = '\ncomputecount = ' + computetimes + '\n'
	appendFile = open('nightfallconfig.ini','a')
	appendFile.write(computecount)
	appendFile.close()
	count = 0
	while (count < int(computetimes) ):
		computeIp = input("Enter compute ip which you desire ( example : 192.168.0.36 ) : ")
		computeName = input("Enter compute name which you desire ( example : compute ) : ")
		computeFqdn = input("Enter compute fully qualified domain name ( example : compute.nightfall.com ) : ")
		commanagementIp = ""
		commanagementIp = input("Enter compute management Ip which you desire ( example : 10.10.100.36 ) : ")
		defgateway = input("Enter default gateway ( example : 192.168.0.1 ) : ")
		comcontrollerip = input("Enter the management ip of controller (example : 10.10.100.35 ) : ")
		comconip = input("Enter the ip of controller ( example : 192.168.0.35 ) : ")
		computetext = 'computeIp'+str(count)+' = '+str(computeIp)+'\n'+'computeFqdn'+str(count)+' = '+str(computeFqdn)+'\n'+'computeName'+str(count)+' = '+str(computeName)+'\n'+'managementIp'+str(count)+' = '+str(commanagementIp)+'\n'+'gateway'+str(count)+' = '+str(defgateway)+'\n'+'comcontrollerip'+str(count)+' = '+str(comcontrollerip)+'\n'
		computehosts = 'computehosts'+str(count)+' = '+computeIp +'\t'+computeFqdn+'\t\t'+computeName+'\n'
		computehostconfig = '\n'+computeIp + '\t' + computeFqdn + '\t\t' + computeName + '\n'
		createFile = open('hosts','a')
		createFile.write(computehostconfig)
		createFile.close()
		appendFile = open('nightfallconfig.ini','a')
		appendFile.write(computetext)
		appendFile.write(computehosts)
		appendFile.close()
		comconfig = "cp compute.py compute_"+computeIp+".py"
		textfile = "\n\tcomputeIp = \""+str(computeIp)+"\"\n\tcommanagementIp = \""+str(commanagementIp)+"\"\n\tcomputeFqdn = \""+str(computeFqdn)+"\"\n\tcomputeName = \""+str(computeName)+"\"\n\tcomgateway = \""+str(defgateway)+"\"\n\tcomnetmask = \""+str(netmask)+"\"\n\tcomcontrollerip = \""+str(comcontrollerip)+"\"\n\tcomconip = \""+str(comconip)+"\"\n"
		os.system(comconfig)
		with open('compute_'+computeIp+'.py','r') as myfile:
			data=myfile.read().replace('#iwillbereplaced=getconfig', '\n'+textfile+'\n')
		with open('compute_'+computeIp+'.py','w') as editfile:
			editfile.write(data)		
		count = count + 1	
			

def contimes():
	getdata()
	global controllerIp
	global controllerName
	global controllerFqdn
	controllertimes = 0
	controllertimes = input("Enter the number of controller hostname and ip to be configured : ")
	computecount = 'controllercount' + controllertimes
	appendFile = open('nightfallconfig.ini','a')
	appendFile.write(computecount)
	appendFile.close()
	count1 = 0
	while (count1 < int(controllertimes) ):
		controllertext = ""
		controllerIp = input("Enter ccntroller ip which you desire ( example : 192.168.0.35 ) : ")
		controllerName = input("Enter controller name which you desire ( example : controller ) : ")
		controllerFqdn = input("Enter controller fully qualified domain name ( example : controller.nightfall.com ) : ")
		conmanagementIp = ""
		conmanagementIp = input("Enter Controller management ip which you desire ( example : 10.10.100.35 ) : ")
		defgateway = input("Enter default gateway ( example : 192.168.0.1 ) : ")
		controllertext = 'controllerIp'+str(count1)+' = '+str(controllerIp)+'\n'+'controllerFqdn'+str(count1)+' = '+ str(controllerFqdn)+'\n'+'controllerName'+str(count1)+' = '+str(controllerName)+'\n'+'managementIp'+str(count1)+' = '+str(conmanagementIp)+'\n'+'gateway'+str(count1)+' = '+str(defgateway)+'\n'
		controllerhosts = 'controllerhosts'+str(count1)+' = '+controllerIp+'\t'+controllerFqdn+'\t\t'+controllerName+'\n'
		controllerhostconfig = '\n'+controllerIp+'\t'+controllerFqdn+'\t\t'+controllerName+'\n'
		editfile = open('hosts','a')
		editfile.write(controllerhostconfig)
		editfile.close()
		appendFile = open('nightfallconfig.ini','a')
		conconfig = "cp controller.py controller_"+controllerIp+".py"
		textfile1 = "\n\tcontrollerIp = \""+str(controllerIp)+"\"\n\tconmanagementIp = \""+str(conmanagementIp)+"\"\n\tcontrollerFqdn = \""+str(controllerFqdn)+"\"\n\tcontrollerName = \""+controllerName+"\"\n\tcongateway = \""+str(defgateway)+"\"\n\tconnetmask = \""+str(netmask)+"\"\n"
		appendFile.write(controllertext)
		appendFile.write(controllerhosts)
		appendFile.close()
		os.system(conconfig)
		with open('controller_'+controllerIp+'.py','r') as myfile1:
			data1=myfile1.read().replace('#iwillbereplaced=getconfig', '\n'+textfile1+'\n')
		with open('controller_'+controllerIp+'.py','w') as editfile1:
			editfile1.write(data1)
		count1 = count1 + 1

def whencalled():
#	os.system("apt install python-pip -y")
#	os.system("pip install paramiko ")
#	os.system("pip install --upgrade pip")
	getdata()
	hoststext="127.0.0.1       localhost\n127.0.1.1       ubuntu\n\n# The following lines are desirable for IPv6 capable hosts\n::1     localhost ip6-localhost ip6-loopback\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\n\n\n"
	hostsfile = open('hosts','w')
	hostsfile.write(hoststext)
	hostsfile.close()
	global netmask
	netmask = "255.255.255.0"
	header = "[controller_config]\nnetmask = "+netmask+"\n"
	appendFile = open('nightfallconfig.ini','w')
	appendFile.write(header)
	appendFile.close()
	contimes()
	print("                         Successfully Executed                           ")
	os.system("cat nightfallconfig.ini")
	getdata()
	netmask = "255.255.255.0"
	header1 = "\n\n[compute_config]\nnetmask = "+netmask+"\n"
	appendFile = open('nightfallconfig.ini','a')
	appendFile.write(header1)
	appendFile.close()
	comtimes()
	print("				Successfully Executed 				")
	os.system("cat nightfallconfig.ini")
	menu()

	
def prereq():
	os.system("apt install python-pip -y")
	os.system("pip3 install paramiko ")
	os.system("pip install --upgrade pip")
	os.system("pip3 install paramiko")

def ssh():
	import paramiko
	import getpass
	def sshCommand(hostname, port, username, password, command):
		sshClient = paramiko.SSHClient()
		sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		sshClient.load_system_host_keys()
		sshClient.connect(hostname, port, username, password)
		stdin, stdout, stderr = sshClient.exec_command(command , get_pty=True)
		#output = (stdout.read())
		#print(output)
		#for line in output:
		for line in iter(lambda: stdout.readline(2048), ""):
			print(line)

	global ip
	global user
	global passwd
	global command
	ip = input("Enter the ip of ssh server : ")
	user = input("Enter the username of server : ")
	passwd = getpass.getpass("Enter password : ")
	#sshCommand(ip, 22, user, passwd, command)

def installcon():
	import os
	import re
	search = "controller_\d+\.\d+\.\d+\.\d+.py"
	os.system("ls | grep controller_ | cat > check")
	with open('check','r') as checkfile:
		data=checkfile.read()
		newdata = re.findall(r'controller_\d+.\d+.\d+.\d+.py',data)
		if newdata:
			#print(newdata)
			def myloop():
				i = 0
				while i < len(newdata):
					print(i +" ]" +newdata[i])
					i += 1 
				option = input("Which Script to run : ")
				if option < len(newdata):
					myloop()
				else:
					scriptrun = (newdata[option])
					copyscript = "cp "+scriptrun+" /var/www/html/"+scriptrun
					os.system(copyscript)
					prereq()
					ssh()
					ipaddress = input("Enter your ")
					os.system("ip a | grep ens33 | cat > temp1")
					with open('temp1','r') as newf:
						data = newf.read()
						newdata = re.findall(r'inet \d+.\d+.\d+.\d+',data)

					with open('temp1','w') as newf:
						newf.write(newdata[0])
						newf.close()

					with open('temp1','r') as newf:
						data = newf.read()
						newdata = re.findall(r'\d+.\d+.\d+.\d+',data)
						ipaddress = (newdata[0])

					j = 0 
					atemp = "wget "+ipaddress+"/hosts"
					btemp = "wget "+ipaddress+"/nightfallconfig.ini"
					ctemp = "wget "+ipaddress+"/"+scriptrun
					dtemp = "python3 "+scriptrun
					command = ["cp hosts /var/www/html/hosts","sudo su","cp nightfallconfig.ini /var/www/html/nightfallconfig.ini","apt install wget -y",atemp,btemp,ctemp,dtemp]
					while j < len(command):
						ssh()
						sshCommand(ip, 22, user, passwd, command)		
						j += 1
					menu()
		else:
			print("No script found")
			menu()

def installcom():
	import os
	import re
	search = "compute_\d+\.\d+\.\d+\.\d+.py"
	os.system("ls | grep compute_ | cat > check")
	with open('check','r') as checkfile:
		data=checkfile.read()
		newdata = re.findall(r'compute_\d+.\d+.\d+.\d+.py',data)
		if newdata:
			#print(newdata)
			def myloop():
				i = 0
				while i < len(newdata):
					print(i +" ]" +newdata[i])
					i += 1 
				option = input("Which Script to run : ")
				if option < len(newdata):
					myloop()
				else:
					scriptrun = (newdata[option])
					copyscript = "cp "+scriptrun+" /var/www/html/"+scriptrun
					os.system(copyscript)
					prereq()
					ssh()
					ipaddress = input("Enter your ")
					os.system("ip a | grep ens33 | cat > temp1")
					with open('temp1','r') as newf:
						data = newf.read()
						newdata = re.findall(r'inet \d+.\d+.\d+.\d+',data)

					with open('temp1','w') as newf:
						newf.write(newdata[0])
						newf.close()

					with open('temp1','r') as newf:
						data = newf.read()
						newdata = re.findall(r'\d+.\d+.\d+.\d+',data)
						ipaddress = (newdata[0])

					j = 0 
					atemp = "wget "+ipaddress+"/hosts"
					btemp = "wget "+ipaddress+"/nightfallconfig.ini"
					ctemp = "wget "+ipaddress+"/"+scriptrun
					dtemp = "python3 "+scriptrun
					command = ["cp hosts /var/www/html/hosts","sudo su","cp nightfallconfig.ini /var/www/html/nightfallconfig.ini","apt install wget -y",atemp,btemp,ctemp,dtemp]
					while j < len(command):
						ssh()
						sshCommand(ip, 22, user, passwd, command)		
						j += 1
					menu()
		else:
			print("No script found")
			menu()

def sync():
	global controllerip
	controllerip = input("Enter Controller Ip  for compute node sync (example : 192.168.0.35 ) : ")
	text = "controllerip = \"" +controllerip+ "\""
	text1 = "cp sync.py sync_"+controllerip+".py" 
	os.system(text1)
	with open('sync_'+controllerip+'.py','r') as myfile:
		data=myfile.read().replace('#iwillbereplaced', '\n'+text+'\n')
	with open('sync_'+controllerip+'.py','w') as editfile:
		editfile.write(data)
	search = "sync_\d+\.\d+\.\d+\.\d+.py"
	os.system("ls | grep sync_ | cat > check")
	with open('check','r') as checkfile:
		data=checkfile.read()
		newdata = re.findall(r'sync_\d+.\d+.\d+.\d+.py',data)
		if newdata:
			#print(newdata)
			def myloop():
				i = 0
				while i < len(newdata):
					print(i + newdata[i])
					i += 1 
				option = input("Which Script to run : ")
				if option < len(newdata):
					myloop()
				else:
					scriptrun = (newdata[option])
					copyscript = "cp "+scriptrun+" /var/www/html/"+scriptrun
					os.system(copyscript)
					prereq()
					ssh()
					#ipaddress = input("Enter your ")
					os.system("ip a | grep ens33 | cat > temp1")
					with open('temp1','r') as newf:
						data = newf.read()
						newdata = re.findall(r'inet \d+.\d+.\d+.\d+',data)	
					with open('temp1','w') as newf:
						newf.write(newdata[0])
						newf.close()
					with open('temp1','r') as newf:
						data = newf.read()
						newdata = re.findall(r'\d+.\d+.\d+.\d+',data)
						ipaddress = (newdata[0])
					j = 0 
					ctemp = "wget "+ipaddress+"/"+scriptrun
					dtemp = "python3 "+scriptrun
					command = ["cp hosts /var/www/html/hosts","sudo su","cp nightfallconfig.ini /var/www/html/nightfallconfig.ini","apt install wget -y",ctemp,dtemp]
					while j < len(command):
						ssh()
						sshCommand(ip, 22, user, passwd, command)		
						j += 1
					menu()
		else:
			print("No script found")
			menu()	
	
	


#def menu():
#	print("Menu")
#	print("1.To create Controller and Compute Node script")
#	print("2.Run Controller node installation")
#	print("3.Run Compute node installation")
#	print("4.Sync Compute node to Controller nodes")
#	print("Press any to exit")
#
def ask():
	askmenu = input("Enter your choice : ")
	if int(askmenu) == int("1"):
		whencalled()
		ask()
	if int(askmenu) == int("2"):
		installcon()
		ask()
	if int(askmenu) == int("3"):
		installcom()
		ask()
	if int(askmenu) == int("4"):
		sync()
		ask()
menu()
ask()
