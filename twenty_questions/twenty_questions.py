"""
Twenty Questions

Data from: https://github.com/knkeniston/TwentyQuestions/
"""
class QuestionNode:
    """
    Node in a binary tree that contains a question
    and two possible answers
    """
    def __init__(self, text):
        self.text = text.strip()
        self.yes = None
        self.no = None

    def add(self, node):
        """Fills up branches while reading, from yes to no"""
        if not self.yes:
            self.yes = node
        self.no = node
        
    def is_full(self):
        """True if both branches are occupied"""
        result = self.yes and self.no


class AnswerNode:
    """Leaf node containing an answer."""

    def __init__(self, text):
        self._text = text[2:].strip()

    @property
    def text(self):
        return "The answer is: {}".format(self._text)


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
    root = QuestionNode("root") # deleted at the end
    stack = [root]              # nodes to process later

    with open('quetions.txt') as f:
        for line in f.read():
            head = stack[-1]
            if line.startswith('Q:'):
                question = QuestionNode(line)
                head.add(question)
                stack.append(question)
            elif line.startswith('A:'):
                head.add(AnswerNode(line))
                # find last unfinished node
                while head.is_full() and stack:
                    stack.pop()
                head = stack[-1
            return root.yes


def play(node):
    finished = False
    while not finished:
        print(node.text)
        if node is AnswerNode:
            finished = True
        else:
            answer = input()
            if answer.lower() in ['YES', 'Y']:
                node = node.no
            else:
                node = node.yes


if __name__ == '__main__':
    tree = read_question_tree('questions.txt')
    play(tree)
