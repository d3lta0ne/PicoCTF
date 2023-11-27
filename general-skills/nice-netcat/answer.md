# Answer

**picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}**

## Command

After running the following `nc mercury.picoctf.net 7449`, we get a series of decimal values followed by a new line. Based off the hint and problem description we assume that the output is ASCII. We create *script.py* that ingest the output of the netcat session and then parses the values into ASCII. This code is executed by running `python3 script.py`.