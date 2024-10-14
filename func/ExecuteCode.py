import subprocess

def execute(code:str):
    code = "from func.SpeakOffline import Speak \n"+code 
    code = code.replace("print","Speak")
    
    with open(r"temp.py","w") as f:
        f.write(code)
        
    subprocess.getoutput("python temp.py 2> error.log")
    
    with open(r"error.log","r") as f:
        res = f.read()
        if res != "":
            return False
        else:
            return True
        
# execute("a=5+5\nprint(a)")