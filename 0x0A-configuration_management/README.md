# Configuration management
When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the s hostname or any other metadata we had (server type, server 
There were 2 pieces of bad news:

    When MCollective receives nil as an argument for its filter method, it takes this to all 
    The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and 
Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)videosSlideShareserversmean environmentserver
## General requirements

    All your files will be interpreted on Ubuntu 14.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp

Install puppet-lint
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
Instal puppet
```
$ apt-get install puppet
```
## Tasks
0. Create a file
```
Using Puppet, create a file in /tmp.
Requirements:
    File path is /tmp/holberton
    File permission is 0744
    File owner is www-data
    File group is www-data
    File contains I love Puppet
```
1. Install a package 
```
Using Puppet, install puppet-lint.
Requirements:
    Install puppet-lint
    Version must be 2.1.1
```
2. Execute a command 
```
Using Puppet, create a manifest that kills a process named killmenow.
Requirements:
    Must use the exec Puppet resource
    Must use pkill
```
