from planning_utility import planner
from time import sleep
import sys

PTH_DOMAIN = "train-domain.pddl"
PTH_PROBLEM = "problem.pddl"

if len(sys.argv) < 3:
	print("Insert the argumets!!")
	exit()
pth_infr = sys.argv[1]+".json"
pth_problem = sys.argv[2]+".json"
problem = planner(pth_infr,pth_problem)
problem.save_pddl(PTH_PROBLEM)
res = problem.find_plan(PTH_DOMAIN,PTH_PROBLEM)

print("Computing plan...")
sleep(5)

if res['status'] == 'ok':
  print("PLAN FOUND!")

  print("\nDetails on search:")
  out = res['result']['output'].split('\n')
  for i in range(2,7):
    print(out[-i])

  print("\nPlan:")
  plan = '\n'.join([act['name'] for act in res['result']['plan']])
  print(plan)

  print("\nDetails of the plan:")
  chars = '()'
  actions = plan.translate(str.maketrans('', '', chars))
  actions = actions.split("\n")
  for a in range(len(actions)):
    print("ACTION N."+str(a+1)+":")
    act = actions[a].split(" ")
    if act[0] == "ready_to_start":
      if "_" in str(act[3]):
        print("Train "+str.upper(act[1])+" available on railway "+str.upper(act[3])+" of station "+str.upper(act[2]))
      else:
        print("Train "+str.upper(act[1])+" available on railway "+str.upper(act[2])+" of station "+str.upper(act[3]))
    if act[0] == "stop":
      if "_" in str(act[3]):
        print("Train "+str.upper(act[1])+" stopped at railway "+str.upper(act[3])+" of station "+str.upper(act[2]))
      else:
        print("Train "+str.upper(act[1])+" stopped at railway "+str.upper(act[2])+" of station "+str.upper(act[3]))
    if act[0] == "move":
      rail = problem.dict_raylways.get(str.upper(act[2]))+"-"+problem.dict_raylways.get(str.upper(act[3]))
      chars = " "
      rail = rail.translate(str.maketrans('', '', chars))
      rail = rail.split("-")
      if rail[1]==rail[2]:
        print("Move train "+str.upper(act[1])+" on rail "+rail[0]+"-"+rail[1]+"-"+rail[3])
      elif rail[0]==rail[3]:
        print("Move train "+str.upper(act[1])+" on rail "+rail[1]+"-"+rail[0]+"-"+rail[2])
      elif rail[0]==rail[2]:
        print("Move train "+str.upper(act[1])+" on rail "+rail[1]+"-"+rail[0]+"-"+rail[3])
      elif rail[1]==rail[3]:
        print("Move train "+str.upper(act[1])+" on rail "+rail[0]+"-"+rail[1]+"-"+rail[2])
    print("\n")
else:
  print("PLAN NOT FOUND!")
