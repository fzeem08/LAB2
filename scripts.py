# Lab2/script.py
import sys

def print_arguments():
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    
    print("Script:", script_name)
    print("Arguments:", arguments)
    print("Script and Arguments:", [script_name] + arguments)

# Test the function
print_arguments()
