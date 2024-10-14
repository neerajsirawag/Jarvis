import re

def find_syntax_error(code):
    try:
        compile(code, filename='<string>', mode = 'exec')
        print("No syntax error found.")
    except SyntaxError as e:
        # print(f"Syntax error is found in line {e.lineno}:")
        # print(e.text)
        # print(" " * (e.offset - 1) + "^")
        # print(e)
        return e.lineno
    return None


def Filter(txt):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern,txt,re.DOTALL)
    
    if matches:
        python_code = matches[0].strip()
        return python_code
    else:
        return None


def CodeFiter(txt:str):
    if "python\nCopy code" in txt:
        code = txt.splitlines()
        code = code[code.index("Copy code")+1:]
        txtCode = ""
        for i in code:
            txtCode += f"{i}\n"
        while 1:
            this = find_syntax_error(txtCode)
            if this is None:
                break
            else:
                code = code[:this-1]
                txtCode = ""
                for i in code:
                    txtCode += f"{i}\n"
        return txtCode
    else:
        return None
