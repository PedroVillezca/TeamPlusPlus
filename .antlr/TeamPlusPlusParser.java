// Generated from d:\Respaldo\Gibran\Proyectos_Programacion\Compis\TeamPlusPlus\TeamPlusPlus.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TeamPlusPlusParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, INT=2, FLOAT=3, CHAR=4, VARS=5, CLASS=6, INHERITS=7, MAIN=8, 
		IF=9, ELSE=10, THEN=11, FUNC=12, RETURN=13, READ=14, PRINT=15, WHILE=16, 
		FROM=17, TO=18, ATTRIBUTES=19, METHODS=20, IMPORT=21, AS=22, PUBLIC=23, 
		PRIVATE=24, AND=25, OR=26, NOT=27, COLON=28, COMMA=29, DOT=30, ASSIGN=31, 
		LEFT_BRACE=32, RIGHT_BRACE=33, LEFT_PARENTHESIS=34, RIGHT_PARENTHESIS=35, 
		LEFT_BRACKET=36, RIGHT_BRACKET=37, SEMICOLON=38, PLUS=39, MINUS=40, MULT=41, 
		DIV=42, EQUALS=43, GREATER_THAN=44, LESS_THAN=45, GREATER_EQUALS=46, LESS_EQUALS=47, 
		DIFFERENT=48, CTE_INT=49, CTE_FLOAT=50, CTE_CHAR=51, CTE_STRING=52, ID=53, 
		COMMENT=54, WHITESPACE=55;
	public static final int
		RULE_program = 0, RULE_imports = 1, RULE_classes = 2, RULE_tpp_vars = 3, 
		RULE_c_vars = 4, RULE_var = 5, RULE_init = 6, RULE_functions = 7, RULE_c_functions = 8, 
		RULE_main = 9, RULE_funblock = 10, RULE_tpp_type = 11, RULE_level = 12, 
		RULE_statement = 13, RULE_assignment = 14, RULE_funcall = 15, RULE_tpp_return = 16, 
		RULE_read = 17, RULE_tpp_print = 18, RULE_block = 19, RULE_condition = 20, 
		RULE_loop = 21, RULE_wloop = 22, RULE_floop = 23, RULE_expression = 24, 
		RULE_expression_A = 25, RULE_express = 26, RULE_exp = 27, RULE_term = 28, 
		RULE_factor = 29, RULE_relop = 30, RULE_sumop = 31, RULE_mulop = 32, RULE_value = 33;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "imports", "classes", "tpp_vars", "c_vars", "var", "init", 
			"functions", "c_functions", "main", "funblock", "tpp_type", "level", 
			"statement", "assignment", "funcall", "tpp_return", "read", "tpp_print", 
			"block", "condition", "loop", "wloop", "floop", "expression", "expression_A", 
			"express", "exp", "term", "factor", "relop", "sumop", "mulop", "value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'int'", "'float'", "'char'", "'vars'", "'class'", 
			"'inherits'", "'main'", "'if'", "'else'", "'then'", "'func'", "'return'", 
			"'read'", "'print'", "'while'", "'from'", "'to'", "'attributes'", "'methods'", 
			"'import'", "'as'", "'public'", "'private'", "'and'", "'or'", "'not'", 
			"':'", "','", "'.'", "'='", "'{'", "'}'", "'('", "')'", "'['", "']'", 
			"';'", "'+'", "'-'", "'*'", "'/'", "'=='", "'>'", "'<'", "'>='", "'<='", 
			"'!='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "INT", "FLOAT", "CHAR", "VARS", "CLASS", "INHERITS", 
			"MAIN", "IF", "ELSE", "THEN", "FUNC", "RETURN", "READ", "PRINT", "WHILE", 
			"FROM", "TO", "ATTRIBUTES", "METHODS", "IMPORT", "AS", "PUBLIC", "PRIVATE", 
			"AND", "OR", "NOT", "COLON", "COMMA", "DOT", "ASSIGN", "LEFT_BRACE", 
			"RIGHT_BRACE", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", 
			"RIGHT_BRACKET", "SEMICOLON", "PLUS", "MINUS", "MULT", "DIV", "EQUALS", 
			"GREATER_THAN", "LESS_THAN", "GREATER_EQUALS", "LESS_EQUALS", "DIFFERENT", 
			"CTE_INT", "CTE_FLOAT", "CTE_CHAR", "CTE_STRING", "ID", "COMMENT", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TeamPlusPlus.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TeamPlusPlusParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(TeamPlusPlusParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(TeamPlusPlusParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(TeamPlusPlusParser.SEMICOLON, 0); }
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public TerminalNode EOF() { return getToken(TeamPlusPlusParser.EOF, 0); }
		public ImportsContext imports() {
			return getRuleContext(ImportsContext.class,0);
		}
		public ClassesContext classes() {
			return getRuleContext(ClassesContext.class,0);
		}
		public Tpp_varsContext tpp_vars() {
			return getRuleContext(Tpp_varsContext.class,0);
		}
		public FunctionsContext functions() {
			return getRuleContext(FunctionsContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(PROGRAM);
			setState(69);
			match(ID);
			setState(70);
			match(SEMICOLON);
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IMPORT) {
				{
				setState(71);
				imports();
				}
			}

			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CLASS) {
				{
				setState(74);
				classes();
				}
			}

			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARS) {
				{
				setState(77);
				tpp_vars();
				}
			}

			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FUNC) {
				{
				setState(80);
				functions();
				}
			}

			setState(83);
			main();
			setState(84);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImportsContext extends ParserRuleContext {
		public List<TerminalNode> IMPORT() { return getTokens(TeamPlusPlusParser.IMPORT); }
		public TerminalNode IMPORT(int i) {
			return getToken(TeamPlusPlusParser.IMPORT, i);
		}
		public List<TerminalNode> ID() { return getTokens(TeamPlusPlusParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(TeamPlusPlusParser.ID, i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(TeamPlusPlusParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(TeamPlusPlusParser.SEMICOLON, i);
		}
		public List<TerminalNode> AS() { return getTokens(TeamPlusPlusParser.AS); }
		public TerminalNode AS(int i) {
			return getToken(TeamPlusPlusParser.AS, i);
		}
		public ImportsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imports; }
	}

	public final ImportsContext imports() throws RecognitionException {
		ImportsContext _localctx = new ImportsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_imports);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(86);
				match(IMPORT);
				setState(87);
				match(ID);
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AS) {
					{
					setState(88);
					match(AS);
					setState(89);
					match(ID);
					}
				}

				setState(92);
				match(SEMICOLON);
				}
				}
				setState(95); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IMPORT );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassesContext extends ParserRuleContext {
		public List<TerminalNode> CLASS() { return getTokens(TeamPlusPlusParser.CLASS); }
		public TerminalNode CLASS(int i) {
			return getToken(TeamPlusPlusParser.CLASS, i);
		}
		public List<TerminalNode> ID() { return getTokens(TeamPlusPlusParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(TeamPlusPlusParser.ID, i);
		}
		public List<TerminalNode> LEFT_BRACE() { return getTokens(TeamPlusPlusParser.LEFT_BRACE); }
		public TerminalNode LEFT_BRACE(int i) {
			return getToken(TeamPlusPlusParser.LEFT_BRACE, i);
		}
		public List<TerminalNode> RIGHT_BRACE() { return getTokens(TeamPlusPlusParser.RIGHT_BRACE); }
		public TerminalNode RIGHT_BRACE(int i) {
			return getToken(TeamPlusPlusParser.RIGHT_BRACE, i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(TeamPlusPlusParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(TeamPlusPlusParser.SEMICOLON, i);
		}
		public List<TerminalNode> INHERITS() { return getTokens(TeamPlusPlusParser.INHERITS); }
		public TerminalNode INHERITS(int i) {
			return getToken(TeamPlusPlusParser.INHERITS, i);
		}
		public List<C_varsContext> c_vars() {
			return getRuleContexts(C_varsContext.class);
		}
		public C_varsContext c_vars(int i) {
			return getRuleContext(C_varsContext.class,i);
		}
		public List<C_functionsContext> c_functions() {
			return getRuleContexts(C_functionsContext.class);
		}
		public C_functionsContext c_functions(int i) {
			return getRuleContext(C_functionsContext.class,i);
		}
		public ClassesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classes; }
	}

	public final ClassesContext classes() throws RecognitionException {
		ClassesContext _localctx = new ClassesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_classes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(97);
				match(CLASS);
				setState(98);
				match(ID);
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==INHERITS) {
					{
					setState(99);
					match(INHERITS);
					setState(100);
					match(ID);
					}
				}

				setState(103);
				match(LEFT_BRACE);
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ATTRIBUTES) {
					{
					setState(104);
					c_vars();
					}
				}

				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==METHODS) {
					{
					setState(107);
					c_functions();
					}
				}

				setState(110);
				match(RIGHT_BRACE);
				setState(111);
				match(SEMICOLON);
				}
				}
				setState(114); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tpp_varsContext extends ParserRuleContext {
		public TerminalNode VARS() { return getToken(TeamPlusPlusParser.VARS, 0); }
		public List<Tpp_typeContext> tpp_type() {
			return getRuleContexts(Tpp_typeContext.class);
		}
		public Tpp_typeContext tpp_type(int i) {
			return getRuleContext(Tpp_typeContext.class,i);
		}
		public List<InitContext> init() {
			return getRuleContexts(InitContext.class);
		}
		public InitContext init(int i) {
			return getRuleContext(InitContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(TeamPlusPlusParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(TeamPlusPlusParser.SEMICOLON, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public Tpp_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tpp_vars; }
	}

	public final Tpp_varsContext tpp_vars() throws RecognitionException {
		Tpp_varsContext _localctx = new Tpp_varsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tpp_vars);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(VARS);
			setState(128); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(117);
					tpp_type();
					setState(118);
					init();
					setState(123);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(119);
						match(COMMA);
						setState(120);
						init();
						}
						}
						setState(125);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(126);
					match(SEMICOLON);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(130); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class C_varsContext extends ParserRuleContext {
		public TerminalNode ATTRIBUTES() { return getToken(TeamPlusPlusParser.ATTRIBUTES, 0); }
		public List<Tpp_typeContext> tpp_type() {
			return getRuleContexts(Tpp_typeContext.class);
		}
		public Tpp_typeContext tpp_type(int i) {
			return getRuleContext(Tpp_typeContext.class,i);
		}
		public List<InitContext> init() {
			return getRuleContexts(InitContext.class);
		}
		public InitContext init(int i) {
			return getRuleContext(InitContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(TeamPlusPlusParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(TeamPlusPlusParser.SEMICOLON, i);
		}
		public List<LevelContext> level() {
			return getRuleContexts(LevelContext.class);
		}
		public LevelContext level(int i) {
			return getRuleContext(LevelContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public C_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_c_vars; }
	}

	public final C_varsContext c_vars() throws RecognitionException {
		C_varsContext _localctx = new C_varsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_c_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(ATTRIBUTES);
			setState(147); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PUBLIC || _la==PRIVATE) {
					{
					setState(133);
					level();
					}
				}

				setState(136);
				tpp_type();
				setState(137);
				init();
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(138);
					match(COMMA);
					setState(139);
					init();
					}
					}
					setState(144);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(145);
				match(SEMICOLON);
				}
				}
				setState(149); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << CHAR) | (1L << PUBLIC) | (1L << PRIVATE) | (1L << ID))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TeamPlusPlusParser.ID, 0); }
		public TerminalNode LEFT_BRACKET() { return getToken(TeamPlusPlusParser.LEFT_BRACKET, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(TeamPlusPlusParser.RIGHT_BRACKET, 0); }
		public TerminalNode DOT() { return getToken(TeamPlusPlusParser.DOT, 0); }
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(TeamPlusPlusParser.COMMA, 0); }
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(ID);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFT_BRACKET) {
				{
				setState(152);
				match(LEFT_BRACKET);
				setState(153);
				exp();
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(154);
					match(COMMA);
					setState(155);
					exp();
					}
				}

				setState(158);
				match(RIGHT_BRACKET);
				}
			}

			setState(164);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(162);
				match(DOT);
				setState(163);
				var();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TeamPlusPlusParser.ID, 0); }
		public TerminalNode LEFT_BRACKET() { return getToken(TeamPlusPlusParser.LEFT_BRACKET, 0); }
		public List<TerminalNode> CTE_INT() { return getTokens(TeamPlusPlusParser.CTE_INT); }
		public TerminalNode CTE_INT(int i) {
			return getToken(TeamPlusPlusParser.CTE_INT, i);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(TeamPlusPlusParser.RIGHT_BRACKET, 0); }
		public TerminalNode ASSIGN() { return getToken(TeamPlusPlusParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(TeamPlusPlusParser.COMMA, 0); }
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(ID);
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFT_BRACKET) {
				{
				setState(167);
				match(LEFT_BRACKET);
				setState(168);
				match(CTE_INT);
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(169);
					match(COMMA);
					setState(170);
					match(CTE_INT);
					}
				}

				setState(173);
				match(RIGHT_BRACKET);
				}
			}

			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(176);
				match(ASSIGN);
				setState(177);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionsContext extends ParserRuleContext {
		public List<TerminalNode> FUNC() { return getTokens(TeamPlusPlusParser.FUNC); }
		public TerminalNode FUNC(int i) {
			return getToken(TeamPlusPlusParser.FUNC, i);
		}
		public List<Tpp_typeContext> tpp_type() {
			return getRuleContexts(Tpp_typeContext.class);
		}
		public Tpp_typeContext tpp_type(int i) {
			return getRuleContext(Tpp_typeContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(TeamPlusPlusParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(TeamPlusPlusParser.ID, i);
		}
		public List<TerminalNode> LEFT_PARENTHESIS() { return getTokens(TeamPlusPlusParser.LEFT_PARENTHESIS); }
		public TerminalNode LEFT_PARENTHESIS(int i) {
			return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, i);
		}
		public List<TerminalNode> RIGHT_PARENTHESIS() { return getTokens(TeamPlusPlusParser.RIGHT_PARENTHESIS); }
		public TerminalNode RIGHT_PARENTHESIS(int i) {
			return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, i);
		}
		public List<FunblockContext> funblock() {
			return getRuleContexts(FunblockContext.class);
		}
		public FunblockContext funblock(int i) {
			return getRuleContext(FunblockContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public FunctionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functions; }
	}

	public final FunctionsContext functions() throws RecognitionException {
		FunctionsContext _localctx = new FunctionsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(180);
				match(FUNC);
				setState(181);
				tpp_type();
				setState(182);
				match(ID);
				setState(183);
				match(LEFT_PARENTHESIS);
				setState(195);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << CHAR) | (1L << ID))) != 0)) {
					{
					setState(184);
					tpp_type();
					setState(185);
					match(ID);
					setState(192);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(186);
						match(COMMA);
						setState(187);
						tpp_type();
						setState(188);
						match(ID);
						}
						}
						setState(194);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(197);
				match(RIGHT_PARENTHESIS);
				setState(198);
				funblock();
				}
				}
				setState(202); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==FUNC );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class C_functionsContext extends ParserRuleContext {
		public TerminalNode METHODS() { return getToken(TeamPlusPlusParser.METHODS, 0); }
		public List<TerminalNode> FUNC() { return getTokens(TeamPlusPlusParser.FUNC); }
		public TerminalNode FUNC(int i) {
			return getToken(TeamPlusPlusParser.FUNC, i);
		}
		public List<Tpp_typeContext> tpp_type() {
			return getRuleContexts(Tpp_typeContext.class);
		}
		public Tpp_typeContext tpp_type(int i) {
			return getRuleContext(Tpp_typeContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(TeamPlusPlusParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(TeamPlusPlusParser.ID, i);
		}
		public List<TerminalNode> LEFT_PARENTHESIS() { return getTokens(TeamPlusPlusParser.LEFT_PARENTHESIS); }
		public TerminalNode LEFT_PARENTHESIS(int i) {
			return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, i);
		}
		public List<TerminalNode> RIGHT_PARENTHESIS() { return getTokens(TeamPlusPlusParser.RIGHT_PARENTHESIS); }
		public TerminalNode RIGHT_PARENTHESIS(int i) {
			return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, i);
		}
		public List<FunblockContext> funblock() {
			return getRuleContexts(FunblockContext.class);
		}
		public FunblockContext funblock(int i) {
			return getRuleContext(FunblockContext.class,i);
		}
		public List<LevelContext> level() {
			return getRuleContexts(LevelContext.class);
		}
		public LevelContext level(int i) {
			return getRuleContext(LevelContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public C_functionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_c_functions; }
	}

	public final C_functionsContext c_functions() throws RecognitionException {
		C_functionsContext _localctx = new C_functionsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_c_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(METHODS);
			setState(228); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PUBLIC || _la==PRIVATE) {
					{
					setState(205);
					level();
					}
				}

				setState(208);
				match(FUNC);
				setState(209);
				tpp_type();
				setState(210);
				match(ID);
				setState(211);
				match(LEFT_PARENTHESIS);
				setState(223);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << CHAR) | (1L << ID))) != 0)) {
					{
					setState(212);
					tpp_type();
					setState(213);
					match(ID);
					setState(220);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(214);
						match(COMMA);
						setState(215);
						tpp_type();
						setState(216);
						match(ID);
						}
						}
						setState(222);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(225);
				match(RIGHT_PARENTHESIS);
				setState(226);
				funblock();
				}
				}
				setState(230); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << PUBLIC) | (1L << PRIVATE))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public TerminalNode MAIN() { return getToken(TeamPlusPlusParser.MAIN, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public FunblockContext funblock() {
			return getRuleContext(FunblockContext.class,0);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(MAIN);
			setState(233);
			match(LEFT_PARENTHESIS);
			setState(234);
			match(RIGHT_PARENTHESIS);
			setState(235);
			funblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunblockContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACE() { return getToken(TeamPlusPlusParser.LEFT_BRACE, 0); }
		public TerminalNode RIGHT_BRACE() { return getToken(TeamPlusPlusParser.RIGHT_BRACE, 0); }
		public Tpp_varsContext tpp_vars() {
			return getRuleContext(Tpp_varsContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funblock; }
	}

	public final FunblockContext funblock() throws RecognitionException {
		FunblockContext _localctx = new FunblockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_funblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(LEFT_BRACE);
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARS) {
				{
				setState(238);
				tpp_vars();
				}
			}

			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << RETURN) | (1L << READ) | (1L << PRINT) | (1L << WHILE) | (1L << FROM) | (1L << ID))) != 0)) {
				{
				{
				setState(241);
				statement();
				}
				}
				setState(246);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(247);
			match(RIGHT_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tpp_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(TeamPlusPlusParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(TeamPlusPlusParser.FLOAT, 0); }
		public TerminalNode CHAR() { return getToken(TeamPlusPlusParser.CHAR, 0); }
		public TerminalNode ID() { return getToken(TeamPlusPlusParser.ID, 0); }
		public Tpp_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tpp_type; }
	}

	public final Tpp_typeContext tpp_type() throws RecognitionException {
		Tpp_typeContext _localctx = new Tpp_typeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_tpp_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << CHAR) | (1L << ID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LevelContext extends ParserRuleContext {
		public TerminalNode PUBLIC() { return getToken(TeamPlusPlusParser.PUBLIC, 0); }
		public TerminalNode PRIVATE() { return getToken(TeamPlusPlusParser.PRIVATE, 0); }
		public LevelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_level; }
	}

	public final LevelContext level() throws RecognitionException {
		LevelContext _localctx = new LevelContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_level);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			_la = _input.LA(1);
			if ( !(_la==PUBLIC || _la==PRIVATE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(TeamPlusPlusParser.SEMICOLON, 0); }
		public Tpp_returnContext tpp_return() {
			return getRuleContext(Tpp_returnContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public Tpp_printContext tpp_print() {
			return getRuleContext(Tpp_printContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				{
				setState(253);
				assignment();
				}
				break;
			case 2:
				{
				setState(254);
				funcall();
				setState(255);
				match(SEMICOLON);
				}
				break;
			case 3:
				{
				setState(257);
				tpp_return();
				}
				break;
			case 4:
				{
				setState(258);
				read();
				}
				break;
			case 5:
				{
				setState(259);
				tpp_print();
				}
				break;
			case 6:
				{
				setState(260);
				condition();
				}
				break;
			case 7:
				{
				setState(261);
				loop();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(TeamPlusPlusParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(TeamPlusPlusParser.SEMICOLON, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			var();
			setState(265);
			match(ASSIGN);
			setState(266);
			expression();
			setState(267);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TeamPlusPlusParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode DOT() { return getToken(TeamPlusPlusParser.DOT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public FuncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcall; }
	}

	public final FuncallContext funcall() throws RecognitionException {
		FuncallContext _localctx = new FuncallContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_funcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				{
				setState(269);
				var();
				setState(270);
				match(DOT);
				}
				break;
			}
			setState(274);
			match(ID);
			setState(275);
			match(LEFT_PARENTHESIS);
			setState(284);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NOT) | (1L << LEFT_PARENTHESIS) | (1L << PLUS) | (1L << MINUS) | (1L << CTE_INT) | (1L << CTE_FLOAT) | (1L << CTE_CHAR) | (1L << ID))) != 0)) {
				{
				setState(276);
				expression();
				setState(281);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(277);
					match(COMMA);
					setState(278);
					expression();
					}
					}
					setState(283);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(286);
			match(RIGHT_PARENTHESIS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tpp_returnContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(TeamPlusPlusParser.RETURN, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(TeamPlusPlusParser.SEMICOLON, 0); }
		public Tpp_returnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tpp_return; }
	}

	public final Tpp_returnContext tpp_return() throws RecognitionException {
		Tpp_returnContext _localctx = new Tpp_returnContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_tpp_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(RETURN);
			setState(289);
			match(LEFT_PARENTHESIS);
			setState(290);
			exp();
			setState(291);
			match(RIGHT_PARENTHESIS);
			setState(292);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReadContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(TeamPlusPlusParser.READ, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(TeamPlusPlusParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_read);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			match(READ);
			setState(295);
			match(LEFT_PARENTHESIS);
			setState(296);
			var();
			setState(301);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(297);
				match(COMMA);
				setState(298);
				var();
				}
				}
				setState(303);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(304);
			match(RIGHT_PARENTHESIS);
			setState(305);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tpp_printContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(TeamPlusPlusParser.PRINT, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode SEMICOLON() { return getToken(TeamPlusPlusParser.SEMICOLON, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> CTE_STRING() { return getTokens(TeamPlusPlusParser.CTE_STRING); }
		public TerminalNode CTE_STRING(int i) {
			return getToken(TeamPlusPlusParser.CTE_STRING, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TeamPlusPlusParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TeamPlusPlusParser.COMMA, i);
		}
		public Tpp_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tpp_print; }
	}

	public final Tpp_printContext tpp_print() throws RecognitionException {
		Tpp_printContext _localctx = new Tpp_printContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_tpp_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(PRINT);
			setState(308);
			match(LEFT_PARENTHESIS);
			setState(311);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
			case LEFT_PARENTHESIS:
			case PLUS:
			case MINUS:
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_CHAR:
			case ID:
				{
				setState(309);
				expression();
				}
				break;
			case CTE_STRING:
				{
				setState(310);
				match(CTE_STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(320);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(313);
				match(COMMA);
				setState(316);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NOT:
				case LEFT_PARENTHESIS:
				case PLUS:
				case MINUS:
				case CTE_INT:
				case CTE_FLOAT:
				case CTE_CHAR:
				case ID:
					{
					setState(314);
					expression();
					}
					break;
				case CTE_STRING:
					{
					setState(315);
					match(CTE_STRING);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(322);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(323);
			match(RIGHT_PARENTHESIS);
			setState(324);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACE() { return getToken(TeamPlusPlusParser.LEFT_BRACE, 0); }
		public TerminalNode RIGHT_BRACE() { return getToken(TeamPlusPlusParser.RIGHT_BRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			match(LEFT_BRACE);
			setState(330);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << RETURN) | (1L << READ) | (1L << PRINT) | (1L << WHILE) | (1L << FROM) | (1L << ID))) != 0)) {
				{
				{
				setState(327);
				statement();
				}
				}
				setState(332);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(333);
			match(RIGHT_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(TeamPlusPlusParser.IF, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public TerminalNode THEN() { return getToken(TeamPlusPlusParser.THEN, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(TeamPlusPlusParser.ELSE, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			match(IF);
			setState(336);
			match(LEFT_PARENTHESIS);
			setState(337);
			expression();
			setState(338);
			match(RIGHT_PARENTHESIS);
			setState(339);
			match(THEN);
			setState(340);
			block();
			setState(343);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(341);
				match(ELSE);
				setState(342);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LoopContext extends ParserRuleContext {
		public WloopContext wloop() {
			return getRuleContext(WloopContext.class,0);
		}
		public FloopContext floop() {
			return getRuleContext(FloopContext.class,0);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(347);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WHILE:
				{
				setState(345);
				wloop();
				}
				break;
			case FROM:
				{
				setState(346);
				floop();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WloopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(TeamPlusPlusParser.WHILE, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wloop; }
	}

	public final WloopContext wloop() throws RecognitionException {
		WloopContext _localctx = new WloopContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_wloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			match(WHILE);
			setState(350);
			match(LEFT_PARENTHESIS);
			setState(351);
			expression();
			setState(352);
			match(RIGHT_PARENTHESIS);
			setState(353);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FloopContext extends ParserRuleContext {
		public TerminalNode FROM() { return getToken(TeamPlusPlusParser.FROM, 0); }
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(TeamPlusPlusParser.ASSIGN, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode TO() { return getToken(TeamPlusPlusParser.TO, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_floop; }
	}

	public final FloopContext floop() throws RecognitionException {
		FloopContext _localctx = new FloopContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_floop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			match(FROM);
			setState(356);
			var();
			setState(357);
			match(ASSIGN);
			setState(358);
			exp();
			setState(359);
			match(TO);
			setState(360);
			exp();
			setState(361);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressContext express() {
			return getRuleContext(ExpressContext.class,0);
		}
		public Expression_AContext expression_A() {
			return getRuleContext(Expression_AContext.class,0);
		}
		public TerminalNode NOT() { return getToken(TeamPlusPlusParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_expression);
		try {
			setState(370);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_PARENTHESIS:
			case PLUS:
			case MINUS:
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_CHAR:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(363);
				express();
				setState(364);
				expression_A();
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 2);
				{
				setState(366);
				match(NOT);
				setState(367);
				expression();
				setState(368);
				expression_A();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_AContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expression_AContext expression_A() {
			return getRuleContext(Expression_AContext.class,0);
		}
		public TerminalNode AND() { return getToken(TeamPlusPlusParser.AND, 0); }
		public TerminalNode OR() { return getToken(TeamPlusPlusParser.OR, 0); }
		public Expression_AContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_A; }
	}

	public final Expression_AContext expression_A() throws RecognitionException {
		Expression_AContext _localctx = new Expression_AContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_expression_A);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				{
				setState(372);
				_la = _input.LA(1);
				if ( !(_la==AND || _la==OR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(373);
				expression();
				setState(374);
				expression_A();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public RelopContext relop() {
			return getRuleContext(RelopContext.class,0);
		}
		public ExpressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_express; }
	}

	public final ExpressContext express() throws RecognitionException {
		ExpressContext _localctx = new ExpressContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_express);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			exp();
			setState(382);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUALS) | (1L << GREATER_THAN) | (1L << LESS_THAN) | (1L << GREATER_EQUALS) | (1L << LESS_EQUALS) | (1L << DIFFERENT))) != 0)) {
				{
				setState(379);
				relop();
				setState(380);
				exp();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<SumopContext> sumop() {
			return getRuleContexts(SumopContext.class);
		}
		public SumopContext sumop(int i) {
			return getRuleContext(SumopContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			term();
			setState(390);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(385);
				sumop();
				setState(386);
				term();
				}
				}
				setState(392);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<MulopContext> mulop() {
			return getRuleContexts(MulopContext.class);
		}
		public MulopContext mulop(int i) {
			return getRuleContext(MulopContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(393);
			factor();
			setState(399);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(394);
				mulop();
				setState(395);
				factor();
				}
				}
				setState(401);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LEFT_PARENTHESIS() { return getToken(TeamPlusPlusParser.LEFT_PARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(TeamPlusPlusParser.RIGHT_PARENTHESIS, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public SumopContext sumop() {
			return getRuleContext(SumopContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_PARENTHESIS:
				{
				setState(402);
				match(LEFT_PARENTHESIS);
				setState(403);
				expression();
				setState(404);
				match(RIGHT_PARENTHESIS);
				}
				break;
			case PLUS:
			case MINUS:
			case CTE_INT:
			case CTE_FLOAT:
			case CTE_CHAR:
			case ID:
				{
				setState(407);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(406);
					sumop();
					}
				}

				setState(409);
				value();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RelopContext extends ParserRuleContext {
		public TerminalNode EQUALS() { return getToken(TeamPlusPlusParser.EQUALS, 0); }
		public TerminalNode GREATER_THAN() { return getToken(TeamPlusPlusParser.GREATER_THAN, 0); }
		public TerminalNode LESS_THAN() { return getToken(TeamPlusPlusParser.LESS_THAN, 0); }
		public TerminalNode GREATER_EQUALS() { return getToken(TeamPlusPlusParser.GREATER_EQUALS, 0); }
		public TerminalNode LESS_EQUALS() { return getToken(TeamPlusPlusParser.LESS_EQUALS, 0); }
		public TerminalNode DIFFERENT() { return getToken(TeamPlusPlusParser.DIFFERENT, 0); }
		public RelopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relop; }
	}

	public final RelopContext relop() throws RecognitionException {
		RelopContext _localctx = new RelopContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_relop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(412);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUALS) | (1L << GREATER_THAN) | (1L << LESS_THAN) | (1L << GREATER_EQUALS) | (1L << LESS_EQUALS) | (1L << DIFFERENT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SumopContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(TeamPlusPlusParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(TeamPlusPlusParser.MINUS, 0); }
		public SumopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sumop; }
	}

	public final SumopContext sumop() throws RecognitionException {
		SumopContext _localctx = new SumopContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_sumop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MulopContext extends ParserRuleContext {
		public TerminalNode MULT() { return getToken(TeamPlusPlusParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(TeamPlusPlusParser.DIV, 0); }
		public MulopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulop; }
	}

	public final MulopContext mulop() throws RecognitionException {
		MulopContext _localctx = new MulopContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_mulop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(416);
			_la = _input.LA(1);
			if ( !(_la==MULT || _la==DIV) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode CTE_INT() { return getToken(TeamPlusPlusParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(TeamPlusPlusParser.CTE_FLOAT, 0); }
		public TerminalNode CTE_CHAR() { return getToken(TeamPlusPlusParser.CTE_CHAR, 0); }
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(423);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				{
				setState(418);
				var();
				}
				break;
			case 2:
				{
				setState(419);
				match(CTE_INT);
				}
				break;
			case 3:
				{
				setState(420);
				match(CTE_FLOAT);
				}
				break;
			case 4:
				{
				setState(421);
				match(CTE_CHAR);
				}
				break;
			case 5:
				{
				setState(422);
				funcall();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\39\u01ac\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\3\2\3\2\3\2\3\2\5\2K\n\2\3\2\5\2N\n\2\3\2\5\2Q\n\2\3"+
		"\2\5\2T\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3]\n\3\3\3\6\3`\n\3\r\3\16\3"+
		"a\3\4\3\4\3\4\3\4\5\4h\n\4\3\4\3\4\5\4l\n\4\3\4\5\4o\n\4\3\4\3\4\6\4s"+
		"\n\4\r\4\16\4t\3\5\3\5\3\5\3\5\3\5\7\5|\n\5\f\5\16\5\177\13\5\3\5\3\5"+
		"\6\5\u0083\n\5\r\5\16\5\u0084\3\6\3\6\5\6\u0089\n\6\3\6\3\6\3\6\3\6\7"+
		"\6\u008f\n\6\f\6\16\6\u0092\13\6\3\6\3\6\6\6\u0096\n\6\r\6\16\6\u0097"+
		"\3\7\3\7\3\7\3\7\3\7\5\7\u009f\n\7\3\7\3\7\5\7\u00a3\n\7\3\7\3\7\5\7\u00a7"+
		"\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00ae\n\b\3\b\5\b\u00b1\n\b\3\b\3\b\5\b\u00b5"+
		"\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00c1\n\t\f\t\16\t\u00c4"+
		"\13\t\5\t\u00c6\n\t\3\t\3\t\3\t\6\t\u00cb\n\t\r\t\16\t\u00cc\3\n\3\n\5"+
		"\n\u00d1\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00dd\n\n\f\n"+
		"\16\n\u00e0\13\n\5\n\u00e2\n\n\3\n\3\n\3\n\6\n\u00e7\n\n\r\n\16\n\u00e8"+
		"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00f2\n\f\3\f\7\f\u00f5\n\f\f\f"+
		"\16\f\u00f8\13\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\5\17\u0109\n\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21"+
		"\3\21\5\21\u0113\n\21\3\21\3\21\3\21\3\21\3\21\7\21\u011a\n\21\f\21\16"+
		"\21\u011d\13\21\5\21\u011f\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\23\3\23\3\23\3\23\3\23\7\23\u012e\n\23\f\23\16\23\u0131\13\23\3\23"+
		"\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u013a\n\24\3\24\3\24\3\24\5\24\u013f"+
		"\n\24\7\24\u0141\n\24\f\24\16\24\u0144\13\24\3\24\3\24\3\24\3\25\3\25"+
		"\7\25\u014b\n\25\f\25\16\25\u014e\13\25\3\25\3\25\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\5\26\u015a\n\26\3\27\3\27\5\27\u015e\n\27\3\30\3"+
		"\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3"+
		"\32\3\32\3\32\3\32\3\32\3\32\5\32\u0175\n\32\3\33\3\33\3\33\3\33\5\33"+
		"\u017b\n\33\3\34\3\34\3\34\3\34\5\34\u0181\n\34\3\35\3\35\3\35\3\35\7"+
		"\35\u0187\n\35\f\35\16\35\u018a\13\35\3\36\3\36\3\36\3\36\7\36\u0190\n"+
		"\36\f\36\16\36\u0193\13\36\3\37\3\37\3\37\3\37\3\37\5\37\u019a\n\37\3"+
		"\37\5\37\u019d\n\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3#\3#\5#\u01aa\n#\3#"+
		"\2\2$\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>"+
		"@BD\2\b\4\2\4\6\67\67\3\2\31\32\3\2\33\34\3\2-\62\3\2)*\3\2+,\2\u01c2"+
		"\2F\3\2\2\2\4_\3\2\2\2\6r\3\2\2\2\bv\3\2\2\2\n\u0086\3\2\2\2\f\u0099\3"+
		"\2\2\2\16\u00a8\3\2\2\2\20\u00ca\3\2\2\2\22\u00ce\3\2\2\2\24\u00ea\3\2"+
		"\2\2\26\u00ef\3\2\2\2\30\u00fb\3\2\2\2\32\u00fd\3\2\2\2\34\u0108\3\2\2"+
		"\2\36\u010a\3\2\2\2 \u0112\3\2\2\2\"\u0122\3\2\2\2$\u0128\3\2\2\2&\u0135"+
		"\3\2\2\2(\u0148\3\2\2\2*\u0151\3\2\2\2,\u015d\3\2\2\2.\u015f\3\2\2\2\60"+
		"\u0165\3\2\2\2\62\u0174\3\2\2\2\64\u017a\3\2\2\2\66\u017c\3\2\2\28\u0182"+
		"\3\2\2\2:\u018b\3\2\2\2<\u019c\3\2\2\2>\u019e\3\2\2\2@\u01a0\3\2\2\2B"+
		"\u01a2\3\2\2\2D\u01a9\3\2\2\2FG\7\3\2\2GH\7\67\2\2HJ\7(\2\2IK\5\4\3\2"+
		"JI\3\2\2\2JK\3\2\2\2KM\3\2\2\2LN\5\6\4\2ML\3\2\2\2MN\3\2\2\2NP\3\2\2\2"+
		"OQ\5\b\5\2PO\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RT\5\20\t\2SR\3\2\2\2ST\3\2\2"+
		"\2TU\3\2\2\2UV\5\24\13\2VW\7\2\2\3W\3\3\2\2\2XY\7\27\2\2Y\\\7\67\2\2Z"+
		"[\7\30\2\2[]\7\67\2\2\\Z\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`\7(\2\2_X\3\2\2"+
		"\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\5\3\2\2\2cd\7\b\2\2dg\7\67\2\2ef\7\t"+
		"\2\2fh\7\67\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ik\7\"\2\2jl\5\n\6\2kj\3"+
		"\2\2\2kl\3\2\2\2ln\3\2\2\2mo\5\22\n\2nm\3\2\2\2no\3\2\2\2op\3\2\2\2pq"+
		"\7#\2\2qs\7(\2\2rc\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\7\3\2\2\2v\u0082"+
		"\7\7\2\2wx\5\30\r\2x}\5\16\b\2yz\7\37\2\2z|\5\16\b\2{y\3\2\2\2|\177\3"+
		"\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081\7("+
		"\2\2\u0081\u0083\3\2\2\2\u0082w\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082"+
		"\3\2\2\2\u0084\u0085\3\2\2\2\u0085\t\3\2\2\2\u0086\u0095\7\25\2\2\u0087"+
		"\u0089\5\32\16\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3"+
		"\2\2\2\u008a\u008b\5\30\r\2\u008b\u0090\5\16\b\2\u008c\u008d\7\37\2\2"+
		"\u008d\u008f\5\16\b\2\u008e\u008c\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e"+
		"\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u0090\3\2\2\2\u0093"+
		"\u0094\7(\2\2\u0094\u0096\3\2\2\2\u0095\u0088\3\2\2\2\u0096\u0097\3\2"+
		"\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\13\3\2\2\2\u0099\u00a2"+
		"\7\67\2\2\u009a\u009b\7&\2\2\u009b\u009e\58\35\2\u009c\u009d\7\37\2\2"+
		"\u009d\u009f\58\35\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0"+
		"\3\2\2\2\u00a0\u00a1\7\'\2\2\u00a1\u00a3\3\2\2\2\u00a2\u009a\3\2\2\2\u00a2"+
		"\u00a3\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a5\7 \2\2\u00a5\u00a7\5\f"+
		"\7\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\r\3\2\2\2\u00a8\u00b0"+
		"\7\67\2\2\u00a9\u00aa\7&\2\2\u00aa\u00ad\7\63\2\2\u00ab\u00ac\7\37\2\2"+
		"\u00ac\u00ae\7\63\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af"+
		"\3\2\2\2\u00af\u00b1\7\'\2\2\u00b0\u00a9\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1"+
		"\u00b4\3\2\2\2\u00b2\u00b3\7!\2\2\u00b3\u00b5\5\62\32\2\u00b4\u00b2\3"+
		"\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\17\3\2\2\2\u00b6\u00b7\7\16\2\2\u00b7"+
		"\u00b8\5\30\r\2\u00b8\u00b9\7\67\2\2\u00b9\u00c5\7$\2\2\u00ba\u00bb\5"+
		"\30\r\2\u00bb\u00c2\7\67\2\2\u00bc\u00bd\7\37\2\2\u00bd\u00be\5\30\r\2"+
		"\u00be\u00bf\7\67\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c1\u00c4"+
		"\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4"+
		"\u00c2\3\2\2\2\u00c5\u00ba\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2"+
		"\2\2\u00c7\u00c8\7%\2\2\u00c8\u00c9\5\26\f\2\u00c9\u00cb\3\2\2\2\u00ca"+
		"\u00b6\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2"+
		"\2\2\u00cd\21\3\2\2\2\u00ce\u00e6\7\26\2\2\u00cf\u00d1\5\32\16\2\u00d0"+
		"\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7\16"+
		"\2\2\u00d3\u00d4\5\30\r\2\u00d4\u00d5\7\67\2\2\u00d5\u00e1\7$\2\2\u00d6"+
		"\u00d7\5\30\r\2\u00d7\u00de\7\67\2\2\u00d8\u00d9\7\37\2\2\u00d9\u00da"+
		"\5\30\r\2\u00da\u00db\7\67\2\2\u00db\u00dd\3\2\2\2\u00dc\u00d8\3\2\2\2"+
		"\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e2"+
		"\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00d6\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2"+
		"\u00e3\3\2\2\2\u00e3\u00e4\7%\2\2\u00e4\u00e5\5\26\f\2\u00e5\u00e7\3\2"+
		"\2\2\u00e6\u00d0\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8"+
		"\u00e9\3\2\2\2\u00e9\23\3\2\2\2\u00ea\u00eb\7\n\2\2\u00eb\u00ec\7$\2\2"+
		"\u00ec\u00ed\7%\2\2\u00ed\u00ee\5\26\f\2\u00ee\25\3\2\2\2\u00ef\u00f1"+
		"\7\"\2\2\u00f0\u00f2\5\b\5\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2"+
		"\u00f6\3\2\2\2\u00f3\u00f5\5\34\17\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3"+
		"\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8"+
		"\u00f6\3\2\2\2\u00f9\u00fa\7#\2\2\u00fa\27\3\2\2\2\u00fb\u00fc\t\2\2\2"+
		"\u00fc\31\3\2\2\2\u00fd\u00fe\t\3\2\2\u00fe\33\3\2\2\2\u00ff\u0109\5\36"+
		"\20\2\u0100\u0101\5 \21\2\u0101\u0102\7(\2\2\u0102\u0109\3\2\2\2\u0103"+
		"\u0109\5\"\22\2\u0104\u0109\5$\23\2\u0105\u0109\5&\24\2\u0106\u0109\5"+
		"*\26\2\u0107\u0109\5,\27\2\u0108\u00ff\3\2\2\2\u0108\u0100\3\2\2\2\u0108"+
		"\u0103\3\2\2\2\u0108\u0104\3\2\2\2\u0108\u0105\3\2\2\2\u0108\u0106\3\2"+
		"\2\2\u0108\u0107\3\2\2\2\u0109\35\3\2\2\2\u010a\u010b\5\f\7\2\u010b\u010c"+
		"\7!\2\2\u010c\u010d\5\62\32\2\u010d\u010e\7(\2\2\u010e\37\3\2\2\2\u010f"+
		"\u0110\5\f\7\2\u0110\u0111\7 \2\2\u0111\u0113\3\2\2\2\u0112\u010f\3\2"+
		"\2\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\7\67\2\2\u0115"+
		"\u011e\7$\2\2\u0116\u011b\5\62\32\2\u0117\u0118\7\37\2\2\u0118\u011a\5"+
		"\62\32\2\u0119\u0117\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b"+
		"\u011c\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0116\3\2"+
		"\2\2\u011e\u011f\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\7%\2\2\u0121"+
		"!\3\2\2\2\u0122\u0123\7\17\2\2\u0123\u0124\7$\2\2\u0124\u0125\58\35\2"+
		"\u0125\u0126\7%\2\2\u0126\u0127\7(\2\2\u0127#\3\2\2\2\u0128\u0129\7\20"+
		"\2\2\u0129\u012a\7$\2\2\u012a\u012f\5\f\7\2\u012b\u012c\7\37\2\2\u012c"+
		"\u012e\5\f\7\2\u012d\u012b\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2"+
		"\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2\2\u0132"+
		"\u0133\7%\2\2\u0133\u0134\7(\2\2\u0134%\3\2\2\2\u0135\u0136\7\21\2\2\u0136"+
		"\u0139\7$\2\2\u0137\u013a\5\62\32\2\u0138\u013a\7\66\2\2\u0139\u0137\3"+
		"\2\2\2\u0139\u0138\3\2\2\2\u013a\u0142\3\2\2\2\u013b\u013e\7\37\2\2\u013c"+
		"\u013f\5\62\32\2\u013d\u013f\7\66\2\2\u013e\u013c\3\2\2\2\u013e\u013d"+
		"\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013b\3\2\2\2\u0141\u0144\3\2\2\2\u0142"+
		"\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0142\3\2"+
		"\2\2\u0145\u0146\7%\2\2\u0146\u0147\7(\2\2\u0147\'\3\2\2\2\u0148\u014c"+
		"\7\"\2\2\u0149\u014b\5\34\17\2\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2\2"+
		"\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c"+
		"\3\2\2\2\u014f\u0150\7#\2\2\u0150)\3\2\2\2\u0151\u0152\7\13\2\2\u0152"+
		"\u0153\7$\2\2\u0153\u0154\5\62\32\2\u0154\u0155\7%\2\2\u0155\u0156\7\r"+
		"\2\2\u0156\u0159\5(\25\2\u0157\u0158\7\f\2\2\u0158\u015a\5(\25\2\u0159"+
		"\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a+\3\2\2\2\u015b\u015e\5.\30\2"+
		"\u015c\u015e\5\60\31\2\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2\u015e-"+
		"\3\2\2\2\u015f\u0160\7\22\2\2\u0160\u0161\7$\2\2\u0161\u0162\5\62\32\2"+
		"\u0162\u0163\7%\2\2\u0163\u0164\5(\25\2\u0164/\3\2\2\2\u0165\u0166\7\23"+
		"\2\2\u0166\u0167\5\f\7\2\u0167\u0168\7!\2\2\u0168\u0169\58\35\2\u0169"+
		"\u016a\7\24\2\2\u016a\u016b\58\35\2\u016b\u016c\5(\25\2\u016c\61\3\2\2"+
		"\2\u016d\u016e\5\66\34\2\u016e\u016f\5\64\33\2\u016f\u0175\3\2\2\2\u0170"+
		"\u0171\7\35\2\2\u0171\u0172\5\62\32\2\u0172\u0173\5\64\33\2\u0173\u0175"+
		"\3\2\2\2\u0174\u016d\3\2\2\2\u0174\u0170\3\2\2\2\u0175\63\3\2\2\2\u0176"+
		"\u0177\t\4\2\2\u0177\u0178\5\62\32\2\u0178\u0179\5\64\33\2\u0179\u017b"+
		"\3\2\2\2\u017a\u0176\3\2\2\2\u017a\u017b\3\2\2\2\u017b\65\3\2\2\2\u017c"+
		"\u0180\58\35\2\u017d\u017e\5> \2\u017e\u017f\58\35\2\u017f\u0181\3\2\2"+
		"\2\u0180\u017d\3\2\2\2\u0180\u0181\3\2\2\2\u0181\67\3\2\2\2\u0182\u0188"+
		"\5:\36\2\u0183\u0184\5@!\2\u0184\u0185\5:\36\2\u0185\u0187\3\2\2\2\u0186"+
		"\u0183\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2"+
		"\2\2\u01899\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u0191\5<\37\2\u018c\u018d"+
		"\5B\"\2\u018d\u018e\5<\37\2\u018e\u0190\3\2\2\2\u018f\u018c\3\2\2\2\u0190"+
		"\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192;\3\2\2\2"+
		"\u0193\u0191\3\2\2\2\u0194\u0195\7$\2\2\u0195\u0196\5\62\32\2\u0196\u0197"+
		"\7%\2\2\u0197\u019d\3\2\2\2\u0198\u019a\5@!\2\u0199\u0198\3\2\2\2\u0199"+
		"\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d\5D#\2\u019c\u0194\3\2\2"+
		"\2\u019c\u0199\3\2\2\2\u019d=\3\2\2\2\u019e\u019f\t\5\2\2\u019f?\3\2\2"+
		"\2\u01a0\u01a1\t\6\2\2\u01a1A\3\2\2\2\u01a2\u01a3\t\7\2\2\u01a3C\3\2\2"+
		"\2\u01a4\u01aa\5\f\7\2\u01a5\u01aa\7\63\2\2\u01a6\u01aa\7\64\2\2\u01a7"+
		"\u01aa\7\65\2\2\u01a8\u01aa\5 \21\2\u01a9\u01a4\3\2\2\2\u01a9\u01a5\3"+
		"\2\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa"+
		"E\3\2\2\2\63JMPS\\agknt}\u0084\u0088\u0090\u0097\u009e\u00a2\u00a6\u00ad"+
		"\u00b0\u00b4\u00c2\u00c5\u00cc\u00d0\u00de\u00e1\u00e8\u00f1\u00f6\u0108"+
		"\u0112\u011b\u011e\u012f\u0139\u013e\u0142\u014c\u0159\u015d\u0174\u017a"+
		"\u0180\u0188\u0191\u0199\u019c\u01a9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}