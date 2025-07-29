#!/bin/bash

# Define string variables
GREETING="Hello, World!"
USERNAME="Alice"
MESSAGE="Welcome to Bash scripting!"

# Define a numeric variable (Bash treats numbers as strings by default,
# but can perform arithmetic operations on them)
COUNT=10

# Define a variable from a command's output (command substitution)
CURRENT_DATE=$(date +"%Y-%m-%d") # Use $(command) for command substitution
CURRENT_TIME=`date +"%H:%M:%S"`  # Backticks also work, but $() is preferred for nesting

# Accessing Variables:**
# Use a `$` prefix to access the value of a variable.
echo $GREETING
echo "User: $USERNAME"
echo "$MESSAGE"
echo "Count: $COUNT"
echo "Today's date: $CURRENT_DATE"
echo "Current time: $CURRENT_TIME"

# Variables inside double quotes are expanded (interpolated)
echo "The user is $USERNAME."
# Variables inside single quotes are not expanded (literal)
echo 'The user is $USERNAME.'