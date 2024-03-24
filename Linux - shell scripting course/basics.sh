#!/bin/bash
# COMMENTS ARE PRECEDED BY # IN BASH, EXCEPT FOR THE SHEBANG IN THE FIRST LINE, WHICH IS EXECUTED
# THE EXTENSION '.sh' ARE A CONVENTION IN SHELL SCRIPTING, BUT NOT NECESSARY
# COMMENTS THAT START WITH A '#!' ARE CALLED SHEBANG COMMENTS/LINES, SINCE '#' IS CALLED 'POUND' OR 'SHARP', SINCE IT LOOKS LIKE THE 'SHARP' USED IN MUSIC NOTATION, AND THE '!' IS CALLED 'BANG'
# EACH BASH FILE SHOULD START WITH A SHEBANG AND A PATH TO THE INTERPRETER, THIS DETERMINES WHAT PROGRAM WILL EXECUTE THE SCRIPT
# MAKE SURE THAT THE FILE HAS THE RIGHT PERMISSIONS BEFORE IT IS EXECUTED
# TO EXECUTE A SCRIPT IN THE SHELL, USE './[NAME SCRIPT]' OR '[FULL PATH TO SCRIPT]'

# TO GET HELP IN THE SHELL (ON A FUNCTION), USE 'help' OR 'help [COMMAND]' FOR BUILT-IN SHELL FUNCTIONS AND 'man [COMMAND]' FOR STANDARD AND NONSTANDARD FUNCTIONS
# TYPES DON'T NEED TO BE SPECIFIED IN SHELL SCRIPTING WHEN DECLARING VARIABLES
# NO SPACINGS ARE USED AROUND THE '=' IN VARIABLE DECLARATION!
# STRINGS CAN BE MADE WITH EITHER DOUBLE OR SINGLE QUOTATION MARKS

DURK='HELLO SHELL'
echo $DURK
echo ${DURK}YYYYY $DURK$DURK
echo 'HELLO SHELL'
# help echo
# man echo

# PSEUDOCODE IS STEPS WRITTEN IN ENGLISH OR ANOTHER HUMAN LANGUAGE TO DESCRIBE THE NECESSARY STEPS
# GOAL IS TO PRINT USER ID, USER NAME AND TO CHECK WHETHER USER IS ROOT USER

# SEVERAL OF THE FOLLOWING COMMANDS ARE IDENTICAL (SINCE 'echo [VARIABLE]' AND 'id' YIELDS THE SAME ANSWER)
id
echo $UID
id -u
echo $USER
id -un
# TO STORE THE OUTPUT OF A COMMAND IN A VARIABLE, USE 'variable=$([COMMAND])'
DURK=$(id -Gn)
echo $DURK
# THE SYNTAX FOR THE IF-STATEMENT IS 'if [[ COMMAND ]]; then COMMAND; elif COMMAND; then COMMAND; else COMMAND; fi
# CONDITIONAL EXPRESSIONS ARE BETWEEN DOUBLE BRACKETS, '[[]]', AND '||' FOR 'OR' AND '&&' FOR 'AND' AND '!' FOR 'NOT' AND '==' AND '=~' FOR 'IS' AND '!=' FOR 'NOT IS' CAN BE USED
# ANOTHER OPERATOR THAT CAN BE USED BETWEEN THE DOUBLE BRACKETS IS 'test', WHICH CAN BE LOOKED UP WITH 'man test'
# THE COMMAND SEPARATOR IS EITHER ';' OR 'ENTER'
if [[ "$USER" == 'root' ]]
then echo 'USER IS ROOT'
else echo 'USER IS NOT ROOT'
fi
# WHICH IS EQUAL TO
if [[ "$UID" -eq 0 ]]; then echo 'USER IS ROOT'; else echo 'USER IS NOT ROOT'; fi

# TO COMPARE STRINGS (==, !=, =~) OR INTEGERS (-ne, -eq, gt, lt) A SLIGHTLY DIFFERENT SYNTAX OUGHT TO BE USED, SEE 'test'
# if [[ "$UID" -ne 1000 ]]; then echo MURK; exit 1; fi 

# TO EXIT WITH A CERTAIN STATUS, USE COMMAND 'exit [NUMBER TO EXIT WITH, SUCCESS IS 0, THE REST IS NONZERO]'
# EXIT STATUS OF LAST COMMAND CAN BE ENTERED USING $? OR ${?}
echo "EXIT STATUS: $?"
# TO ADD USERS, USE 'useradd', CONVENTIONS FOR USERNAMES ARE WITHOUT SPECIAL CHARACTERS AND ALL LOWERCASE
# FOR USER INPUT, USE 'read' WITH OPTION PROMPT '-p'
# THERE IS STANDARD INPUT, STANDARD OUTPUT AND STANDARD ERROR
# TO CHANGE THE PASSWORD, USE 'passwd', PREFERABLY WITH FLAG '--stdin' TO READ INPUT AND WITH FLAG '-e' TO FORCE USER TO CHANGE PASSWORD DURING FIRST LOGIN
# ANOTHER WAY TO CHANGE PASSWORD IS WITH 'usermod -p [PASSWORD] [USERNAME]'
read -p 'PROVIDE USERNAME: ' USERNAME
echo $USERNAME
read -p 'PROVIDE PASSWORD: ' PASSWORD
useradd -m "${USERNAME}"
less /etc/passwd | grep "${USERNAME}"
# passwd "${USERNAME}" 
echo | echo | (echo "${PASSWORD}" && cat) | (echo "${PASSWORD}" && cat) | passwd $USERNAME 
passwd -e "${USERNAME}" 
userdel -r "${USERNAME}"
less /etc/passwd | grep "${USERNAME}"

exit 0
