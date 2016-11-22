ASCII art movie Telnet player
=============================

Can stream an ~20 minutes ASCII movie via Telnet emulation
as stand alone server or via xinetd daemon. 

<img src="screenshots/example.gif?raw=true" width=500>

Wanna see it in action? Just watch http://asciinema.org/a/3132


Tested with Python 2.6+, Python 3.5+

Original art work : Simon Jansen [http://www.asciimation.co.nz/](http://www.asciimation.co.nz/)  
Telnetification & Player coding : Martin W. Kirst  
Python3 Update: Ryan Jarvis  

Command line parameters
-----------------------

See program output:

    $ python ascii_telnet_server.py --help
    Usage: ascii_telnet_server.py [options]
    Options:
      -h, --help            show this help message and exit
      --standalone          Run as stand alone multi threaded TCP server (default)
      --stdout              Run with STDIN and STDOUT, for example in XINETD
                            instead of stand alone TCP server. Use with python
                            option '-u' for unbuffered STDIN STDOUT communication
      -f FILE, --file=FILE  Text file containing the ASCII movie
      -i INTERFACE, --interface=INTERFACE
                            Bind to this interface (default '0.0.0.0', all
                            interfaces)
      -p PORT, --port=PORT  Bind to this port (default 23, Telnet)
      -v, --verbose         Verbose (default for TCP server)
      -q, --quiet           Quiet! (default for STDIN STDOUT server)


Run as stand alone server
-------------------------

Simple call this Python script by using the sample movie file:

    $> python ascii_telnet_server.py --standalone -f ../sample_movies/sw1.txt
    Running TCP server on 0.0.0.0:23
    Playing movie sw1.txt
   

Run as xinetd program
---------------------

place this configuration into `/etc/xinetd.d/telnet`:

    # default: on
    # description: An telnet service playing an ASCII movie, Star Wars Episode 4 
    service telnet
    {
            disable         = no
            socket_type     = stream
            protocol        = tcp
            port            = 23
            user            = root
            wait            = no
            instances       = 10
    
            log_type        = FILE /var/log/asciiplayer
            log_on_success  += PID HOST DURATION
            log_on_failure  = HOST
            server          = /usr/bin/python
            server_args     = -u -OO /opt/asciiplayer/ascii_telnet_server.py -f /opt/asciiplayer/sw1.txt --stdout
    }

