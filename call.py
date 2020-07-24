import csv
import random
from gtts import gTTS 
import playsound

MP3FILE = "student.mp3"

students = []

with open('list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    HEADLINE = True
    for row in csv_reader:
        if HEADLINE:
            HEADLINE = False
            continue

        if not row[-1]:
            students.append(row[0])
           

student = random.choice(students).upper()

speech = gTTS(text=student, lang='ru', slow=False)
speech.save(MP3FILE)

print(student)
playsound.playsound(MP3FILE)
input()
