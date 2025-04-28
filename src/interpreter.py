class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        if isinstance(ast, list):
            for statement in ast:
                self.execute(statement)
        else:
            self.execute(ast)

    def execute(self, statement):
        if not statement:
            return

        stmt_type = statement[0]
        if stmt_type == 'display':
            value = self.evaluate(statement[1])
            print(value)
        elif stmt_type == 'assign':
            var_name = statement[1]
            value = self.evaluate(statement[2])
            self.variables[var_name] = value
        elif stmt_type == 'if':
            condition = self.evaluate_condition(statement[1])
            if condition:
                self.interpret(statement[2])
            elif statement[3]:
                self.interpret(statement[3])
        elif stmt_type == 'loop':
            while True:
                self.interpret(statement[1])
        elif stmt_type == 'while':
            while self.evaluate_condition(statement[1]):
                self.interpret(statement[2])
        elif stmt_type == 'array_decl':
            var_name = statement[1]
            elements = [self.evaluate(e) for e in statement[2]]
            self.variables[var_name] = elements
        elif stmt_type == 'array_assign':
            var_name = statement[1]
            index = self.evaluate(statement[2])
            value = self.evaluate(statement[3])
            self.variables[var_name][index] = value

    def evaluate(self, expr):
        if isinstance(expr, tuple):
            if expr[0] == 'array_access':
                var_name = expr[1]
                index = self.evaluate(expr[2])
                return self.variables[var_name][index]
            op = expr[0]
            left = self.evaluate(expr[1])
            right = self.evaluate(expr[2])
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
        elif isinstance(expr, str) and expr in self.variables:
            return self.variables[expr]
        else:
            return expr

    def evaluate_condition(self, condition):
        op = condition[0]
        left = self.evaluate(condition[1])
        right = self.evaluate(condition[2])
        if op == '==':
            return left == right
        elif op == '>':
            return left > right
        elif op == '<':
            return left < right 