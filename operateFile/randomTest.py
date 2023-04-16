from cgi import test
from fileinput import filename
import os
import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

targetPath = (os.path.abspath("."),)
print(targetPath[0])


def createTest():
    for i in range(5):
        testfilename = str(i) + ".txt"
        answerfilename = str(i) + "answer.txt"
        with open(
            os.path.join(targetPath[0], testfilename), "w", encoding="utf-8"
        ) as test1:
            test1.write("geography_exam\n")
            test1.write("class:_______\n")
            test1.write("name: _______\n")
        with open(
            os.path.join(targetPath[0], answerfilename), "w", encoding="utf-8"
        ) as answer1:
            answer1.write(" " * 20 + "试题答案\n")
        # 开始写试题内容
        states = list(capitals.keys())
        # 打乱列表排序
        random.shuffle(states)

        for i in range(50):
            qustion = states[i]
            answers_to_questions = capitals[qustion]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(answers_to_questions)]
            wrongAnswer3 = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswer3 + [answers_to_questions]
            random.shuffle(answerOptions)

            with open(
                os.path.join(targetPath[0], testfilename), "a", encoding="utf-8"
            ) as test2:
                test2.write("%s: 请问%s的首府是哪里?\n" % (i + 1, qustion))
                test2.write(" " * 4)
                for j in range(4):
                    test2.write("%s:%s\t" % ("ABCD"[j], answerOptions[j]))
                test2.write("\n")
            with open(
                os.path.join(targetPath[0], answerfilename), "a", encoding="utf-8"
            ) as answer2:
                answer2.write(
                    "%s:  答案:%s 选项:%s\n"
                    % (
                        i + 1,
                        answers_to_questions,
                        "ABCD"[answerOptions.index(answers_to_questions)],
                    )
                )


createTest()
