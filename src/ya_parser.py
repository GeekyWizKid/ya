import ply.yacc as yacc
from lexer import tokens, lexer

# 更详细的调试信息
yacc.yacc.yaccdebug = True

# 定义语法规则
def p_program(p):
    '''program : BEGIN statements END'''
    print(f"解析程序")
    p[0] = p[2]

def p_statements(p):
    '''statements : statement
                 | statements statement'''
    # print(f"解析语句序列")
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : display_statement
                | assignment_statement
                | if_statement
                | loop_statement
                | while_statement
                | array_statement
                | empty'''
    # print(f"解析语句")
    p[0] = p[1]

def p_display_statement(p):
    '''display_statement : PRINT LPAREN expression RPAREN'''
    # print(f"解析显示语句")
    p[0] = ('display', p[3])

def p_assignment_statement(p):
    '''assignment_statement : VARIABLE ASSIGN expression'''
    # print(f"解析赋值语句: {p[1]}")
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN BEGIN statements END
                   | IF LPAREN condition RPAREN BEGIN statements END ELSE BEGIN statements END'''
    # print(f"解析条件语句")
    if len(p) == 8:
        p[0] = ('if', p[3], p[6], None)
    else:
        p[0] = ('if', p[3], p[6], p[10])

def p_loop_statement(p):
    '''loop_statement : LOOP BEGIN statements END'''
    # print(f"解析循环语句")
    p[0] = ('loop', p[3])

def p_while_statement(p):
    '''while_statement : WHILE LPAREN condition RPAREN BEGIN statements END'''
    # print(f"解析while循环")
    p[0] = ('while', p[3], p[6])

def p_array_statement(p):
    '''array_statement : ARRAY VARIABLE ASSIGN LBRACKET array_elements RBRACKET'''
    # print(f"解析数组语句")
    p[0] = ('array_decl', p[2], p[5])

def p_array_assign(p):
    '''array_statement : VARIABLE LBRACKET expression RBRACKET ASSIGN expression'''
    p[0] = ('array_assign', p[1], p[3], p[6])

def p_array_elements(p):
    '''array_elements : expression
                     | expression COMMA array_elements'''
    # print(f"解析数组元素")
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_condition(p):
    '''condition : expression EQ expression
                | expression GT expression
                | expression LT expression
                | expression GE expression
                | expression LE expression'''
    # print(f"解析条件")
    p[0] = (p[2], p[1], p[3])

def p_expression(p):
    '''expression : term
                 | expression PLUS term
                 | expression MINUS term'''
    # print(f"解析表达式")
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''term : factor
           | term TIMES factor
           | term DIVIDE factor'''
    # print(f"解析项")
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_factor(p):
    '''factor : NUMBER
             | STRING
             | VARIABLE
             | array_access
             | LPAREN expression RPAREN'''
    # print(f"解析因子: {p[1]}")
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_array_access(p):
    '''array_access : VARIABLE LBRACKET expression RBRACKET'''
    p[0] = ('array_access', p[1], p[3])

def p_empty(p):
    'empty :'
    p[0] = None

def p_error(p):
    if p:
        print(f"语法错误在 '{p.value}', 类型: {p.type}, 位置: {p.lexpos}")
    else:
        print("语法错误在文件末尾")

# 构建语法分析器
parser = yacc.yacc()

# 测试语法分析器
def test_parser():
    data = '''
开始
    显示("你好，世界！")
    数字 = 10
    显示(数字)
结束
'''
    print("测试数据:")
    print(data)
    
    print("\n词法分析:")
    lexer.input(data)
    for tok in lexer:
        print(tok)
    
    print("\n语法分析:")
    lexer.input(data)
    result = parser.parse(data, lexer=lexer, debug=True)
    print("解析结果:", result)

if __name__ == '__main__':
    test_parser() 