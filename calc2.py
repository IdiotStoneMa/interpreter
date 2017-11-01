#！/usr/bin/env python
# -*- coding=utf-8 -*-

INTERGER, PLUS, MINUS, EOF = 'INTERGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, val):
        self.type = type
        self.val = val

    def __str__(self):
        return 'Token({type}, {val})'.format(type=self.type, val=repr(self.val))

    def __repr__(self):
        return self.__str__()

class interpreter(object):
    def __init__(self, inStr):
        self.str = inStr
        self.curPos = 0
        self.curToken = None
        self.curCh = self.str[self.curPos]

    def error(self):
        raise Exception("Error parsing input")

    def advance(self):
        self.curPos += 1
        if self.curPos > len(self.str) - 1:
            self.curCh = None
        else:
            self.curCh = self.str[self.curPos]

    def interget(self):
        result = ''
        while self.curCh is not None and self.curCh.isdigit():
            result += self.curCh
            self.advance()

        return int(result)

    def skip_whiteSpace(self):
        while self.curCh is not None and self.curCh.isspace():
            self.advance()

    def getNextToken(self):
        while self.curCh is not None:
            if self.curCh.isspace():
                self.skip_whiteSpace()
                continue
            if self.curCh.isdigit():
                token = Token(INTERGER, self.interget())
                self.advance()
                return token

            if self.curCh == '+':
                self.advance()
                token = Token(PLUS, '+')
                return token

            if self.curCh == '-':
                self.advance()
                token = Token(MINUS, '-')
                return token
            self.error()
        return Token(EOF, None)

    def eat(self, token_type):
        if self.curToken.type == token_type:
            self.curToken = self.getNextToken()
        else:
            self.error()

    def expr(self):
        self.curToken = self.getNextToken()
        left = self.curToken
        self.eat(INTERGER)

        op = self.curToken
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        right = self.curToken
        self.eat(INTERGER)

        if op.type == PLUS:
            ret = left.val + right.val
        else:
            ret = left.val - right.val

        return ret

def main():
    while True:
        try:
            #获取用户输入
            inStr = input("Calc >")
        except EOFError:
            break

        if not inStr:
            continue

        interpre = interpreter(inStr)
        ret = interpre.expr()
        print(ret)

if __name__ == '__main__':
    main()