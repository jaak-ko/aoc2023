#!/bin/bash

function make_dir() 
{
    mkdir -p "${DIR_NAME}"
    touch $PY_FILE
    cp template.py $PY_FILE
}

if [ $# -eq 0 ]; then
    echo "  Usage: ./get_input.sh <day> <year(default=2023)>"
    exit 1
elif (( $1 < 1 || $1 > 24)); then
    echo "Day must be between 1 and 24"
    exit 1
fi

DAY=$1
YEAR=${2:-2023}

# Session token is stored in .env file
SESSION_TOKEN=$(grep SESSION .env | sed s/SESSION=//g)

DIR_NAME="day_${DAY}"
FILE_NAME="${DIR_NAME}/input.txt"
PY_FILE="${DIR_NAME}/day_${DAY}.py"

make_dir

curl -k --ssl-no-revoke --cookie "session=${SESSION_TOKEN}" https://adventofcode.com/${YEAR}/day/${DAY}/input -o ${FILE_NAME}