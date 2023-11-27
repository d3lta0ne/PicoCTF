# Answer

**picoCTF{d15a5m_t34s3r_f5aeda17}**

# Solution

After downloading the binary and the bash script they provide we start by making the bash script executable. We do this using `chmod u+x static`. Based of the information presented when attempting to just run the bash script by itself we see that the correct way is to use `./ltdis.sh static`. This generates two files, static.ltdis.strings.txt and static.ltdis.x86_64.txt. We use `grep` to simplify searching these files for the flag using the following command: `grep pico static.ltdis.strings.txt`.