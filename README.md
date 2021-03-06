# vibhelm Documentation

## License information

[site]: http://www.adamrohacs.com "adamrohacs.com website"
[license]: http://www.gnu.org/licenses/gpl.html "gnu.org license"
[repo]: https://github.com/arohacs/vibhelm "vibhelm repository"
[contact id]: http://www.adamrohacs.com/contact "Contact Adam Rohacs"
**Vi**rtual **B**ox **Helm** (vibhelm) by [Adam Rohacs][site] is licensed under a [GNU General Public License][license] and is based on a work at [github.com][repo].  

### Anatomy of the project name
I wanted to make a unique name for this software which included something related to commanding a ship. I immediately thought of **helm**, which is the  
[driving mechanism of a ship][helm def]:
 
1. Nautical The steering gear of a ship, especially the tiller or wheel.
2. A position of leadership or control: at the helm of the government.  

Further, I wanted to attach an abbreviation of [VirtualBox][vbox def] to "helm", but was concerned that using "VB" would confuse folks who are used to dot net terminology, and so I lengthened the typical abbreviation to "vib", which formed a nonsense, and hopefully *catchy* word to name the project.
### Version information
This is a python 2.7.x script and may not work correctly or at all when invoked by python 3. Please check your version by typing: python -V  

#### OS Platform support and Testing
This program has been tested with Python 2.7 under virtualenvs and with python2 on Arch Linux.  Most windows folks seem to use VMWare with Hypervisor anyway, so this may not apply. If you are using a non Unix/Linux platform, I'm guessing that raw strings might be the only change needed, if anything is needed. 

If you test this program on any platform (Unix, Linux, FreeBSD, Mac OSX, Windows xx, etc.) and find issues, please [contact][contact id] me and I'll update the README and possibly make another version for your platform. Also, you could fork this repo and let me know the name of your repository and I will link to it. 

[helm def]: http://www.thefreedictionary.com/helm
[vbox def]: https://www.virtualbox.org/


[git clone url]: http://git-scm.com/book/en/Git-Basics-Getting-a-Git-Repository

### Usage
[Clone][git clone url] the repository to a directory of your choice: 
$ git clone git://github.com/arohacs/vibhelm.git

Run the program with python version 2.7, for example:   
$ python vibhelm.py  
For Arch Linux and other distributions that separate python by version:
$ python2 vibhelm.py 

Follow the menus - you should be fine. Remember that "Shutdown" aborts the virtual machine. 

### Features

With this software, you can:  

* **List** all VirtualBox machines that are installed and accessible  
* **Display** a list of running machines  
* **Start** machines in headless mode  
* **Shutdown** machines in *saved state* (like hibernate)  
* **Power off** machines (abort - only for emergencies)
  
### UI
There is a very rudimentary UI menu system available. I intend to leverage some sort of curses console UI in the future.  

[core python site]: http://corepython.com/
[Wesley Chun site]: http://cpp.wesc.webfactional.com/events.html
The current menu style is borrowed from examples in:  
[Core Python Programming][core python site] by [Wesley Chun][Wesley Chun site].  


### History
I started writing this program a few months back when I wasn't satisfied with typing VBoxManage and VBoxHeadless commands over and over to start and stop (save state of) machines.  
I considered using Vagrant, which is a Ruby Gem, to accomplish this task, but it seemed like I would have to learn a lot in order to do what I could accomplish more quickly by writing a Python program.  

Since I use SSH to connect to each headless box via terminal window and don't use VRDE and web interfaces (and could use VNC with encryption if I really wanted to do that), I decided not to work on that feature so that I could finish the non-UI version of this project.  

If you are ambitious, and would like to add VRDE port support - please fork the project and do so (and make a repo on github to share with the community - and let me know so that I can follow your project and learn how you did it). I might add support later if enough people seem interested in that feature. I personally think that running headless with SSH is all anyone should need for most practical applications.   


### TODO

Properly squelch nohup output.  
Create UI with a Python curses library.   
Create install package.  
Create GUI (desktop and touch devices).  
Add networking with Twisted library (to control VMs on other machines with desktop or touch device).  
Create command line version with completion.
