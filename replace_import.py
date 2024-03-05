import os

if __name__ == "__main__":
    for root, dirs, files in os.walk("./mo", topdown=False):
        for name in files:
            filepath = os.path.join(root, name)
            if os.path.exists(filepath) and name.endswith(".py"):
                wlines = []
                check = False
                with open(filepath, "r") as read_file:
                    lines = read_file.readlines()                    
                    for line in lines:
                        
                        if "from openvino.tools.mo.utils import class_registration" in line:
                            line = line.replace("from openvino.tools.mo.utils import class_registration", 
                                                "from utils import class_registration")
                        if "from openvino.tools.mo." in line:
                            line = line.replace("from openvino.tools.mo.", 
                                                "from ")                            
                        wlines.append(line)
                        
                with(open(filepath, "w")) as write_file:
                    write_file.writelines(wlines)
                    
                print("Done writing: {}".format(filepath))