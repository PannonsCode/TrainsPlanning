//script.js
import {form} from '/form.js';

const F = new form();

function download(content, fileName, contentType) {
    var a = document.createElement("a");
    var file = new Blob([content], {type: contentType});
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
}

function init(){
	
	document.getElementById("ADD").onclick = function(){
		var train = document.getElementById("train").value;
		var from = document.getElementById("from").value;
		var to = document.getElementById("to").value;
		
		F.add(train,from,to);
		
		document.getElementById("inserted").innerHTML = "TRAINS: "+F.trains+"\n"+
														"TRAINS_IN_STATION_INIT: "+F.start_in+"\n"+
														"TRAINS_IN_STATION_GOAL: "+F.arrive_in+"\n"+
														"TRAINS_OUT_STATION_INIT: "+F.start_out+"\n"+
														"TRAINS_OUT_STATION_GOAL: "+F.arrive_out;
		document.getElementById("train").value="";
		document.getElementById("from").value="";
		document.getElementById("to").value="";
	};
	
	document.getElementById("SUBMIT").onclick = function(){
		
		F.trains = F.trains.slice(0,-1);
		F.start_in = F.start_in.slice(0,-1);
		F.arrive_in = F.arrive_in.slice(0,-1);
		F.start_out = F.start_out.slice(0,-1);
		F.arrive_out = F.arrive_out.slice(0,-1);
		
		var json_data = {
							"TRAINS": F.trains,
							"TRAINS_IN_STATION_INIT": F.start_in,
							"TRAINS_IN_STATION_GOAL": F.arrive_in,
							"TRAINS_OUT_STATION_INIT": F.start_out,
							"TRAINS_OUT_STATION_GOAL": F.arrive_out
						}
		json_data = JSON.stringify(json_data);
		console.log(json_data);
		download(json_data, 'problem.json', 'text/plain');
		document.getElementById("inserted").innerHTML = "";
		F.trains = "";
		F.start_in = "";
		F.arrive_in = "";
		F.start_out = "";
		F.arrive_out = "";
	}
}

init();


