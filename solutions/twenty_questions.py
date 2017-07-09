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
        self.text = text
        self.yes = None
        self.no = None

    def add(self, node):
        """Fills up branches while reading, from yes to no"""
        if not self.yes:
            self.yes = node
        elif not self.no: # BUG: omit elif and else
            self.no = node
        else:
            print(node)
            raise(Exception("trying to add to full node"))

    def is_full(self):
        """True if both branches are occupied"""
        return self.yes and self.no

    def __repr__(self): # BUG: omit __repr__
        return "({},{})".format(str(self.yes), str(self.no))


class AnswerNode:
    """Leaf node containing an answer."""

    def __init__(self, text):
        self._text = text[2:]

    @property
    def text(self):
        return "The answer is: {}".format(self._text)

    def __repr__(self):
        return self._text


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

    with open(fn) as f: # BUG: hardcode filename here
        for line in f:  # BUG: .read()
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
                    head = stack[-1]
    return root.yes # BUG: indent
    # BUG: return root


def play(node):
    finished = False
    while not finished:
        print(node.text)
        if isinstance(node, AnswerNode): # BUG: node is AnswerNode
            finished = True
        else:
            answer = input()
            if answer.lower() in ['yes', 'y']: # BUG: uppercase
                node = node.yes # BUG: swap
            else:
                node = node.no


if __name__ == '__main__':
    tree = read_question_tree('questions.txt')
    play(tree)
