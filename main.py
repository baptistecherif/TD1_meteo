data = {}
with open("meteo.data.txt", "w") as file:
    for line in file:
        year, month, time = line.strip().split("\t")
        data[int(year), int(month), int(time)] = int(time)
    string = ""
    for year in range(1991, 2001):
        string += "<tr>" + "<td>" + str(year) + "<td>"
    for month in range (1, 12):
        string += "<td>" + str(data[year, month]) + "</td>"
    string += "</try>"
    string += "</table>"

def
