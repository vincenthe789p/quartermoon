from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
import csv

#Currently Not Functional, However should b easy to implement
with open('febData2020.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 100
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

#Assume we filter the data into purely tweets to perform sediment analysis (Use raw data for now for demo)
train = [
("Still fighting bushfires in #mallacoota - situation critical near raheen and radley. Just caught a break in the wind. We’re controlling as best we can to save sister’s place. Tea trees are exploding infernos.", 'shelter'),
("Mallacoota locals understand this as the inevitable and overdue outcome of living in the middle of a national park after many years of drought. Power outages are very common and many ppl equipped with generators. I feel for the visitors expecting a holiday.", "shelter"
),

("My family are safe, billeted with friends. Fire hit my place late in the day yesterday.  My heart goes out to everyone in the valley.", 'shelter'),
("Devastated that my family cant enjoy a good christmas dinner without power. These fires are getting worst. Pray they stop soon.", 'shelter'),
("Devastation. Property damaged by the East Gippsland fires is seen in Sarsfield, Victoria, #Australia January 1, 2020.  #Australiabushfire", 'shelter'),
("I can't deal with this", 'healthcare'),
("im emotionally broken from the fire", "healthcare"),
("I can't deal with this", 'healthcare'),
("The fire is causing a terrible shock on my mental state", "healthcare"),
("This really hurt my family financially as we can not afford healthcare and their are no hopsitals", "healthcare"),
("All the hospitals are full and people are suffering on the streets", "healthcare"),
("I lost my house and my property", "shelter"),
("I need shelter here", "shelter"),
("I need shelter over here", "shelter"),
("I need shelter really bad", "shelter"),
("We need help, we need shelter", "shelter"),
("I need shelter urgently", "shelter"),
("I need shelter", "shelter"),
("I need shelter", "shelter"),
("I need shelter", "shelter"),
("I need shelter now", "shelter")
]

test = [
("Still fighting bushfires in #mallacoota - situation critical near raheen and radley. Just caught a break in the wind. We’re controlling as best we can to save sister’s place. Tea trees are exploding infernos.", 'shelter'),
("Mallacoota locals understand this as the inevitable and overdue outcome of living in the middle of a national park after many years of drought. Power outages are very common and many ppl equipped with generators. I feel for the visitors expecting a holiday.", "shelter"
),

("My family are safe, billeted with friends. Fire hit my place late in the day yesterday.  My heart goes out to everyone in the valley.", 'shelter'),
("Devastated that my family cant enjoy a good christmas dinner without power. These fires are getting worst. Pray they stop soon.", 'shelter'),
("Devastation. Property damaged by the East Gippsland fires is seen in Sarsfield, Victoria, #Australia January 1, 2020.  #Australiabushfire", 'shelter'),
("I can't deal with this", 'healthcare'),
("im emotionally broken from the fire", "healthcare"),
("I can't deal with this", 'healthcare'),
("The fire is causing a terrible shock on my mental state", "healthcare"),
("This really hurt my family financially as we can not afford healthcare and their are no hopsitals", "healthcare"),
("All the hospitals are full and people are suffering on the streets", "healthcare"),
("I lost my house and my property", "shelter"),
("I need shelter", "shelter"),
("I need shelter", "shelter"),
("I need shelter really bad", "shelter"),
("We need help, we need shelter", "shelter"),
("Very sad right now and depressed", "healthcare"),
("I need shelter", "shelter"),
("I need shelter", "shelter"),
("The hospitals here are all full", "healthcare"),
("I need shelter", "shelter"),
("I need healthcare", "healthcare"),
("I am concerned about my children's meantal well being and health, the earthquake has caused big stress", "healthcare")
]


# BASIC TESTING FRAMEWORK USING NAIVE BAYES CLASSIFIER MODEL
print("Beginning training set")
classy = NaiveBayesClassifier(train)
print("Training set ended")

print("Beginning testing set")
totalCorrect = 0
totalTestPoints = len(test)
for testPoint in test:
    print("Checking: {}".format(testPoint))
    print("Focus on shelter probability: {}".format(classy.prob_classify(testPoint[0]).prob("shelter")))
    print("Focus on healthcare probability {}".format(classy.prob_classify(testPoint[0]).prob("healthcare")))
    prediction = classy.classify(testPoint[0])
    if (prediction == testPoint[1]):
        totalCorrect += 1
print()
print("=================")
print()
print("Overall Test Accuracy: {0:.2f}%".format((totalCorrect/totalTestPoints)* 100))
classy.show_informative_features(8)
