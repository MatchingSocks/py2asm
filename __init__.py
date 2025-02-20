import os
import sys

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Add the tests directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "tests")))
