## Comparision of Various TCP Congestion Algorithms

#### Instalation Process
1. Clone The Project
2. Install required Modules _thread, time, select, socket
    all these are included when python is installed.
3. Add a file "in.txt" which is the test file that is sent to other receiver.
4. run server.py as node and two instances of client.py (works as two clients).
5. Change the ip according to your local config.
6. You can observe the transferred file as "out.txt". Any file format would work but here text file are considered.
7. After running client.py an input is prompted where you can type "q" or "Q" to quit or any other set of characters to transfer the "in.txt" file.