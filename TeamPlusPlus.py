import sys
from antlr4 import *

from antlr.TeamPlusPlusLexer import TeamPlusPlusLexer
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser
from src.CustomListener import CustomListener
from src.VirtualMachine import VirtualMachine

"""
Main logic for TeamPlusPlus program. First runs through the input
with ANTLR's parser to fill out the General Directory and Quadruple
List, then runs the Virtual Machine with the compiled information.
"""

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
        if '-d' in argv:
            # Print General Directory and Quadruple List alongside results
            print(custom_listener)
        if '-c' in argv:
            # Print just Quadruple List alongside results
            print(custom_listener.quadruple_list)
        if '-f' in argv:
            # Print just General Directory alongside results
            print(custom_listener.dir_gen)
        if '-o' in argv:
            # Print Operator Stack alongside results
            print(custom_listener.quadruple_list.p_operators)
        if '-v' in argv:
            # Print Operand Stack alongside results
            print(custom_listener.quadruple_list.p_operands)

        
        virtual_machine = VirtualMachine(custom_listener.dir_gen, custom_listener.quadruple_list.quadruple_list)
        virtual_machine.run()
        sys.exit()
 
if __name__ == '__main__':
    main(sys.argv)