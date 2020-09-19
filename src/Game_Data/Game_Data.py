x_field = 1
y_field = 0
mine_field = 0

def set_initial_data(data):
    global x_field
    global y_field
    global mine_field

    x_field = data[0]
    y_field = data[1]

    if data[2] > (data[0]*data[1])/2:
        mine_field = data[0]*data[1]/2
    else:
        mine_field = data[2]
