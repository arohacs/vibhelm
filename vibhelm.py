
# Copyright 2011-2012 Adam Rohacs
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


#!/usr/bin/env python
import subprocess
from subprocess import PIPE, Popen, STDOUT, call
import sys

def listVMs(pref):
    
    if pref == 0:
        state = 'vms'
    elif pref == 1:
        state = 'runningvms'
        
    wordlist=[]
    output = subprocess.Popen(['VBoxManage','--nologo','list', state],\
            stdout=subprocess.PIPE).communicate()[0] 
        # will show running vms or list of all vms
        
    output = output.rstrip()
    for index in output.split('\n'):
        for word in index.split(' '):
            wordlist.append(word.strip('"{}'))
    
    VMlist = [(wordlist[t], wordlist[t+1]) for t in range(0, len(wordlist) - 1, 2)]
    VMlist = dict(VMlist)

    return VMlist

def runVMs(): 
    '''
    Using no vrde because I ssh to headless machines and don't need it. Feel free to fork and add
    the feature of keeping track of ports, etc., for each machine. 
    '''
   
    print "The following virtual machines are available and not already running:"
    AvailVMs = {}
    for num, index in enumerate(listVMs(0)):

        p1 = Popen(["VBoxManage", "showvminfo", index], stdout=PIPE)
        p2 = p2 = Popen(["grep","-i", "^state"], stdin=p1.stdout, stdout = PIPE)
        p1.stdout.close()
        result = p2.communicate()[0]

        if 'running' not in result:
            AvailVMs[num] = index
        # elif 'running' in result:
        #     # print "DEBUG: ", index, "is running..."
    print AvailVMs
    
    choicelist = AvailVMs
    if choicelist:
        print "The following vms are available to be started:"
        for key in choicelist:
            print key, choicelist[key]
        choice = ''
        while not choice:
            choice = raw_input("Please enter the number of the VM you'd like to run: ")
            n = None #check for non-integer entries
            while n is None:
                try:
                    n = int(choice)
                except ValueError:
                    print "Please enter an integer!"
                    choice = raw_input()
            
        print "starting {0} ...".format(choicelist[int(choice)])

        p1 = Popen(['nohup', 'VBoxHeadless', '-s', choicelist[int(choice)], '-v', 'off']) 

    else: print "no virtual machines are available to be started."

    call('clear') #otherwise nohup message shows up at menu prompt and munges the display. 

    return

def shutdownVMs(pref):
    
    cmd = 'VBoxManage'
    if pref == 0:
        state = 'savestate'
    elif pref == 1:
        state = 'poweroff'
    
    choicelist = listVMs(1)
    vmChoices = []
    if choicelist:
        for key in choicelist:
                vmChoices.append(key)
    if vmChoices:
        print "The following vms are running:"
        for index,name in enumerate(vmChoices):
            print index,name
        choice = ''
        while not choice:
            choice = raw_input("Please enter a list number from those listed: ")
            n = None #check for non-integer entries
            while n is None:
                try:
                    n = int(choice)
                except ValueError:
                    print "Please enter an integer!"
                    choice = raw_input()
        
        print "shutting down {0}".format(vmChoices[int(choice)])
        call(['vboxmanage','controlvm', vmChoices[int(choice)], 'savestate']) 
    else: print "no virtual machines are running that would be shut down."
    call('clear')
    return

def showVMs(pref):
    if pref == 0:
        desc = "available:"
    elif pref == 1:
        desc = "running:"
    
    if not listVMs(pref):
        print "No virtual machines are {0}.".format(desc)
    else:
        print "the following vms are {0}".format(desc)
        for num, index in enumerate(listVMs(pref)):
            print num,index
        return
    
def showMenu(): #main menu
    
    prompt = """
    (L)ist all virtual machines
    (D)isplay running virtual machines
    (R)un virtual machines
    (S)hutdown virtual machines 
    (P)oweroff virtual machines
    (E)xit
    
    Enter choice: """

    done = False
    while not done:

        chosen = False
        while not chosen: #continue until choice made
            try:
                choice = raw_input(prompt).\
                strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'e'
            except IndexError:
                choice = 'e'
            except UnboundLocalError:
                choice = 'e'
            print '\nYou picked: [%s]' % choice
            if choice not in 'ldrspe':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'l': showVMs(0)
        if choice == 'd': showVMs(1)
        if choice == 'r': runVMs()
        if choice == 's': shutdownVMs(0)
        if choice == 'p': shutdownVMS(1)
        if choice == 'e': done = True

if __name__ == '__main__':
   showMenu()
