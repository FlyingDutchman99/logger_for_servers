import sys




def help():
    s = """This command is used to edit json rules. You can edit one rule at a time and view logs for the same.

    Please enter in the specified format :
    \t  python3 rulemaker.py create-rules
    \t \t   -> Use this to edit the json file to modify logging rules.
    \t python3 rulemaker.py help
    \t \t   -> Use this to print this help.
    """
    print(s)


if sys.argv[1] == "help":
    help()
    sys.exit()


if sys.argv[1] == "explain":
    explain()
    sys.exit()


if sys.argv[1] == "create-rules":

    x = input(" Enter 1 to edit Response Time \n Enter 2 to edit Number of Errors \n")

    if '1' == x:
        rule = "ResponseTime"
        value = input("Enter value in milliseconds : ")
        time_window = input("Enter duration : ")
        sign = input("Enter < or > or = : ")

    elif '2' == x:
        rule = "No_of_errors"
        value = input("Enter threshold value of errors : ")
        time_window = input("Enter duration in seconds : ")
        sign = input("Enter < or > or = : ")

    else:
        help()
        system.exit()

    s = "{ \""+rule+"\" : [ \""+ sign+"_"+value+"\", \""+time_window+"\" ] }"
    with open("./rule.json",'w') as fout:
        fout.write(s)
    print("\nNew json is created and it looks like "+s)
    print(" now you can run \n$python3 monitorlog.py logfile /your/path/to/logfile ")
