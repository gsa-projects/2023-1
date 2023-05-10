import sys
import io
import math
import re

class testcase:
    def __init__(self, input, output):
        if isinstance(input, list) or isinstance(input, tuple):
            self.input = ' '.join(map(str, input))
        else:
            self.input = str(input)

        if isinstance(output, Exception):
            self.output = output
        else:
            self.output = str(output).rstrip()

    def __str__(self) -> str:
        return f"testcase(input={self.input}, output={self.output})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, case, rel_tol=1e-9, abs_tol=0) -> bool:
        if not isinstance(case, testcase):
            return False
        elif isinstance(self.output, Exception) or isinstance(case.output, Exception):
            return False

        isint = lambda s: re.match(r"^-?\d+$", s) is not None
        isfloat = lambda s: re.match(r"^-?\d+(?:.\d+)?$", s) is not None and not isint(s)

        if isfloat(case.output) or isfloat(self.output):
            return self.input == case.input and math.isclose(float(self.output) if isfloat(self.output) else int(self.output), float(case.output) if isfloat(case.output) else int(case.output), rel_tol=rel_tol, abs_tol=abs_tol)
        else:
            return self.input == case.input and self.output == case.output

    def run(self, user_code):
        sys.stdin, sys.stdout = io.StringIO(self.input), io.StringIO()

        try:
            exec(user_code, {})
        except Exception as error:
            return testcase(self.input, error)
        output = sys.stdout.getvalue()

        sys.stdin, sys.stdout = sys.__stdin__, sys.__stdout__
        return testcase(self.input, output)

class testcases:
    def __init__(self, *cases):
        self.testcases = list(cases)
    
    def __add__(self, case):
        self.testcases.append(case)
        return self
    
    def run(self, code):
        runned = []
        for case in self.testcases:
            runned.append(case.run(code))
        
        return runned
    
    def scoring(self, runned):
        count = 0
        for i in range(len(self.testcases)):
            isAC = runned[i] == self.testcases[i]
            if isAC:
                count += 1
            print(f"Case {i+1}: {'✅ AC' if isAC else '⛔ WA'}", end="")
            if not isAC and isinstance(runned[i].output, Exception):
                print(f" # {type(runned[i].output).__name__}", end="")
            # print(f"\n    {runned[i]} | {test_cases[i]}", end="")
            print()

        print(f"{count}/{len(self.testcases)} success!")

    def __str__(self) -> str:
        ret = "[\n"
        for case in self.testcases:
            ret += f"    {case},\n"
        ret = ret[:-2]
        return ret + "\n]"

    def __repr__(self) -> str:
        return self.__str__()

test_cases = testcases(
    testcase((0.1, 0.2), 0.3),
    testcase((0.2, 0.2), 0.4),
    testcase((0.3, 0.2), 0.5),
    testcase((0.4, 0.3), 0.7)
)

# print(test_cases)

user_code = open("ps/user_code.txt").read()
runned = test_cases.run(user_code)
test_cases.scoring(runned)