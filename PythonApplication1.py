// creatung new branch
input_count = int(input())
seat_plan = {1:"WS",2:"MS",3:"AS",4:"AS",5:"MS",0:"WS"}

for i in range(input_count):
    current_seat = int(input())
    front_seat = 0
    seat_type = ""
    x = current_seat % 12
    y = 2*( (6 -x) % 6) + 1

    if((x > 6)):
        front_seat = current_seat - (2*(x-6)) + 1
    elif(x == 0):
        front_seat = current_seat - 11
    else:
        front_seat = current_seat + y

    z = front_seat % 6
    
    seat_type = seat_plan[z]
        
    print( str(front_seat) + " " + str(seat_type) )
