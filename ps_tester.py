import sys
import io
import math
import re

user_code = '''\
a, b = map(int, input().split())
print(a / b)\
'''

class testcase:
    def __init__(self, input, output):
        if isinstance(input, list) or isinstance(input, tuple):
            self.input = ' '.join(map(str, input))
        else:
            self.input = str(input)
    
        if isinstance(output, str):
            self.output = output.rstrip()
        else:
            self.output = output

    def __str__(self) -> str:
        return f"testcase(input={self.input}, output={self.output})"
    
    def __eq__(self, case, rel_tol=1e-9, abs_tol=0) -> bool:
        if not isinstance(case, testcase):
            return False
        
        isint = lambda s: re.match(r"^-?\d+$", s) != None
        isfloat = lambda s: re.match(r"^-?\d+(?:.\d+)?$", s) != None and not isint(s)

        if isfloat(case.output):
            return self.input == case.input and math.isclose(self.output, float(case.output), rel_tol=rel_tol, abs_tol=abs_tol)
        else:
            return self.input == case.input and str(self.output).rstrip() == str(case.output).rstrip()
    
    def run(self, user_code):
        sys.stdin, sys.stdout = io.StringIO(self.input), io.StringIO()
        
        try:
            exec(user_code, {})
        except Exception as error:
            return testcase(self.input, error)
        output = sys.stdout.getvalue()

        sys.stdin, sys.stdout = sys.__stdin__, sys.__stdout__
        return testcase(self.input, output)

test_cases = [
    testcase((1, 0), 2),
    testcase((3, -1), -3),
    testcase((94, 13), 7.23076923)
]

for case in test_cases:
    runned = case.run(user_code)
    print(case, "->", runned)