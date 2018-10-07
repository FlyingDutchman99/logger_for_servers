import sys
import json
import datetime



def help():
    s = """Please enter in the specified format :
    \t  monitorlog.py logfile /path_to/logfile
    """
    print(s)


if not sys.argv[1] == "logfile":
    help()
    sys.exit()



# attributes from json to be edited by user in json.
RESPONSE_TIME = "ResponseTime"
NO_OF_ERRORS = "No_of_errors"

# to read the json file
with open("rule.json",'r') as out:
    data = out.read()
    json_file_data = json.loads(data)


filename =  sys.argv[2]
try:
    for rule in json_file_data.keys():
        print( "xxxxxxxxxxx")
        print(rule)
        print( "xxxxxxxxxxx")
            #rule = NO_OF_ERRORS
        value = int( json_file_data[rule][0].split("_")[1] )
        duration = int( json_file_data[rule][1] )

        comparer = 0
        if json_file_data[rule][0].split("_")[0] == ">":
            comparer =1
        elif json_file_data[rule][0].split("_")[0] == "<":
            comparer = 2

        ticounter=0
        error_counter=0

# used to extract important data from individual lines.
        with open(filename,'r') as input_file:
            for line in input_file:
                if "[PID" in line:
                    data=line.split("[")
                    date,time = data[0].split()
                    pid = ( data[1].split()[1].replace("]","") )
                    response_time = int( data[2].replace("ms]","") )
                    uid = ( data[3].split()[1].replace("]","") )
                    log_level = data[4].split("]")[0]
                    url = ( data[4].split()[1]  )
                    msg = ( "".join( data[4].split()[2:] )  )
                    # print( msg)

                    tc = datetime.datetime( int(date.split("-")[0]), int(date.split("-")[1]),int(date.split("-")[2]), int(time.split(":")[0]), int(time.split(":")[1]), int(time.split(":")[2].split(".")[0]  ) )

                    if ticounter == 0:
                        ti = tc
                        ticounter+=1

                    if rule == RESPONSE_TIME:
                        if comparer == 1:
                            if value > response_time:
                                ti=tc
                            else:
                                if tc-ti >= datetime.timedelta( seconds=duration ):
                                    print (line)
                                    ti=tc

                        elif comparer == 2:
                            if value < response_time:
                                ti=tc
                            else:
                                if tc-ti >= datetime.timedelta( seconds=duration ):
                                    print (line)
                                    ti=tc

                        elif comparer == 0:
                            if response_time == value:
                                ti=tc
                            else:
                                if tc-ti >= datetime.timedelta( seconds=duration ):
                                    print (line)
                                    ti=tc

                    elif rule == NO_OF_ERRORS:
                        if log_level == "ERROR":
                            error_counter += 1

                        if comparer == 1:
                            if tc-ti >= datetime.timedelta( seconds=duration ):
                                if error_counter > value:
                                    print(line)
                                else:
                                    ti=tc
                                    error_counter=0

                        elif comparer == 2:
                            if tc-ti >= datetime.timedelta( seconds=duration ):
                                if error_counter < value:
                                    print(line)
                                else:
                                    ti=tc
                                    error_counter=0

                        elif comparer == 0:
                            if tc-ti >= datetime.timedelta( seconds=duration ):
                                if error_counter == value:
                                    print(line)
                                else:
                                    ti=tc
                                    error_counter=0


except Exception as e:
        print(e)
