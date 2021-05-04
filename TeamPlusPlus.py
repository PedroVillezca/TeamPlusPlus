import sys
from antlr4 import *
from antlr.TeamPlusPlusLexer import TeamPlusPlusLexer
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

from src.CustomListener import CustomListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TeamPlusPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TeamPlusPlusParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() != 0:
        print("Unsuccessful Compilation...")
        sys.exit()

    custom_listener = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(custom_listener, tree)

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Successful Compilation!")
        print(custom_listener)
        sys.exit()
 
if __name__ == '__main__':
    main(sys.argv)