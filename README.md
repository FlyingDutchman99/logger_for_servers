     Answers to Discussion questions
    ---------------------------------
1. My approach has mostly been to extract out "only the nessassary data" from the log files and complete the specified task using least possible resources and with easy-to use arguments so that anybody can perform tasks easily. Concept was to iterate through the log file and to process and store only task-specific data in the RAM. Also using in-built commands such grep.
2. The runtime performance :
    Worst case compleixity : O(n), for 'n' being lines in input log file.
    Runtime performance on "out.log" for calculating percentile was 0.322s calculated using :  $time python3  analyze.py percentile 100
3. If I had more time, I would
  a) Try to make the code more maintainable so that contributors can develop and make it more useful.
  b) Try to add more features to enhance usage in multiple scenarios.
  c) Optimize the code because obviously, "Performance is everything."
  d) given enough time I could try making it run using multiple cores.


# logger_for_servers
# Contain all the nessassary files for successfull running.
# Must have python3 installed.
# Must install matplotlib, numpy first.
# Never hesitate to use help as an argument.

Usage as follows:
 1. analyze.py                                              // This is solution to first question.
	python3 analyze.py histogram                              // Part-I
	python3 analyze.py percentile 65                          // Part-II
	python3 analyze.py help                                   // miscellaneous

 2. monitorlog.py
	python3 monitorlog.py logfile ./out.log                   // This is solution to second question. It logs for both problem a and b.
	python3 monitorlog.py help                                // miscellaneous

 3. rulemaker.py                                            // To implement the idea that user can edit the json file easily.
# Used to edit rules via editing json file.
	python3 rulemaker.py create-rules
	python3 rulemaker.py help
