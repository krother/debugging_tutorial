"""
Twenty Questions

Data from: https://github.com/knkeniston/TwentyQuestions/
"""
import json

def is_answer(node):
    return len(node) == 1


f = open('../twenty_questions/questions.json')
content = f.read()
node = json.loads(content)

finished = False
while not finished:
    print(node['text'])
    if is_answer(node):
        finished = True
    else:
        answer = input()
        if answer.lower() in ['yes', 'y']:
            node = node['yes']
        else:
            node = node['no']
