class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark
Amount = 0
Best_pupils = []
Sum = 0

with open("pupils_large.txt", "r", encoding = "utf-8") as file:
    for line in file:
        data = line.split(" ")
        data_pupil = Pupil(data[0], data[1], int(data[2]))


        if data_pupil.Mark == 5:
            Best_pupils.append(data_pupil.Surname)
        Amount += 1 
        Sum += int(data_pupil.Mark)

print("Середня оцінка:", (Sum/Amount), "\n\nКількість відмінників:", len(Best_pupils))