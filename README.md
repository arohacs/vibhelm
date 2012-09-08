# vibhelm Documentation

## License information

[site]: http://www.adamrohacs.com "adamrohacs.com website"
[license]: http://www.gnu.org/licenses/gpl.html "gnu.org license"
[repo]: https://github.com/arohacs/vibhelm "vibhelm repository"

**Vi**rtual **B**ox **Helm** (vibhelm) by [Adam Rohacs][site] is licensed under a [GNU General Public License][license] and is based on a work at [github.com][repo].  
 
### Version information
This is a python 2.7.x script and may not work correctly or at all when invoked by python 3. Please check your version by typing: python -V  


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
The current menu style is borrowed from examples in [Core Python Programming][core python site] by [Wesley Chun][Wesley Chun site].  



### History
I started writing this program a few months back when I wasn't satisfied with typing VBoxManage and VBoxHeadless commands over and over to start and stop machines.  
I considered using Vagrant, which is a Ruby Gem, to accomplish this task, but it seemed like I would have to learn a lot in order to do what I could accomplish more quickly in writing a Python program.  

Since I use SSH to connect to each headless box via terminal window and don't use VRDE and web interfaces (and could use VNC with encryption if I really wanted to do that), I decided not to work on that feature so that I could finish the non-UI version of this project.  

If you are ambitious, and would like to add VRBE port support - please fork the project and do so (and make a repo on github to share with the community). It shouldn't take more than an hour or so with debugging. I might add support later if enough people seem interested.  


### TODO

Properly squelch nohup output.  
Create UI with a Python curses library.   
Create install package.  
Create GUI (desktop and touch devices).  
Add networking with Twisted library (to control VMs on other machines with desktop or touch device).  
Create command line version with completion.
