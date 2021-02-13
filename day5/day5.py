# FBFBBFFRLR
# F "front"
# B "back"
# L "left"
# R "right"
# i primi 7 caratteri possono essere F o B (indicano precisamente una di 128 righe dell'aereo)
# ricerca binaria (ogni lettera indica la metà)
# F > [0-63], B -> [64 - 127]
# gli ultimi tre caratteri saranno L o R (specificano una delle 8 colonne dell'aereo)
# L -> lower half, R -> upper half

# id del posto: row * 8 + column

def get_half(bottom, top, lower):
    mid = (bottom+top)//2
    if lower:
        return bottom, mid
    else:
        return mid, top

seats = ["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]

occupied = [[0 for i in range(8)] for j in range(128)]

with open("input.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        seats.append(line.replace("\n",""))

higher_id = 0
for seat in seats:
    bottom, top = 0, 128
    for i in range(7):
        move = seat[i]
        bottom, top = get_half(bottom, top, move=="F")
    row = bottom

    bottom,top = 0, 8
    for i in range(7, 10):
        move = seat[i]
        bottom, top = get_half(bottom, top, move=="L")
    col = bottom

    id = row*8+col
    occupied[row][col] = id

    if id > higher_id:
        higher_id = id

print(higher_id)
for index in range(len(occupied)):
    print(occupied[index])

