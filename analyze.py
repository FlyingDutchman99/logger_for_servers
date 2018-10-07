import sys
import numpy as np
import subprocess as sp
from matplotlib.pyplot import *


def help():
    s = """This command is used to analyze log files. You can view both histogram and percentile stats of response time.

    Please enter in the specified format :

      analyze.py histogram
        -> Use this to edit the json file to modify logging rules.

     analyze.py percentile INTEGER_VALUE_[0-100]
        -> Use this to view percentile statsself.
        
     analyze.py help
        -> Use it to view the above help.
    """
    print(s)
    sys.exit()


if sys.argv[1] == "help":
    help()


elif sys.argv[1] == "histogram":
    total_log_lines = sp.getoutput( "grep -c '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]' ./out.log")

    count_total_errors = sp.getoutput("grep -c 'ERROR' ./out.log")

    count_runtime=0
    count_variable=0
    count_unknown=0
    count_random=0
    count_value=0
    types_of_errors = ( "RunTimeError", "VariableError", "UnknownError", "RandomError", "ValueError" )

    with open("./out.log", 'r') as file:
        for line in file:
            if types_of_errors[0] in line:
                    count_runtime+=1
            elif types_of_errors[1] in line:
                    count_variable+=1
            elif types_of_errors[2] in line:
                    count_unknown+=1
            elif types_of_errors[3] in line:
                    count_random+=1
            elif types_of_errors[4] in line:
                    count_value+=1

    count=0
    #this code gives the same answer  my successor does.
    with open("./out.log", 'r') as file:
         for line in file:
                 if 'Exception' in line:
                         count=count+1
    x = ["RunTimeError", "VariableError", "UnknownError", "RandomError", "ValueError"]
    y = [count_runtime,count_variable,count_unknown,count_random,count_value]
    bar(x,y)
    show()

elif sys.argv[1] == "percentile":

    x = int(sys.argv[2])

    list_of_responses = []
    with open("./out.log", 'r') as file:
         for line in file:
             if "ms]" in line:
                  list_of_responses.append( int(line.split(" ")[4][1:-3])  )

    #print( list_of_responses)
    arr = np.array( list_of_responses )
    print("Response time is "+str(np.percentile( arr,x))+"ms" )

else:
    help()
