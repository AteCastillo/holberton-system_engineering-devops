# SSH
Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 16.04 LTS environment. You do not need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do not attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.
## Learning Objectives

    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash
##  Tasks
0. Use a private key 
```
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
Requirements:
    Only use ssh single-character flags
    You cannot use -l
    You do not need to handle the case of a private key protected by a passphrase
```

1. Create an SSH key pair
mandatory
```
Write a Bash script that creates an RSA key pair.
Requirements:
    Name of the created private key must be holberton
    Number of bits in the created key to be created 4096
    The created key must be protected by the passphrase betty
```
2. Client configuration file
```
Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
Requirements:
    Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
    Your SSH client configuration must be configured to refuse to authenticate using a password
```
3. Let me in!
```
Now that you have successfully connected to your server, we would also like to join the party.
Add the SSH public key below to your server so that we can connect using the ubuntu user.
```
4. Client configuration file (w/ Puppet) 
```
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
Requirements:
    Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
    Your SSH client configuration must be configured to refuse to authenticate using a password
```

