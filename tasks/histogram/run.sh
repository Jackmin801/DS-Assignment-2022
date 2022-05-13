#!/bin/bash
VERBOSE=$1
TIMELIMIT=5s
mkfifo iopipe0 iopipe1

if [[ $VERBOSE ]]
then
    timeout $TIMELIMIT <iopipe0 java -classpath solutions Histogram | tee iopipe1 & <iopipe1 python3 tasks/histogram/run.py | tee iopipe0;
else
    timeout $TIMELIMIT <iopipe0 java -classpath solutions Histogram | python3 tasks/histogram/run.py > iopipe0;
fi
PASS=$?

rm iopipe0 iopipe1
exit $PASS
