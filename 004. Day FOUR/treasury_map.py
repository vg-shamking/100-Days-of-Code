row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]
mappa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = mappa[vertical - 1]
selected_row[horizontal - 1] = "1"
print(f"{row1}\n{row2}\n{row3}")
