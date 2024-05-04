import os,sys
neededFiles=sys.argv
neededFiles.append("clean-cwd.py")
cwd=os.path.dirname(os.path.realpath(__file__))
if not os.path.isdir("moved"):
    os.makedirs("moved")
for doc in os.listdir(cwd):
    if doc in neededFiles or doc=="moved":
        continue
    else:
        os.rename(doc, f"moved/{doc}")