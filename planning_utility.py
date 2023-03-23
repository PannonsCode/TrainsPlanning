import json
import requests
from utility import invert_dictionary

class planner:

  def __init__(self, pthfile_infr, pthfile_data):
    self.data_infr = json.load(open(pthfile_infr))
    self.data_problem = json.load(open(pthfile_data))
    self.trains = []
    self.stations = []
    self.raylways = []
    self.busy_rail = []
    self.objects = ""
    self.init = ""
    self.goal = ""
    self.dict_raylways = {}
    self.num_raylways = 1;
    self.read_objects()
    self.read_init()
    self.read_goal()

  '''Generate a string with the pddl code of the problem from data'''
  def generate_pddl(self):

    define = "(define (problem train-problem)\n\n"
    domain = "\t(:domain train-domain)\n\n"
    last_line ="\n)"

    pddl = define+domain+self.objects+self.init+self.goal+last_line

    return pddl

  '''save the pddl code into a file'''
  def save_pddl(self,pth):
    pddl = open(pth,"w")
    pddl.write(self.generate_pddl())
    pddl.close()

  '''connect to a server (passing the pddl files as input) which response with a plan (if it exist)'''
  def find_plan(self, pth_domain, pth_problem):
    data = {'domain': open(pth_domain, 'r').read(),
            'problem': open(pth_problem, 'r').read()}
    resp = requests.post('http://solver.planning.domains/solve', verify=False, json=data).json()

    return resp

  '''read all objects'''
  def read_objects(self):

    self.objects = "\t(:objects "

    #read trains and insert it in the clause "objects"
    self.trains = self.data_problem["TRAINS"].split("-")
    for t in self.trains:
      self.objects += t
      self.objects += " "

    #read stations and insert it in the clause "objects"
    sts = self.data_infr["STATIONS"].split("-")
    for s in sts:
      app = s.split(",")
      self.stations.append(app[0])
      self.objects += app[0]
      self.objects += " "

    #read raylways between stations and insert it in the clause "objects"
    self.pths_stations = self.data_infr["PTH_BTW_STATIONS"].split(";")
    #read all the paths
    for pth in self.pths_stations:
      p = pth.split("-")
      lenght = len(p)

      #analyze a single path
      for i in range(lenght-1):

        rail = p[i]+" - "+p[i+1]
        inv_rail = p[i+1]+" - "+p[i]

        #case of a rail between a station and a node
        if i == 0:
          new_railway = p[i]
          node = p[i+1]
          rail = new_railway+" - "+node
          inv_rail = node+" - "+new_railway

        #case of a rail between a node and a station
        elif i == lenght-2:
          new_railway = p[i+1]
          node = p[i]
          rail = node+" - "+new_railway
          inv_rail = new_railway+" - "+node

        #case of a rail between two nodes
        else:
          node1 = p[i]
          node2 = p[i+1]
          rail = node1+" - "+node2
          inv_rail = node2+" - "+node1
          if rail not in self.dict_raylways.values() and inv_rail not in self.dict_raylways.values():
            new_railway = "R_"+str(self.num_raylways)
            self.num_raylways+=1

        #chek in railways or rails alredy inserted
        if new_railway not in list(self.dict_raylways.keys()) or rail not in self.dict_raylways.values() and inv_rail not in self.dict_raylways.values():
          self.dict_raylways.update({new_railway:rail})
          self.objects += new_railway
          self.objects += " "

    self.objects += ")\n\n"

  '''read initialization of the problem'''
  def read_init(self):

    self.init = "\t(:init "

    #init trains
    for t in self.trains:
      train = "(train "+t+")"
      self.init += train
    self.init += "\n"

    #init stations
    self.init += "\t\t"
    for s in self.stations:
      station = "(station "+s+")"
      self.init += station
    self.init += "\n"

    #init railways
    self.init += "\t\t"
    for r in list(self.dict_raylways.keys()):
      railway = "(railway "+r+")"
      self.init += railway
    self.init += "\n"

    #init railways of each station
    self.init += "\t\t"
    for station in self.data_infr["STATIONS"].split("-"):
      s = station.split(",")[0]
      num_r = station.split(",")[1]
      for i in range(int(num_r)):
        isin = "(isin "+s+"_"+str(i+1)+" "+s+")"
        self.init+=isin
    self.init += "\n"

    #init all the paths
    self.init += "\t\t"
    inv_dict_rails = invert_dictionary(self.dict_raylways)
    done = []
    a = 2;
    for pth in self.pths_stations:
      p = pth.split("-")
      lenght = len(p)

      #init fluent "conn"
      for i in range(lenght-2):
        rail1 = p[i]+" - "+p[i+1]
        railway1 = inv_dict_rails.get(rail1)
        if railway1 is None:
          rail1 = p[i+1]+" - "+p[i]
          railway1 = inv_dict_rails.get(rail1)
        rail2 = p[i+1]+" - "+p[i+2]
        railway2 = inv_dict_rails.get(rail2)
        if railway2 is None:
          rail2 = p[i+2]+" - "+p[i+1]
          railway2 = inv_dict_rails.get(rail2)
        rail = railway1+" "+railway2
        inv_rail = railway2+" "+railway1
        if rail not in done and inv_rail not in done:
          done.append(rail)
          done.append(inv_rail)
          conn = "(conn "+rail+")"
          self.init += conn
          inv_conn = "(conn "+inv_rail+")"
          self.init += inv_conn
      self.init += "\n\t\t"

    #init fluent "at" and "instation"
    init_pos_trains = self.data_problem["TRAINS_IN_STATION_INIT"].split("-")
    for pos in init_pos_trains:
      pos = pos.split(",")
      train = pos[0]
      railway = pos[1]
      station = railway.split("_")[0]
      at1 = "(at "+train+" "+station+")"
      self.init += at1
      at2 = "(at "+train+" "+railway+")"
      self.busy_rail.append(railway)
      self.init += at2
      self.init += "\n\t\t"
      instation = "(instation "+train+")"
      self.init += instation
      self.init += "\n\t\t"

    #init fluent "at" for initial position of trains out of a station
    init_pos_trains = self.data_problem["TRAINS_OUT_STATION_INIT"].split("-")
    for pos in init_pos_trains:
      pos = pos.split(",")
      train = pos[0]
      rail = pos[1]+" - "+pos[2]
      railway = inv_dict_rails.get(str(rail))
      if railway is None:
        rail = pos[2]+" - "+pos[1]
        railway = inv_dict_rails.get(str(rail))
      at = "(at "+train+" "+railway+")"
      self.init += at
      self.busy_rail.append(railway)
    self.init += "\n"

    #init fluent "free"
    self.init += "\t\t"
    for railway in self.dict_raylways.keys():
      if railway not in self.busy_rail:
        free = "(free "+railway+")"
        self.init += free

    self.init += "\n\t)\n\n"

  '''read the goal of the problem'''
  def read_goal(self):

    self.goal = "\t(:goal (and "

    #goal for trains into stations
    init_pos_trains = self.data_problem["TRAINS_IN_STATION_GOAL"].split("-")
    for pos in init_pos_trains:
      pos = pos.split(",")
      train = pos[0]
      station = pos[1]
      at = "(at "+train+" "+station+")"
      self.goal += at
      instation = "(instation "+train+")"
      self.goal += instation

    #goal for trains out of stations
    inv_rails_dict = invert_dictionary(self.dict_raylways)
    init_pos_trains = self.data_problem["TRAINS_OUT_STATION_GOAL"].split("-")
    for pos in init_pos_trains:
      pos = pos.split(",")
      train = pos[0]
      rail = pos[1]+" - "+pos[2]
      railway = inv_rails_dict.get(str(rail))
      if railway is None:
        rail = pos[2]+" - "+pos[1]
        railway = inv_rails_dict.get(str(rail))
      at = "(at "+train+" "+railway+")"
      self.goal += at

    self.goal += ") ) "


'''This class creates a JSON file insertirng data, needed to create a pddl problem file'''
class problem_generator:

	def __init__(self):

		self.trains = ""
		self.stations = ""
		self.rails = ""
		self.init_trains_in = ""
		self.init_trains_out = ""
		self.goal_trains_in = ""
		self.goal_trains_out = ""

	'''Save infrastructure data into a JSON file'''
	def save_infrastructure(self, pth):

		infrastructure = {
				   "STATIONS": self.stations,
				   "PTH_BTW_STATIONS": self.rails,
				  }

		with open(pth, "w") as outfile:
		  json.dump(infrastructure, outfile)
		  
	'''Save problem data into a JSON file'''
	def save_problem(self, pth):

		problem = {
				   "TRAINS": self.trains,
				   "TRAINS_IN_STATION_INIT": self.init_trains_in,
				   "TRAINS_OUT_STATION_INIT": self.init_trains_out,
				   "TRAINS_IN_STATION_GOAL": self.goal_trains_in,
				   "TRAINS_OUT_STATION_GOAL": self.goal_trains_out
				   }

		with open(pth, "w") as outfile:
		  json.dump(problem, outfile)

	'''Insert data'''
	def insert_input_infrastructure(self):

		print("INSERT DATA, ATTENTION: FOLLOW STRICTLY THE SUGGESTED SYNTAX, OTHERWISE THE PROGRAM CAN'T RUN")
		
		self.stations = input("INSERT STAIONS:\n"
							  "(name 1,num raylways-name2,num raylways-...)\n" 
							  "(ex. 'A,3-B,1-...')\n")
		print("\n")

		self.rails = input("INSERT ALL POSSIBLE LINKS BETWEEN STATION AND NODES, SPECIFYING FOR EACH STATION THE NUMBER OF RAILWAY," 
						   "EACH PATH HAS TO BE SEPARETED BY A ';' :\n"
						   "(nameStation_numRailway-node1-node2-...-nameStation_numRailway; ...)\n"
						   "(ex.: 'A_1-N1-N2-N3-N4-B_1;A_2-N1-...')\n")
		print("\n")

	'''----------------------NOT USEED (INSERT FROM HTML FORM)----------------------------------------------------------------------'''

	def insert_input_problem(self):

		self.trains = input("INSERT TRAINS:\n"
							"(name 1-name 2-...)\n"
							"(ex. 'T1-T2-...')\n")
		print("\n")
		
		self.init_trains_in = input("INSERT THE INITIAL POSITION OF TRAIN STOPPED IN A STATION:\n"
									"(nameTrain,nameStation_numRailway- ...)\n "
									"(ex. 'T1,A_1-T2,B_1-...')\n")
		print("\n")
		
		self.init_trains_out = input("INSERT THE INITIAL POSITION OF TRAIN STOPPED IN A RAILWAY, BETWEEN TWO NODES:\n"
									"(nameTrain,node1,node2- ...)\n "
									"(ex. 'T3,N2,N3-...')\n")
		print("\n")
		
		self.goal_trains_in = input("INSERT THE FINAL POSITION OF TRAIN STOPPED IN A STATION:\n"
									"(nameTrain,nameStation- ...)\n"
									"(ex. 'T1,A-T2,B-...')\n")
		print("\n")
		
		self.goal_trains_out = input("INSERT THE FINAL POSITION OF TRAIN STOPPED IN A RAILWAY, BETWEEN TWO NODES:\n"
									"(nameTrain,node1,node2- ...)\n"
									"(ex. 'T3,N2,N3-...')\n")
		print("\n DONE \n")
