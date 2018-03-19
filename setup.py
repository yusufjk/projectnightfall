#!/usr/bin/python
import os
import re
import time
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
	print("5.Exit")
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

def status():
	os.system("if [ $? -eq 0 ]; then \n\t echo SUCCESS \n\telse \n\techo FAILED \n\texit\n\tfi")

def getdata():
#	global controllerIp
#	global conmanagementIp
#	global commanagementIp
#	global computeIp
	global netmask 
#	global gateway
	#netmask  = "255.255.255.0"
		
#os.system("rm nightfallconfig.ini")
#os.system("rm hosts")
#os.system("rm temp* ")
#os.system("rm check ")

def comtimes():
	getdata()
	global computeIp
	global computeName
	global ComputeFqdn
	computetimes = 0
	computetimes = input("Enter the number of computes hostname and ip to be configured : ")
	computecount = '\ncomputecount = ' + str(computetimes) + '\n'
	appendFile = open('nightfallconfig.ini','a')
	appendFile.write(computecount)
	appendFile.close()
	count = 0
	while (count < int(computetimes) ):
		computeIp = input("Enter compute ip which you desire ( example : 192.168.0.36 ) : ")
		computeName = input("Enter compute name which you desire ( example : compute"+str(count)+" ) : ")
		computeFqdn = input("Enter compute fully qualified domain name ( example : compute"+str(count)+".nightfall.com ) : ")
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
		comconfig1 = "cp comprereq.py comprereq_"+computeIp+".py"
		comconfig = "cp compute.py compute_"+computeIp+".py"
		textfile = "\n\tcomputeIp = \""+str(computeIp)+"\"\n\tcommanagementIp = \""+str(commanagementIp)+"\"\n\tcomputeFqdn = \""+str(computeFqdn)+"\"\n\tcomputeName = \""+str(computeName)+"\"\n\tcomgateway = \""+str(defgateway)+"\"\n\tcomnetmask = \""+str(netmask)+"\"\n\tcomcontrollerip = \""+str(comcontrollerip)+"\"\n\tcomconip = \""+str(comconip)+"\"\n"
		os.system(comconfig)
		os.system(comconfig1)
		with open('compute_'+computeIp+'.py','r') as myfile:
			data=myfile.read().replace('#iwillbereplaced=getconfig', '\n'+textfile+'\n')
		with open('compute_'+computeIp+'.py','w') as editfile:
			editfile.write(data)
		with open('comprereq_'+computeIp+'.py','r') as myfile2:
			data2=myfile2.read().replace('#iwillbereplaced=getconfig', '\n'+textfile+'\n')
		with open('comprereq_'+computeIp+'.py','w') as editfile2:
			editfile2.write(data2)		
		count = count + 1	
			

def contimes():
	getdata()
	global controllerIp
	global controllerName
	global controllerFqdn
	controllertimes = 0
	controllertimes = input("Enter the number of controller hostname and ip to be configured : ")
	controllercount = '\ncontrollercount = ' + str(controllertimes)
	appendFile = open('nightfallconfig.ini','a')
	appendFile.write(controllercount)
	appendFile.close()
	count1 = 0
	while (count1 < int(controllertimes) ):
		controllertext = ""
		controllerIp = input("Enter ccntroller ip which you desire ( example : 192.168.0.35 ) : ")
		controllerName = input("Enter controller name which you desire ( example : controller"+str(count1)+" ) : ")
		controllerFqdn = input("Enter controller fully qualified domain name ( example : controller"+str(count1)+".nightfall.com ) : ")
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
		conconfig1 = "cp conprereq.py conprereq_"+controllerIp+".py"
		conconfig2 = "cp sync.py sync_"+controllerIp+".py"
		textfile1 = "\n\tcontrollerIp = \""+str(controllerIp)+"\"\n\tconmanagementIp = \""+str(conmanagementIp)+"\"\n\tcontrollerFqdn = \""+str(controllerFqdn)+"\"\n\tcontrollerName = \""+controllerName+"\"\n\tcongateway = \""+str(defgateway)+"\"\n\tconnetmask = \""+str(netmask)+"\"\n"
		textfile2 = "controllerip = \""+str(controllerIp)+"\""
		appendFile.write(controllertext)
		appendFile.write(controllerhosts)
		appendFile.close()
		os.system(conconfig)
		os.system(conconfig1)
		os.system(conconfig2)
		with open('controller_'+controllerIp+'.py','r') as myfile1:
			data1=myfile1.read().replace('#iwillbereplaced=getconfig', '\n'+textfile1+'\n')
		with open('controller_'+controllerIp+'.py','w') as editfile1:
			editfile1.write(data1)
		with open('conprereq_'+controllerIp+'.py','r') as myfile4:
			data4=myfile4.read().replace('#iwillbereplaced=getconfig', '\n'+textfile1+'\n')
		with open('conprereq_'+controllerIp+'.py','w') as editfile4:
			editfile4.write(data4) 
		with open('sync_'+controllerIp+'.py', 'r') as syncfile:
			data5=syncfile.read().replace('#iwillbereplaced', '\n'+textfile2+'\n')
		with open('sync_'+controllerIp+'.py', 'w') as syncfile1:
			syncfile1.write(data5)
		count1 = count1 + 1

def whencalled():
#	os.system("apt install python-pip -y")
#	os.system("pip install paramiko ")
#	os.system("pip install --upgrade pip")
	getdata()
	hoststext="#This added by projectnightfall\n"
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
	os.system("apt install python3-pip -y")
#	os.system("pip3 install paramiko ")
	os.system("pip install --upgrade pip")
#	os.system("pip3 install paramiko")
	os.system("apt install apache2 -y")

#def ssh():
#	import paramiko
#	import getpass
#	def sshCommand(hostname, port, username, password, command):
#		sshClient = paramiko.SSHClient()
#		sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#		sshClient.load_system_host_keys()
#		sshClient.connect(hostname, port, username, password)
#		stdin, stdout, stderr = sshClient.exec_command(command , get_pty=True)
		#output = (stdout.read())
		#print(output)
		#for line in output:
#		for line in iter(lambda: stdout.readline(2048), ""):
#			print(line)

#	global ip
#	global user
#	global passwd
#	global command
#	ip = input("Enter the ip of ssh server : ")
#	user = input("Enter the username of server : ")
#	passwd = getpass.getpass("Enter password : ")
	#sshCommand(ip, 22, user, passwd, command)

def installcon():
	import os
	import time
	import re
	import getpass
	search = "controller_\d+\.\d+\.\d+\.\d+.py"
	os.system("ls | grep controller_ | cat > check")
	with open('check','r') as checkfile:
		data=checkfile.read()
		newdata = re.findall(r'controller_\d+.\d+.\d+.\d+.py',data)
		if len(newdata) > 0:
			#print(newdata)
			def conloop():
				i = 0
				while i < len(newdata):
					print(str(i) +" ) " +newdata[i])
					i += 1 
			conloop()
			option = input("Which Script to run : ")
			if int(option) < len(newdata):
				#myloop()
				#else: 
				scriptrun = (newdata[int(option)])
				print(scriptrun)
				copyscript = "cp "+scriptrun+" /var/www/html/"+scriptrun
				os.system(copyscript)
				status()
				prereq()
				scriptpre = re.findall(r'\d+.\d+.\d+.\d+',scriptrun)
				#print(scriptpre[0])
				conip = str(scriptpre[0])
				scriptpre1 = "conprereq_"+str(scriptpre[0])+".py"	
				#print(scriptpre1)
				copyscript1 = "cp "+scriptpre1+" /var/www/html/"+scriptpre1
				os.system(copyscript1)
#					ssh()
#					ipaddress = input("Enter your ")
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
				import paramiko
				j = 0 
				ip = input("Enter the ip address of the target : ")
				user = input("Enter the username of the target :  ")
				passwd = getpass.getpass("Enter target's password : ")
				temp1 = "cp hosts /var/www/html/hosts"
				temp2 = "cp nightfallconfig.ini /var/www/html/nightfallconfig.ini"
				#temp3 = 
				os.system(temp1)
				os.system(temp2)
				#temp3 = "apt install wget -y | cat > check && cat check"
				atemp = "wget "+ipaddress+"/hosts | cat > check1 && cat check1"
				btemp = "wget "+ipaddress+"/nightfallconfig.ini | cat > check2 && cat check2"
				ctemp = "wget "+ipaddress+"/"+scriptrun+" | cat > check3 && cat check3"
				dtemp = "wget "+ipaddress+"/"+scriptpre1+" | cat > check4 && cat check4"
#				dtemp = "sudo su - nightfall && python3 "+scriptrun+" | cat > check4 && cat check4"
#				command = ["cp hosts /var/www/html/hosts","sudo su","cp nightfallconfig.ini /var/www/html/nightfallconfig.ini","apt install wget -y",atemp,btemp,ctemp,dtemp]
				def sshCommand(hostname, port, username, password, command):
					sshClient = paramiko.SSHClient()
					sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					sshClient.load_system_host_keys()
					sshClient.connect(hostname, port, username, password)
					stdin, stdout, stderr = sshClient.exec_command(command , get_pty=True)
					for line in iter(lambda: stdout.readline(2048), ""):
							print(line)
#				ip = input("Enter the ip address of the target : ")
#				user = input("Enter the username of the target : ")
#				passwd = getpass.getpass("Enter target's password : ")
				#while j < len(command):
				#	ssh()
#				sshCommand(ip, 22, user, passwd, temp1)
#				sshCommand(ip, 22, user, passwd, temp2)
				sshCommand(ip, 22, user, passwd, dtemp)
				sshCommand(ip, 22, user, passwd, atemp)
				status()
				sshCommand(ip, 22, user, passwd, btemp)
				status()
				sshCommand(ip, 22, user, passwd, ctemp)
				status()
#=====> Add Lines Heres reminder for creater
				with open('temppass','w') as temppass:
					temppass.write(passwd)
					temppass.close()
				print("Enter the password for confirmation of target for security reasons : ")
				text1 = "ssh -t "+user+"@"+ip+" \"sudo python3 /home/ubuntu/"+scriptpre1+"\""
#				print(text1)
				os.system(text1)
			#	status()
				time.sleep(60)
				print("Enter the password for confirmation of target for security reasons : ")
				text2 = "ssh -t "+user+"@"+conip+" \"sudo python3 /home/ubuntu/"+scriptrun+"\""
				os.system(text2)
#				sshCommand(ip, 22, user, passwd, dtemp)	
				status()	
				os.system("rm check")
				os.system("rm temp1")
				#	j += 1
				menu()
			else:
				conloop()
		else:
			print("No script found")
			menu()

def installcom():
	import os
	import time
	import re
	import getpass
	search = "compute_\d+\.\d+\.\d+\.\d+.py"
	os.system("ls | grep compute_ | cat > check")
	with open('check','r') as checkfile:
		data=checkfile.read()
		newdata = re.findall(r'compute_\d+.\d+.\d+.\d+.py',data)
		if len(newdata) > 0:
			#print(newdata)
			def comloop():
				i = 0
				while i < len(newdata):
					print(str(i) +" ) " +newdata[i])
					i += 1 
			comloop()
			option = input("Which Script to run : ")
			if int(option) < len(newdata):
				#myloop()
				#else: 
				scriptrun = (newdata[int(option)])
				print(scriptrun)
				copyscript = "cp "+scriptrun+" /var/www/html/"+scriptrun
				os.system(copyscript)
				status()
				prereq()
				scriptpre = re.findall(r'\d+.\d+.\d+.\d+',scriptrun)
				#print(scriptpre[0])
				conip = str(scriptpre[0])
				scriptpre1 = "comprereq_"+str(scriptpre[0])+".py"	
				#print(scriptpre1)
				copyscript1 = "cp "+scriptpre1+" /var/www/html/"+scriptpre1
				os.system(copyscript1)
#					ssh()
#					ipaddress = input("Enter your ")
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
				import paramiko
				j = 0 
				ip = input("Enter the ip address of the target : ")
				user = input("Enter the username of the target :  ")
				passwd = getpass.getpass("Enter target's password : ")
				temp1 = "cp hosts /var/www/html/hosts"
				temp2 = "cp nightfallconfig.ini /var/www/html/nightfallconfig.ini"
				#temp3 = 
				os.system(temp1)
				os.system(temp2)
				#temp3 = "apt install wget -y | cat > check && cat check"
				atemp = "wget "+ipaddress+"/hosts | cat > check1 && cat check1"
				btemp = "wget "+ipaddress+"/nightfallconfig.ini | cat > check2 && cat check2"
				ctemp = "wget "+ipaddress+"/"+scriptrun+" | cat > check3 && cat check3"
				dtemp = "wget "+ipaddress+"/"+scriptpre1+" | cat > check4 && cat check4"
#				dtemp = "sudo su - nightfall && python3 "+scriptrun+" | cat > check4 && cat check4"
#				command = ["cp hosts /var/www/html/hosts","sudo su","cp nightfallconfig.ini /var/www/html/nightfallconfig.ini","apt install wget -y",atemp,btemp,ctemp,dtemp]
				def sshCommand(hostname, port, username, password, command):
					sshClient = paramiko.SSHClient()
					sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					sshClient.load_system_host_keys()
					sshClient.connect(hostname, port, username, password)
					stdin, stdout, stderr = sshClient.exec_command(command , get_pty=True)
					for line in iter(lambda: stdout.readline(2048), ""):
							print(line)
#				ip = input("Enter the ip address of the target : ")
#				user = input("Enter the username of the target : ")
#				passwd = getpass.getpass("Enter target's password : ")
				#while j < len(command):
				#	ssh()
#				sshCommand(ip, 22, user, passwd, temp1)
#				sshCommand(ip, 22, user, passwd, temp2)
				sshCommand(ip, 22, user, passwd, dtemp)
				sshCommand(ip, 22, user, passwd, atemp)
				status()
				sshCommand(ip, 22, user, passwd, btemp)
				status()
				sshCommand(ip, 22, user, passwd, ctemp)
				status()
#=====> Add Lines Heres reminder for creater
				with open('temppass','w') as temppass:
					temppass.write(passwd)
					temppass.close()
				print("Enter the password for confirmation of target for security reasons : ")
				text1 = "ssh -t "+user+"@"+ip+" \"sudo python3 /home/ubuntu/"+scriptpre1+"\""
#				print(text1)
				os.system(text1)
			#	status()
				time.sleep(60)
				print("Enter the password for confirmation of target for security reasons : ")
				text2 = "ssh -t "+user+"@"+conip+" \"sudo python3 /home/ubuntu/"+scriptrun+"\""
				os.system(text2)
#				sshCommand(ip, 22, user, passwd, dtemp)	
				status()	
				os.system("rm check")
				os.system("rm temp1")
				#	j += 1
				menu()
			else:
				comloop()
		else:
			print("No script found")
			menu()

def sync():
	#global controllerip
	import os
	import re
	import getpass
	search = "sync_\d+\.\d+\.\d+\.\d+.py"
	os.system("ls | grep sync_ | cat > check")
	with open('check','r') as checkfile:
		data=checkfile.read()
		newdata = re.findall(r'sync_\d+.\d+.\d+.\d+.py',data)
		if len(newdata) > 0:
			#print(newdata)
			def syncloop():
				i = 0
				while i < len(newdata):
					print(str(i) +" ) " +newdata[i])
					i += 1 
			syncloop()
			option = input("Which Script to run : ")
			if int(option) < len(newdata):
				#myloop()
				#else:
				scriptrun = (newdata[int(option)])
				copyscript = "cp "+scriptrun+" /var/www/html/"+scriptrun
				os.system(copyscript)
				status()
				prereq()
				scriptpre = re.findall(r'\d+.\d+.\d+.\d+',scriptrun)
				#print(scriptpre[0])
				scriptpre1 = str(scriptpre[0])	
#					ssh()
#					ipaddress = input("Enter your ")
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
				import paramiko
				#j = 0 
				print("Controller ip address of the target ("+scriptpre1+") : ")
				ip = scriptpre1
				print(ip)
				user = input("Enter the username of the target  :  ")
				passwd = getpass.getpass("Enter target's password : ")
				#controllerip = input("Enter the Ip address of controller ( 192.168.0.35 ) : ")
		#		temp1 = "cp hosts /var/www/html/hosts"
		#		temp2 = "cp nightfallconfig.ini /var/www/html/nightfallconfig.ini"
		#		os.system(temp1)
		#		os.system(temp2)
				#temp3 = "apt install wget -y | cat > check && cat check"
#				atemp = "wget "+ipaddress+"/hosts | cat > check1 && cat check1"
#				btemp = "wget "+ipaddress+"/nightfallconfig.ini | cat > check2 && cat check2"
				ctemp = "wget "+ipaddress+"/"+scriptrun+" | cat > check3 && cat check3"
#				dtemp = "sudo su - nightfall && python3 "+scriptrun+" | cat > check4 && cat check4"
#				command = ["cp hosts /var/www/html/hosts","sudo su","cp nightfallconfig.ini /var/www/html/nightfallconfig.ini","apt install wget -y",atemp,btemp,ctemp,dtemp]
				def sshCommand(hostname, port, username, password, command):
					sshClient = paramiko.SSHClient()
					sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					sshClient.load_system_host_keys()
					sshClient.connect(hostname, port, username, password)
					stdin, stdout, stderr = sshClient.exec_command(command , get_pty=True)
					for line in iter(lambda: stdout.readline(2048), ""):
							print(line)
#				ip = input("Enter the ip address of the target : ")
#				user = input("Enter the username of the target : ")
#				passwd = getpass.getpass("Enter target's password : ")
				#while j < len(command):
				#	ssh()
#				sshCommand(ip, 22, user, passwd, temp1)
#				sshCommand(ip, 22, user, passwd, temp2)
		#		sshCommand(ip, 22, user, passwd, temp3)
	#			sshCommand(ip, 22, user, passwd, atemp)
	#			status()
	#			sshCommand(ip, 22, user, passwd, btemp)
	#			status()
				sshCommand(ip, 22, user, passwd, ctemp)
				status()
#=====> Add Lines Heres reminder for creater
				print("Enter the password for confirmation of target for security reasons : ")
				text2 = "ssh -t "+user+"@"+ip+" \"sudo python3 /home/ubuntu/"+scriptrun+"\""
				os.system(text2)
#				sshCommand(ip, 22, user, passwd, dtemp)	
				status()	
				#	j += 1
				os.system("rm check")
				os.system("rm temp1")
				menu()
			else:
				syncloop()
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
	if askmenu == "":
		menu()
		ask()
#	if (str(askmenu)).lower() == "quit":
#		print("Quitting")
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
	if int(askmenu) == int("5"):
		print("Quitting")
menu()
ask()



