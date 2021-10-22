#!/usr/bin/env python3
import parakiko
import pyexcel
import yaml

# server file has hostname and IP

def main():
    with open("servers.yml", "r") as myf:
        credz = yaml.load(myf)

   #  print(credz)
   mykey= paramiko.RSAkey.from_private_key_file("/home/student/.ssh/id_rsa.pub") 

   mylistdict={}

   for cred in creda:
       # build a paramiko SSH connection
       sshsession= paramiko.SSHClient()
      
       # auto accept an missing host keys
       sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

       # debut
       print("Connecting to ..." + cred.get("un") + "@" + cred.get("ip"))

       # teach sshsession how to connect
       sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

       # executea a command ... return a tuple
       # (x, y, z)
       stdin, stdout, stderr= sshsession.exec_command("python3 --version")
 
       ver= stdout.read().decode("utf-8").rstrip("\n")
      
       d= {"Servername":       cred.get("un"), 
           "Software-version": ver}

       mylistdict.append(d)

    print(mylistdict)
     
    pyexcel.save_as(records=mylistdict,
                    dest_file="filename.out")

main()

