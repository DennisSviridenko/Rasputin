import sys 
import os

code = sys.argv[1]
param1 = sys.argv[2]
param2 = sys.argv[3]
passwd = ""

match code:
    case "1":
        if os.path.exists(f"Root/User/{param1}"):
            file = open(f"Root/User/{param1}", "r")
            content = file.read()
            file.close()

            for i in content:
                if i == ":":
                    break
                elif i != ":":
                    passwd = passwd + i
            
            if passwd == param2:
                os.system("python interface.py")
            else:
                print("AGEISCODE: INTERLOPER \n ACCES DENIED")

        else: 
            print("AGEISCODE: ANONYMOUS \n USER NOT FOUND")

    case "2":
        inp = input(">>> ")
        x = 0
        lol = ""
        jo = ""
        for i in inp:
            if i == " ":
                for j in range(0, x):
                    lol = lol + inp[j]
                for j in range(x, len(inp)):
                    if inp[j] == ".":
                        jo = jo + "/"
                    else:
                        jo = jo + inp[j]
            x += 1


        if lol or jo != "":
            if os.path.exists(f"Root/commands/{lol}"):
                os.system(f"python Root/commands/{inp}")
            elif "start" in inp:
                os.system(f"python {jo}/main.py")
        else:
            os.system(inp)


