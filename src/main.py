import sys
from lexer import lexer
from ya_parser import parser
from interpreter import Interpreter

def print_usage():
    print("雅语言解释器")
    print("用法: python main.py <源文件>")
    print("示例: python main.py examples/hello_world.ya")

def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    source_file = sys.argv[1]
    
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{source_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 读取文件时发生错误: {str(e)}")
        sys.exit(1)

    try:
        # 语法分析
        ast = parser.parse(data, lexer=lexer)
        if not ast:
            print("错误: 语法分析失败")
            sys.exit(1)

        # 解释执行
        interpreter = Interpreter()
        interpreter.interpret(ast)

    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main() 