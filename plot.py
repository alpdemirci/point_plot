from tkinter import Tk, Canvas

name = input("Enter file name:")  # file name (for this project:hw4)
point = {}  # point can be called as their id
X = []   # Using to find maximum and minimum X value
Y = []  # Using to find maximum and minimum Y value
arc = []  # First column --> start point id, second column --> end point id
while True:
    """
    File reading
    fline --> point array
    aline --> arc array
    """
    try:
        ff = open(name+".xyz", "r")  # node file
        fa = open(name+".nno", "r")  # arc file
        break
    except FileNotFoundError:  # Checks the existence of file at same directory
        name = input("Enter file name")
fline = ff.readlines()
aline = fa.readlines()
for i in aline:
    i = i.split()
    try:
        arc.append([i[0], i[1]])
    except IndexError:
        pass
for i in fline:
    i = i.split()
    try:
        X.append(float(i[1]))
        Y.append(float(i[2]))
    except IndexError:
        pass
# will be substract X values because of tkinter could not show negative value
minx = min(X)
# will be substract Y values because of tkinter could not show negative value
miny = min(Y)
deltax = max(X) - min(X)  # Determine scale
deltay = max(Y) - min(Y)  # Determine scale

root = Tk()

h = root.winfo_screenheight()
w = root.winfo_screenwidth() / 2
cnv = Canvas(root, width=w, height=h)  # Canvas size determined
sclx = (deltax / w) * 1.25  # scale of x values
scly = (deltay / h) * 1.25  # scale of x values
scl = max(sclx, scly)  # scale determined small one
for i in fline:
    try:
        i = i.split()
        x = float(i[1])
        y = float(i[2])
        tx = (x - minx) / scl + 50  # (x-minx)--> negative values does positive
# max(Y) - y --> tkinter origin point is left-up
# +50 --> used due to window bar
        ty = (max(Y)-y+50)/scl
        point[i[0]] = [tx, ty]   # this dict will using drawing arc
    except IndexError:
        pass
for i in range(len(arc)):
    try:
        id1 = arc[i][0]  # arc starting point id
        id2 = arc[i][1]  # arc end point id
        x1, y1 = point[id1][0], point[id1][1]  # x1,y1 are start point coord.
        x2, y2 = point[id2][0], point[id2][1]  # x2,y2 are end point coord.
        cnv.create_line(x1, y1, x2, y2, fill="black")  # line created
    except KeyError:  # if any points are deleted, their lines will not create
        pass
for i in point:
    tx, ty = point[i][0], point[i][1]  # tx ,ty are point coord.
    cnv.create_text(tx+12, ty-7, text=i)  # text created North-East of point
    cnv.create_oval(tx-3, ty-3, tx+3, ty+3, fill="orange")  # (r = 3 unit)
    cnv.pack()
root.mainloop()
