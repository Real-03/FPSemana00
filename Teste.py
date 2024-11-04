n_columns = 5
n_rows = 5
room_desc = []
for i in range(0, n_columns):
    room_desc.append([])
    for j in range(0, n_rows):
        room_desc[i].append("Description of room x="+str(i)+", y="+str(j))
print(room_desc[0])     
