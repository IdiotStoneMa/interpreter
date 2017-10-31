#！/usr/bin/env python
# -*- coding=utf-8 -*-

INTERGER, PLUS, EOF = 'INTERGER', 'PLUS', 'EOF'

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

    def error(self):
        raise Exception("Error parsing input")

    def getNextToken(self):
        inStr = self.str
        if self.curPos > len(inStr) - 1:
            return Token(EOF, None)

        cur_ch = inStr[self.curPos]
        if cur_ch.isdigit():
            token = Token(INTERGER, int(cur_ch))
            self.curPos += 1
            return token

        if cur_ch == '+':
            token = Token(PLUS, cur_ch)
            self.curPos += 1
            return token

        self.error()

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
        self.eat(PLUS)

        right = self.curToken
        self.eat(INTERGER)

        ret = left.val + right.val
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