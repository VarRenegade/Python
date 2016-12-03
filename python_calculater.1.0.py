start_list = input().split()
start_list[0] = int(start_list[0])
start_list[2] = int(start_list[2])

def add(start_list):
	return start_list[0]+start_list[2]
	
def subtract(start_list):
	return start_list[0]-start_list[2]
	
def multiply(start_list):
	return start_list[0]*start_list[2]
	
def divide(start_list):
	return start_list[0]/start_list[2]

if(start_list[1] == "+"):
	end_num=add(start_list);
elif(start_list[1] == "-"):
	end_num=subtract(start_list);
elif(start_list[1] == "*"):
	end_num=multiply(start_list);
elif(start_list[1] == "/"):
	end_num=divide(start_list);

print(end_num)
	

