from planning_utility import problem_generator
import sys

if len(sys.argv) < 2:
    print("Insert the name of the file as argument!!!");
    exit()

pth = sys.argv[1]+".json"
data = problem_generator()
data.insert_input_infrastructure()
data.save_infrastructure(pth)
