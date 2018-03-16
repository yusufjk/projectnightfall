#!/usr/bin/python 

import os

print("                                                                                                    ")
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
print("                                                                                                    ")
print("                                                                                                    ")
print("                                                                                                    ")
os.system("service nova-api restart")
os.system("service nova-consoleauth restart")
os.system("service nova-scheduler restart")
os.system("service nova-conductor restart")
os.system("service nova-novncproxy restart")

global controllerip
#iwillbereplaced


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
        permission5 = "http://" + controllerip + ":5000/v3"
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

creds()

os.system("su -s /bin/sh -c \"nova-manage cell_v2 discover_hosts --verbose\" nova")

os.system("openstack compute service list")


