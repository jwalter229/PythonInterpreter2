class ArithmeticOperator:
    ADD_OP = 1
    MUL_OP = 2
    SUB_OP = 3
    DIV_OP = 4
    MOD_OP = 5
    REV_DIV_OP = 6
    EXP_OP = 7


class RelativeOperator:
    LE_OP = 1
    LT_OP = 2
    GE_OP = 3
    GT_OP = 4
    EQ_OP = 5
    NE_OP = 6


class TokenType:
    ID_TOK = 1
    ADD_TOK = 2
    MUL_TOK = 3
    ASSIGN_TOK = 4
    CONST_TOK = 5
    EOS_TOK = 6
    SUB_TOK = 7
    DIV_TOK = 8
    REV_DIV_TOK = 9
    EXP_TOK = 10
    MOD_TOK = 11
    LE_TOK = 12
    LT_TOK = 13
    GE_TOK = 14
    GT_TOK = 15
    EQ_TOK = 16
    NE_TOK = 17
    LEFT_PAREN_TOK = 18
    RIGHT_PAREN_TOK = 19
    IF_TOK = 20
    ELSE_TOK = 21
    FOR_TOK = 22
    WHILE_TOK = 23
    FUNCTION_TOK = 24
    THEN_TOK = 25
    END_TOK = 26
    PRINT_TOK = 27
    REPEAT_TOK = 28
    UNTIL_TOK = 29
    COL_TOK = 30


class Token:

    #    private int rowNumber;
    #    private int columnNumber;
    #    private String lexeme;
    #    private TokenType tokType;

    def __init__(self, rowNumber, columnNumber, lexeme, tokType):
        if (rowNumber <= 0):
            raise Exception("IllegalArgumentException: invalid row number argument")
        if (columnNumber <= 0):
            raise Exception("IllegalArgumentException: invalid column number argument")
        if (lexeme == None or len(lexeme) == 0):
            raise Exception("IllegalArgumentException: invalid lexeme argument")
        if (tokType == None):
            raise Exception("IllegalArgumentException: invalid TokenType argument")
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.lexeme = lexeme
        self.tokType = tokType

    def getRowNumber(self):
        return self.rowNumber

    def getColumnNumber(self):
        return self.columnNumber

    def getLexeme(self):
        return self.lexeme

    def getTokType(self):
        return self.tokType


class Memory:
    mem = [0] * 52

    def fetch(ch):
        return Memory.mem[Memory.getIndex(ch)]

    def store(ch, value):
        Memory.mem[Memory.getIndex(ch)] = value

    def getIndex(ch):

        if (not ch.isalpha()) or len(ch) > 1:
            raise Exception("IllegalArgumentException: " + ch + " is not a valid identifier")
        if (ord(ch) - ord('A') < 26):
            return ord(ch) - ord('A')
        else:
            return ord(ch) - ord('a') + 26

    def displayMemory():
        for i, v in enumerate(Memory.mem):
            if i < 26:
                print('{}: {}'.format(chr(ord('A') + i), str(v)))
            else:
                print('{}: {}'.format(chr(ord('a') + i - 26), str(v)))


class Statement:
    def __init__(self):
        return

    def execute(self):
        return


class WhileStatement(Statement):
    #    private BooleanExpression expr;
    #    private Block blk;
    def __init__(self, expr, blk):
        if (expr == None):
            raise Exception("IllegalArgumentException: None boolean expression argument")
        if (blk == None):
            raise Exception("IllegalArgumentException: None block argument")
        self.expr = expr
        self.blk = blk

    def execute(self):
        while (self.expr.evaluate()):
            self.blk.execute()


class PrintStatement(Statement):

    #    private ArithmeticExpression expr;

    def __init__(self, expr):
        if (expr == None):
            raise Exception("IllegalArgumentException: None arithmetic expression argument")
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())


class ForStatement(Statement):

    #    private Id var;
    #    private Iter it;
    #    private Block blk;

    def __init__(self, var, it, blk):
        if (var == None):
            raise Exception("IllegalArgumentException: None Id argument")
        if (it == None):
            raise Exception("IllegalArgumentException: None iterator argument")
        if (blk == None):
            raise Exception("IllegalArgumentException: None block argument")
        self.var = var;
        self.it = it;
        self.blk = blk;
        return

    def execute(self):
        if (self.it.evaluate()[0] < self.it.evaluate()[1]):
            Memory.store(self.var.getChar(), self.it.evaluate()[0])
            while (Memory.fetch(self.var.getChar()) <= self.it.evaluate()[1]):
                self.blk.execute()
                i = Memory.fetch(self.var.getChar());
                i += 1
                Memory.store(self.var.getChar(), i);
        else:
            Memory.store(self.var.getChar(), self.it.evaluate()[0])
            while (Memory.fetch(self.var.getChar()) >= self.it.evaluate()[1]):
                self.blk.execute();
                i = Memory.fetch(self.var.getChar());
                i -= 1
                Memory.store(self.var.getChar(), i);


class IfStatement(Statement):

    #    private BooleanExpression expr;
    #    private Block blk1, blk2;

    def __init__(self, expr, blk1, blk2):
        if (expr == None):
            raise Exception("IllegalArgumentException: None boolean expression argument")
        if (blk1 == None or blk2 == None):
            raise Exception("IllegalArgumentException: None block argument")
        self.expr = expr;
        self.blk1 = blk1;
        self.blk2 = blk2;

    def execute(self):
        if (self.expr.evaluate()):
            self.blk1.execute();
        else:
            self.blk2.execute();


class ArithmeticExpression:
    def __init__(self):
        return

    def execute(self):
        return


class Id(ArithmeticExpression):
    #    private char ch;
    def __init__(self, ch):
        if (not ch.isalpha()) or len(ch) > 1:
            raise Exception("IllegalArgumentException: character is not a valid identifier")
        self.ch = ch

    def evaluate(self):
        return Memory.fetch(self.ch)

    def getChar(self):
        return self.ch


class BinaryExpression(ArithmeticExpression):
    #    private ArithmeticExpression expr1, expr2;
    #    private ArithmeticOperator op;
    #    /**
    #     * @param expr1 - cannot be None
    #     * @param expr2 - cannot be None
    #     * @throws IllegalArgumentException if either argument is None
    #     */
    def __init__(self, op, expr1, expr2):
        if (op == None):
            raise Exception("IllegalArgumentException: " + "None arithmetic operator argument");
        if (expr1 == None or expr2 == None):
            raise Exception("IllegalArgumentException: " + "None expression argument");
        self.expr1 = expr1;
        self.expr2 = expr2;
        self.op = op;

    def evaluate(self):
        value = 0
        if self.op == ArithmeticOperator.ADD_OP:
            value = self.expr1.evaluate() + self.expr2.evaluate();
        elif self.op == ArithmeticOperator.SUB_OP:
            value = self.expr1.evaluate() - self.expr2.evaluate();
        elif self.op == ArithmeticOperator.MUL_OP:
            value = self.expr1.evaluate() * self.expr2.evaluate();
        elif self.op == ArithmeticOperator.DIV_OP:
            value = self.expr1.evaluate() / self.expr2.evaluate();
        elif self.op == ArithmeticOperator.MOD_OP:
            value = self.expr1.evaluate() % self.expr2.evaluate();
        elif self.op == ArithmeticOperator.EXP_OP:
            value = self.expr1.evaluate() ** self.expr2.evaluate();
        elif self.op == ArithmeticOperator.REV_DIV_OP:
            value = self.expr2.evaluate() / self.expr1.evaluate();
        return value;


class BooleanExpression(ArithmeticExpression):

    def __init__(self, op, expr1, expr2):
        if (op == None):
            raise Exception("IllegalArgumentException: " + "None relative operator argument");
        if (expr1 == None or expr2 == None):
            raise Exception("IllegalArgumentException: " + "None expression argument");
        self.expr1 = expr1;
        self.expr2 = expr2;
        self.op = op;

    def evaluate(self):
        value = False
        if (self.op == RelativeOperator.LE_OP):
            value = self.expr1.evaluate() <= self.expr2.evaluate();
        elif (self.op == RelativeOperator.LT_OP):
            value = self.expr1.evaluate() < self.expr2.evaluate();
        elif (self.op == RelativeOperator.GE_OP):
            value = self.expr1.evaluate() >= self.expr2.evaluate();
        elif (self.op == RelativeOperator.GT_OP):
            value = self.expr1.evaluate() > self.expr2.evaluate();
        elif (self.op == RelativeOperator.EQ_OP):
            value = self.expr1.evaluate() == self.expr2.evaluate();
        elif (self.op == RelativeOperator.NE_OP):
            value = self.expr1.evaluate() != self.expr2.evaluate();

        return value


class Constant(ArithmeticExpression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class AssignmentStatement(Statement):

    #    /**
    #     * @param var - cannot be None
    #     * @param expr - cannot be None
    #     * @throws IllegalArgumentException if either argument is None
    #     */
    def __init__(self, var, expr):
        if not expr:
            error
        if not var:
            error
        self.expr = expr
        self.var = var
        return

    def execute(self):
        Memory.store(self.var.getChar(), self.expr.evaluate())


class Block:
    def __init__(self):
        self.stmts = []

    def add(self, stmt):
        if not stmt:
            raise Exception("IllegalArgumentException: None statement argument");
        self.stmts.append(stmt)

    def execute(self):
        for stmt in self.stmts:
            stmt.execute()


class Iter:
    #    private ArithmeticExpression expr1;
    #    private ArithmeticExpression expr2;
    #    private ArrayList<Integer> it = new ArrayList<Integer>();;

    def __init__(self, expr1, expr2):
        if (expr1 == None or expr2 == None):
            raise Exception("IllegalArgumentException: None arithmetic expression argument")
        self.expr1 = expr1
        self.expr2 = expr2
        self.it = []

    def evaluate(self):
        self.it.append(self.expr1.evaluate())
        self.it.append(self.expr2.evaluate())
        return self.it


class LexicalAnalyzer:

    #    private List<Token> tokens;

    def __init__(self, fileName):
        assert (fileName != None)
        self.tokens = []
        with open(fileName) as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        for lineNumber, line in enumerate(lines):
            self.processLine(line, lineNumber)
        self.tokens.append(Token(lineNumber, 1, "EOS", TokenType.EOS_TOK))

    def processLine(self, line, lineNumber):
        assert (line != None and lineNumber >= 0)
        index = 0
        index = LexicalAnalyzer.skipWhiteSpace(line, index)
        while (index < len(line)):
            lexeme = LexicalAnalyzer.getLexeme(line, lineNumber, index)
            tokType = LexicalAnalyzer.getTokenType(lexeme, lineNumber, index)
            self.tokens.append(Token(lineNumber + 1, index + 1, lexeme, tokType))
            index += len(lexeme)
            index = LexicalAnalyzer.skipWhiteSpace(line, index)

    def getTokenType(lexeme, lineNumber, columnNumber):
        assert (lexeme != None and lineNumber >= 0 and columnNumber >= 0);
        tokType = None
        if (lexeme[0].isalpha()):
            if (len(lexeme) == 1):
                if (LexicalAnalyzer.isValidIdentifier(lexeme[0])):
                    tokType = TokenType.ID_TOK
                else:
                    raise Exception(
                        "LexicalException: " + "invalid lexeme at row number {} and column {}".format((lineNumber + 1),
                                                                                                      (
                                                                                                                  columnNumber + 1)))
            elif (lexeme == "if"):
                tokType = TokenType.IF_TOK
            elif (lexeme == "function"):
                tokType = TokenType.FUNCTION_TOK
            elif (lexeme == "end"):
                tokType = TokenType.END_TOK
            elif (lexeme == "else"):
                tokType = TokenType.ELSE_TOK
            elif (lexeme == "for"):
                tokType = TokenType.FOR_TOK
            elif (lexeme == "while"):
                tokType = TokenType.WHILE_TOK
            elif (lexeme == "print"):
                tokType = TokenType.PRINT_TOK
            else:
                raise Exception(
                    "LexicalException: " + "invalid lexeme at row number {} and column {}".format((lineNumber + 1),
                                                                                                  (columnNumber + 1)))
        elif (lexeme[0]).isdigit():
            if (LexicalAnalyzer.allDigits(lexeme)):
                tokType = TokenType.CONST_TOK
            else:
                raise Exception(
                    "LexicalException: " + "invalid lexeme at row number {} and column {}".format((lineNumber + 1),
                                                                                                  (columnNumber + 1)))
        elif (lexeme == "+"):
            tokType = TokenType.ADD_TOK
        elif (lexeme == "-"):
            tokType = TokenType.SUB_TOK
        elif (lexeme == "*"):
            tokType = TokenType.MUL_TOK
        elif (lexeme == "/"):
            tokType = TokenType.DIV_TOK
        elif (lexeme == "\\"):
            tokType = TokenType.REV_DIV_TOK
        elif (lexeme == "^"):
            tokType = TokenType.EXP_TOK
        elif (lexeme == "%"):
            tokType = TokenType.MOD_TOK
        elif (lexeme == "="):
            tokType = TokenType.ASSIGN_TOK
        elif (lexeme == "("):
            tokType = TokenType.LEFT_PAREN_TOK
        elif (lexeme == ")"):
            tokType = TokenType.RIGHT_PAREN_TOK
        elif (lexeme == ">="):
            tokType = TokenType.GE_TOK
        elif (lexeme == ">"):
            tokType = TokenType.GT_TOK
        elif (lexeme == "<="):
            tokType = TokenType.LE_TOK
        elif (lexeme == "<"):
            tokType = TokenType.LT_TOK
        elif (lexeme == "=="):
            tokType = TokenType.EQ_TOK
        elif (lexeme == "!="):
            tokType = TokenType.NE_TOK
        elif (lexeme == ":"):
            tokType = TokenType.COL_TOK
        else:
            raise Exception(
                "LexicalException: " + "invalid lexeme at row number {} and column {}".format((lineNumber + 1),
                                                                                              (columnNumber + 1)))
        return tokType

    def allDigits(s):
        assert (s != None)
        for c in s:
            if not c.isdigit():
                return False
        return True

    def getLexeme(line, lineNumber, index):
        assert (line != None and lineNumber >= 0 and index >= 0)
        i = index
        while (i < len(line)):
            if line[i].isspace():
                break
            i += 1
        return line[index:i]

    def skipWhiteSpace(line, index):
        assert (line != None and index >= 0)
        i = index
        while (i < len(line)):
            if not line[i].isspace():
                break
            i += 1
        return i

    def getNextToken(self):
        if (not len(self.tokens)):
            raise Exception("LexicalException: " + "no more tokens")
        return self.tokens.pop(0)

    def getLookaheadToken(self):
        if (not len(self.tokens)):
            raise Exception("LexicalException: " + "no more tokens")
        return self.tokens[0]

    def isValidIdentifier(ch):
        return ch.isalpha()

    def printLex(self):  # print all tokens and lexemes
        for token in self.tokens:
            tokType = token.getTokType()
            lexeme = token.getLexeme()
            print("The next token is: " + str(tokType) + " **** Next lexeme is: " + str(lexeme))


class Program:
    #    private Block blk;

    def __init__(self, blk):
        if (blk == None):
            raise Exception("IllegalArgumentException: None block argument")
        self.blk = blk

    def execute(self):
        self.blk.execute()


class Parser:
    #    private LexicalAnalyzer lex;

    def __init__(self, fileName):
        self.lex = LexicalAnalyzer(fileName)

    def parse(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.FUNCTION_TOK)
        functionName = self.getId()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.LEFT_PAREN_TOK)
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.RIGHT_PAREN_TOK)
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.END_TOK)
        tok = self.lex.getNextToken()
        if (tok.getTokType() != TokenType.EOS_TOK):
            raise Exception("ParserException: " + "garbage at end of file")
        return Program(blk)

    def getBlock(self):
        blk = Block()
        tok = self.lex.getLookaheadToken()
        while (Parser.isValidStartOfStatement(tok)):
            stmt = self.getStatement()
            blk.add(stmt)
            tok = self.lex.getLookaheadToken()
        return blk;

    def getStatement(self):
        tok = self.lex.getLookaheadToken();
        if (tok.getTokType() == TokenType.IF_TOK):
            stmt = self.getIfStatement()
        elif (tok.getTokType() == TokenType.WHILE_TOK):
            stmt = self.getWhileStatement()
        elif (tok.getTokType() == TokenType.PRINT_TOK):
            stmt = self.getPrintStatement()
        elif (tok.getTokType() == TokenType.ID_TOK):
            stmt = self.getAssignmentStatement()
        elif (tok.getTokType() == TokenType.FOR_TOK):
            stmt = self.getForStatement()
        else:
            raise Exception(
                "ParserException: " + "invalid statement at row " + str(tok.getRowNumber()) + " and column " + str(
                    tok.getColumnNumber()))
        return stmt;

    def getAssignmentStatement(self):
        var = self.getId()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.ASSIGN_TOK)
        expr = self.getArithmeticExpression()
        return AssignmentStatement(var, expr)

    def getPrintStatement(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.PRINT_TOK)
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.getArithmeticExpression()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expr)

    def getForStatement(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.FOR_TOK)
        var = self.getId()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.ASSIGN_TOK)
        expr1 = self.getArithmeticExpression()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.COL_TOK)
        expr2 = self.getArithmeticExpression()
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.END_TOK)
        it = Iter(expr1, expr2)
        return ForStatement(var, it, blk)

    def getWhileStatement(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.WHILE_TOK)
        expr = self.getBooleanExpression()
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.END_TOK)
        return WhileStatement(expr, blk)

    def getIfStatement(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.IF_TOK)
        expr = self.getBooleanExpression()
        blk1 = self.getBlock()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.ELSE_TOK)
        blk2 = self.getBlock()
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.END_TOK)
        return IfStatement(expr, blk1, blk2)

    def isValidStartOfStatement(tok):
        assert (tok != None);
        return (tok.getTokType() == TokenType.ID_TOK) or ((tok.getTokType() == TokenType.IF_TOK)) or (
                    tok.getTokType() == TokenType.WHILE_TOK) or (tok.getTokType() == TokenType.FOR_TOK) or (
                           tok.getTokType() == TokenType.PRINT_TOK)

    def getArithmeticExpression(self):
        tok = self.lex.getLookaheadToken()
        if (tok.getTokType() == TokenType.ID_TOK):
            expr = self.getId()
        elif (tok.getTokType() == TokenType.CONST_TOK):
            expr = self.getConstant()
        else:
            expr = self.getBinaryExpression()
        return expr

    def getBinaryExpression(self):
        tok = self.lex.getNextToken();
        if (tok.getTokType() == TokenType.ADD_TOK):
            Parser.match(tok, TokenType.ADD_TOK)
            op = ArithmeticOperator.ADD_OP
        elif (tok.getTokType() == TokenType.SUB_TOK):
            Parser.match(tok, TokenType.SUB_TOK)
            op = ArithmeticOperator.SUB_OP
        elif (tok.getTokType() == TokenType.MUL_TOK):
            Parser.match(tok, TokenType.MUL_TOK)
            op = ArithmeticOperator.MUL_OP
        elif (tok.getTokType() == TokenType.DIV_TOK):
            Parser.match(tok, TokenType.DIV_TOK)
            op = ArithmeticOperator.DIV_OP
        elif (tok.getTokType() == TokenType.REV_DIV_TOK):
            Parser.match(tok, TokenType.REV_DIV_TOK)
            op = ArithmeticOperator.REV_DIV_OP
        elif (tok.getTokType() == TokenType.EXP_TOK):
            Parser.match(tok, TokenType.EXP_TOK)
            op = ArithmeticOperator.EXP_OP
        elif (tok.getTokType() == TokenType.MOD_TOK):
            Parser.match(tok, TokenType.MOD_TOK)
            op = ArithmeticOperator.MOD_OP
        else:
            raise Exception(
                "ParserException: " + " operator expected at row " + str(tok.getRowNumber()) + " and column " + str(
                    tok.getColumnNumber()))
        expr1 = self.getArithmeticExpression();
        expr2 = self.getArithmeticExpression();
        return BinaryExpression(op, expr1, expr2)

    def getBooleanExpression(self):
        tok = self.lex.getNextToken()
        if (tok.getTokType() == TokenType.EQ_TOK):
            op = RelativeOperator.EQ_OP
        elif (tok.getTokType() == TokenType.NE_TOK):
            op = RelativeOperator.NE_OP
        elif (tok.getTokType() == TokenType.GT_TOK):
            op = RelativeOperator.GT_OP
        elif (tok.getTokType() == TokenType.GE_TOK):
            op = RelativeOperator.GE_OP
        elif (tok.getTokType() == TokenType.LT_TOK):
            op = RelativeOperator.LT_OP
        elif (tok.getTokType() == TokenType.LE_TOK):
            op = RelativeOperator.LE_OP
        else:
            raise Exception("ParserException: " + "relational operator expected at row " + str(
                tok.getRowNumber()) + " and column " + str(tok.getColumnNumber()))

        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        return BooleanExpression(op, expr1, expr2)

    def getId(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.ID_TOK)
        return Id(tok.getLexeme()[0])

    def getConstant(self):
        tok = self.lex.getNextToken()
        Parser.match(tok, TokenType.CONST_TOK)
        value = int(tok.getLexeme())
        return Constant(value);

    def match(tok, tokType):
        assert (tok != None and tokType != None)
        # print(tokType)
        if (tok.getTokType() != tokType):
            raise Exception(
                "ParserException: tokType expected at row " + str(tok.getRowNumber()) + " and column " + str(
                    tok.getColumnNumber()))


if True:
    filenames = []
    filenames.append("test1.jl")  # prints 5
    filenames.append("test2.jl")  # prints 14
    filenames.append("test3.jl")  # prints 5-10,89
    filenames.append("test4.jl")  # prints 3,333,5
    filenames.append("test5.jl")  # prints 1
    filenames.append("test6.jl")  # prints 71

    for filename in filenames:
        print('Testing {}'.format(filename))
        p = Parser(filename)
        prog = p.parse()
        prog.execute()
        # to see chart of tokens and lexemes
        Llex = LexicalAnalyzer(filename)
        Llex.printLex()
        # to see results of assignment statement
        # Memory.displayMemory()