# Answer

**picoCTF{b1scu1ts_4nd_gr4vy_616f7182}**

# Solution

After downloading the binary we are presented with a program named `warm`. We first change privledges on the file to ensure that we execute it using `chmod u+x warm`, then run the file by typing `./warm`. When we run the binary with the help flag it provides us with the flag. `./warm -h`