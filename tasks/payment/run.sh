#!/bin/bash
VERBOSE=$1
TIMELIMIT=3s
SOLUTION_FILE=Payment
RUNNER_FILE=tasks/payment/run.py
mkfifo iopipe0 iopipe1

if [[ $VERBOSE ]]
then
    timeout $TIMELIMIT <iopipe0 java -classpath solutions $SOLUTION_FILE | tee iopipe1 & <iopipe1 python3 $RUNNER_FILE | tee iopipe0;
else
    timeout $TIMELIMIT <iopipe0 java -classpath solutions $SOLUTION_FILE | python3 $RUNNER_FILE > iopipe0;
fi
PASS=$?

rm iopipe0 iopipe1
exit $PASS
