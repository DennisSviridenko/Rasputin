import os



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
