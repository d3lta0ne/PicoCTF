# Answer
    **picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_c42168d9}**

# Solution

    After starting the instance we are provided with ssh credentials for the ctf-player user. There are a series of missing bash commands we can not use in the bash terminal we are connected to.

    We find by using just *TAB*+*TAB*, that we have the following commands at our disposal.
    ```
    !          :          [[         alias      bg         break      caller     cd         compgen    compopt    coproc     dirs       do         echo       else       esac       exec       export     fc         fi         function   hash       history    in         kill       local      mapfile    printf     pwd        readarray  return     set        shopt      suspend    then       times      true       typeset    umask      unset      wait       {
    ./         [          ]]         bash       bind       builtin    case       command    complete   continue   declare    disown     done       elif       enable     eval       exit       false      fg         for        getopts    help       if         jobs       let        logout     popd       pushd      read       readonly   select     shift      source     test       time       trap       type       ulimit     unalias    until      while      }
    ```

    We can leverage the ability to autocomplete with TAB and the `cd` command to enumerate the directories and files on the system. Yet, without an easy way to read the files (i.e. cat, strings, etc) we will use the builtin functions for this. The following command will read the contents of a file by using only the echo command. `echo $(<[file_to_read])`. We can use the TAB auto-complete functionality with our `echo` command to manually display the contents of all the directories as there are only a few to check.  The flag is then found in the by running the following command `echo $(<ala/kazam.txt) `.