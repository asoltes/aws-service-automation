#!/bin/bash

# Check if all arguments are provided
if [ $# -ne 3 ]; then
  echo "Usage: $0 <names> <begintime> <endtime>"
  exit 1
fi

# Split the names argument into an array
names=($(echo $1 | tr ',' ' '))

# Loop over the names and call the scheduler-cli command for each one
for name in "${names[@]}"; do
  echo "Updating schedule for period ltf-prod-$name-awsis"
  scheduler-cli update-period \
    --stack LTF-PROD-Instance-Scheduler \
    --name "ltf-prod-$name-awsis" \
    --description "LTF Prod ${name^^} Environment Schedule" \
    --weekdays mon-fri \
    --begintime $2 \
    --endtime $3
done

echo "Done updating schedule for all instances"