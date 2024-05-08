"""
file is so tests can use files in the parent directory
"""

import os
import sys

#get the absolute path of the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))

#get the absolute path of the project directory (assuming its the parent of the current script directory)
project_directory = os.path.join(current_script_directory,"..")

#add the project directory to sys.path
sys.path.insert(0,project_directory)

