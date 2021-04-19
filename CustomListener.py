from antlr4 import *
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

from DirGen import DirGen
from QuadrupleList import QuadrupleList

class CustomListener(TeamPlusPlusListener):
    dir_gen = DirGen()
    quadruple_list = QuadrupleList()

    def __repr__(self):
        return f'\nDir Gen: \n {self.dir_gen} \n\n Quadruple List: \n {self.quadruple_list}'

    # Point 1
    def enterProgram(self, ctx):
        self.dir_gen.enterProgram(ctx)
        
    # Point 9 
    def enterClasses(self, ctx):
        self.dir_gen.enterClasses(ctx)
        
    # Point 11
    def exitClasses(self, ctx):
        self.dir_gen.exitClasses(ctx)
        
    # Point 2
    def enterTpp_class(self, ctx):
        self.dir_gen.enterTpp_class(ctx)
        
    # Point 3
    def exitInherit(self, ctx):
        self.dir_gen.exitInherit(ctx)
            
    # Point 6
    def exitId_type(self, ctx):
        self.dir_gen.exitId_type(ctx)
    
    # Point 7
    def enterInit(self, ctx):
        self.dir_gen.enterInit(ctx)
        
    # Point 5
    def exitVoid_type(self, ctx):
        self.dir_gen.exitVoid_type(ctx)
    
    # Point 12
    def enterDeclare_func(self, ctx):
        self.dir_gen.enterDeclare_func(ctx)
    
    # Point 8
    def exitDeclare_func(self, ctx):
        self.dir_gen.exitDeclare_func(ctx)
        
    # Point 7
    def exitParam(self, ctx):
        self.dir_gen.exitParam(ctx)
        
    # Point 13
    def exitFunblock(self, ctx):
        self.dir_gen.exitFunblock(ctx)

    # Point 10
    def enterMain(self, ctx):
        self.dir_gen.enterMain(ctx)
    
    # Point 5
    def exitTpp_type(self, ctx):
        self.dir_gen.exitTpp_type(ctx)

    # Point 4
    def exitLevel(self, ctx):
        self.dir_gen.exitLevel(ctx)