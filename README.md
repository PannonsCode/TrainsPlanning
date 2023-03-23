This folder contains the following files:
- A notebook ("planning_project.ipynb") containing all the code of the project, used to work on the prject
- 4 python files to run the program from shell:
	- 'infrastructure_generator.py' to generate a new '.json' file with the infratstructure of the railway
	- 'train_planning.py' to create 'problem.pddl' and find a plan for it
	- 'planning_utility.py' containig the definition of classes used
	- 'utility.py' containig a function used 
- A 'train_domain.pddl' file containing the domain definition of the problem
- A 'problem.pddl' file containing an instance of the problem, a new one can be generated
- 3 default 'infastructure_i.json' file containing the data of the infrastructure to generate the instance of a problem into a pddl file
- 3 default 'problem_i.json' file containing the data of trains itineray, to generate the instance of a problem into a pddl file
- A folder 'form', containing the files to open a local web page with a form to generate a new 'problem.json'
- A 'requirment.txt' file, to install external libraries
- A report ('report.pdf')

============================================================================================================================================================

To run the following commands, make sure to execute the shell in the directory of the project ("planning_project")

First to run the prject you have to check if all needed packages are installed, to do it run:

>pip install -r requirements.txt

============================================================================================================================================================

To generate and solve a problem you need 2 json files: one for the infrastructure of the railway, one for the itinerary of the trains

-------------------------------------------------------------------------------------------------------------------------------------------------------------

For the infrastructure you can chose if use one of the default file ('infrastructure_1', 'infrastructure_2', 'infrastructure_3') or
generating a new infrastructure running:

>python infrastructure_generator.py name_file

-------------------------------------------------------------------------------------------------------------------------------------------------------------

For the train itineray, you can generate a file using a local web page with a form, to do this:

-open a new terminal in the folder /planning_project/form and run: > http-server
-copy this url on your browser: "http://127.0.0.1:8080/form.html"
-Oss: chek the ip and the door in the terminal where you lunched "http-server" command if the page don't run
-When click on "Submit button", a file 'problem.json' will be downloaded
-move the 'problem.json' file from your download folder to the folder of this project ("planning_project")
-there are 3 existent files for 3 different problems ('problem_1.json','problem_2.json','problem_3.json')

-------------------------------------------------------------------------------------------------------------------------------------------------------------

To find a plan, run:

>python train_planning.py name_infrastructure problem

-'name_infrastructure' can be {'infrastructure_1', 'infrastructure_2', 'infrastructure_3'} or a name you choosed if you create a new infrastrucure
-'problem' is the downloaded file, if you re-name it change this name in the argument; if you use an existent problem use 'problem_1' with 'infrastructure_1',
 'problem_2' with 'infrastructure_2', 'problem_3' with 'infrastructure_3'
-ATTENTION: make sure that the problem generated refer to the right infrastructure: if you use one of the pre-defined infrastructure, you can generate new
 problem files referreing to the corresponding image of the infrastructure on the report at page [i]; if you generate a new infrastructure, use the same names
 for the station, railways and nodes in the form to generate a problem.
-If some errors occur, probably the data are not inserted correctly, else if the result is ‘PLAN NOT FOUND!’, a plan not exist.

