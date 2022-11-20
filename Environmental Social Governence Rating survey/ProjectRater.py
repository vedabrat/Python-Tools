import time
import math

questions = [
    "Does this program end poverty in all its forms everywhere?",
    "Does this program end hunger, achieve food security and improved nutrition, and promote sustainable agriculture?",
    "Does this program ensure healthy lives and promote well-being for all at all ages?",
    "Does this program ensure inclusive and equitable quality education and promote life-long learning opportunities for all?",
    "Does this program achieve gender equality and empower all women and girls?",
    "Does this program ensure availability and sustainable management of water sanitation for all?",
    "Does this program ensure access to affordable, reliable, sustainable, and modern energy for all?",
    "Does this program promote sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all?",
    "Does this program build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation?",
    "Does this program reduce inequality within and among countries?",
    "Does this program make cities and human settlements inclusive, safe, resilient and sustainable?",
    "Does this program ensure sustainable consumption and production patterns?",
    "Does this program take urgent action to combat climate change and its impacts?",
    "Does this program conserve and sustainably use the oceans, seas and marine resources for sustainable development?",
    "Does this program protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land, degradation and halt biodiversity loss",
    "Does this program promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive, institutions at all levels",
    "Does this program strengthen the means of implementation and revitalize the global partnership for sustainable development?" 
]

score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def body(x):

    indivScore = input()
    if (indivScore == "Y"):
        score[x] = 1
        # print("your score has been added")
    elif (indivScore == "y"):
        score[x] = 1
        # print("your score has been added")
    # else:
        # print("0 points")

print("Please enter your response as Y or N and press enter")   
time.sleep(1)
for x in range(17):
    print( str(x + 1) + " " + str(questions[x-1]))
    body(x)

# print(score)
sum = 0
for i in range(0, len(score)):    
   sum = sum + score[i];    
     
# print("Sum of all the elements of an array: " + str(sum));    
finalScore = math.ceil(( sum/len(questions) )*100)

# print(finalScore)

print("Your program scored " +  str(finalScore) + " out of 100.")