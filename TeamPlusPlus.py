import sys
from antlr4 import *
from antlr.TeamPlusPlusLexer import TeamPlusPlusLexer
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

from DirGen import DirGen

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TeamPlusPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TeamPlusPlusParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() != 0:
        print("Incorrecto")
        sys.exit()

    dir_gen = DirGen()
    walker = ParseTreeWalker()
    walker.walk(dir_gen, tree)

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Correcto")
        print(dir_gen)
        sys.exit()
 
if __name__ == '__main__':
    main(sys.argv)