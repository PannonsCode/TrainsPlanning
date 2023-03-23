//form

class form{
	
	constructor(){
		this.trains_array = Array();
		this.trains = "";
		this.start_in = "";
		this.start_out = "";
		this.arrive_in = "";
		this.arrive_out = "";
	}
	
	add(train,from,to){
		if(!this.in_array(train,this.trains_array)){
			
			this.trains_array.push(train);
			this.trains = this.trains+train+"-";
			
			var splitted = from.split(",");
			if(splitted.length==2)
				this.start_out = this.start_out+train+","+from+"-";
			else
				this.start_in = this.start_in+train+","+from+"-";
				
			var splitted = to.split(",");
			if(splitted.length==2)
				this.arrive_out = this.arrive_out+train+","+to+"-";
			else
				this.arrive_in = this.arrive_in+train+","+to+"-";				

		}
		else{
			console.log("Train itinerary alredy present, insert another one");
		}	

	}
	
	in_array(t, array){
		for(var i = 0; i<array.length; i++) {
			if(t == array[i]) {
				return true;
			}
		}
		return false;
	}
}

export {form}
