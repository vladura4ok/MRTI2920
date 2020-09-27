import csv

name = "Audi.csv"
 
auto = [
    {"Model" : "80 1.6 Spaces", "Year" : 1989, "Horsepower" : 69, "Engine size" : "1595 cm3 (97.3 cu-in)"},
    {"Model" : "80 1.6 Spaces", "Year" : 1993, "Horsepower" : 102, "Engine size" : "1595 cm3 (97.3 cu-in)"},
    {"Model" : "80 1.8 Spaces", "Year" : 1986, "Horsepower" : 75, "Engine size" : "1781 cm3 (108.7 cu-in)"},
    {"Model" : "80 1.8 Spaces", "Year" : 1989, "Horsepower" : 90, "Engine size" : "1781 cm3 (108.7 cu-in)"},
    {"Model" : "80 1.8 S Spaces", "Year" : 1986, "Horsepower" : 88, "Engine size" : "1781 cm3 (108.7 cu-in)"},
    {"Model" : "80 1.9 E Spaces", "Year" : 1986, "Horsepower" : 113, "Engine size" : "1847 cm3 (112.7 cu-in)"},
    {"Model" : "80 1.9 E Quattro Spaces", "Year" : 1986, "Horsepower" : 113, "Engine size" : "1847 cm3 (112.7 cu-in)"}]


with open(name, "w", newline="") as file:
    columns = ["Model", "Year", "Horsepower", "Engine size"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(auto)