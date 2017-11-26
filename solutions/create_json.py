"""
Twenty Questions

Data from: https://github.com/knkeniston/TwentyQuestions/
"""
import json

def read_question_tree(fn):
    """
    Reads a question tree from a text file
    containing a series of lines like
      Q: first question
      Q: second question, asked if first answer is 'yes'
      A: you answered: yes, yes
      A: you answered: yes, no
      Q: asked if first answer no
      A: you answered: no, yes
      A: you answered: no, no
    """ 
    tree = {}
    stack = [tree]

    with open(fn) as f: # BUG: hardcode filename here
        for line in f:  # BUG: .read()
            head = stack.pop()
            head['text'] = line.strip()[2:]
            if line.startswith('Q:'):
                head['yes'] = {}
                head['no'] = {}
                stack.append(head['no'])
                stack.append(head['yes'])
                
    return tree


if __name__ == '__main__':
    tree = read_question_tree('../twenty_questions/questions.txt')
    #tree = read_question_tree('mini.txt')
    with open('questions.json', 'w') as f:
        f.write(json.dumps(tree))
