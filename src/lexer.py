import ply.lex as lex

# 定义词法规则
tokens = (
    'BEGIN',
    'END',
    'IF',
    'ELSE',
    'LOOP',
    'WHILE',
    'FOR',
    'BREAK',
    'CONTINUE',
    'FUNCTION',
    'RETURN',
    'CLASS',
    'NEW',
    'VARIABLE',
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EQ',
    'NE',
    'GT',
    'LT',
    'GE',
    'LE',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'SEMI',
    'ASSIGN',
    'PRINT',
    'INPUT',
    'IMPORT',
    'TRY',
    'EXCEPT',
    'FINALLY',
    'ARRAY'
)

# 定义关键字字典
keywords = {
    '开始': 'BEGIN',
    '结束': 'END',
    '如果': 'IF',
    '否则': 'ELSE',
    '否则如果': 'ELSE',
    '循环': 'LOOP',
    '当': 'WHILE',
    '遍历': 'FOR',
    '跳出': 'BREAK',
    '继续': 'CONTINUE',
    '函数': 'FUNCTION',
    '返回': 'RETURN',
    '类': 'CLASS',
    '新建': 'NEW',
    '真': 'TRUE',
    '假': 'FALSE',
    '空': 'NULL',
    '且': 'AND',
    '或': 'OR',
    '非': 'NOT',
    '显示': 'PRINT',
    '输入': 'INPUT',
    '导入': 'IMPORT',
    '尝试': 'TRY',
    '捕获': 'EXCEPT',
    '最终': 'FINALLY',
    '数组': 'ARRAY'
}

# 正则表达式规则

# 匹配空白字符，但不返回标记
t_ignore = ' \t\r\n'

# 匹配标点和运算符
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMI = r'；|;'  # 支持中文分号和英文分号
t_ASSIGN = r'='

# 匹配变量和关键字
def t_VARIABLE(t):
    r'[a-zA-Z\u4e00-\u9fa5][a-zA-Z0-9\u4e00-\u9fa5]*'
    # 检查是否是关键字
    t.type = keywords.get(t.value, 'VARIABLE')
    return t

# 匹配数字
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# 匹配字符串
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # 去掉引号
    return t

# 错误处理规则
def t_error(t):
    print(f"非法字符: '{t.value[0]}' 在位置 {t.lexpos}")
    t.lexer.skip(1)

# 构建词法分析器
lexer = lex.lex()

# 测试词法分析器
def test_lexer():
    data = '''
开始
    显示("你好，世界！")
    数字 = 10
    显示(数字)
结束
    '''
    print("测试数据:")
    print(data)
    
    lexer.input(data)
    print("\n标记列表:")
    for tok in lexer:
        print(f"类型: {tok.type}, 值: {tok.value}, 位置: {tok.lexpos}")

if __name__ == '__main__':
    test_lexer() 