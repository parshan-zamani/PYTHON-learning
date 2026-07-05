print("Hello and good morning !")

scores = {}
scores2 = []

count = int(input("please enter the number of the students : "))

for i in range(count):
    name = str(input(f"please enter the name of the student {i+1} : "))
    score = float(input(f"please enter the score of the student {i+1} : "))

    scores[name] = score

    scores2.append(score)

for name,score in scores.items():

   print(name,":",score)

print(scores2)
a = (sum(scores2))/(len(scores2))
h = max(scores2)
l = min(scores2)
print("the average = ",a )
print("the highest score = ",h)
print("the lowest score = ",l)
s = str(input("If you want to search for a special student's score , type his or her name : "))
if s in scores :
    print(scores[s])
else :
    print("Student not found !")


