import os.path
from os import path

msg = ["New file name:","Existing file name:"];

def main():
    AskInfo();

def AskInfo():
    checkpoint="askinfo"
    whichoption= int(input("1-Create new file\n"
                           "2-Search for an existing file\n"
                           "Select an option by typing 1 or 2: "));
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich,pointcheck):
    global whichfilename;
    match(pointcheck):
        case 'askinfo':
            optwhich = ord(str(optionwhich));
            if(ord(str(optionwhich)) < 49 or ord(str(optionwhich)) > 50):
                print("Incorrect response.")
                AskInfo();
            else:
                if(optionwhich == 1):
                    whichfilename = str(input(msg[0]));
                else:
                    whichfilename = str(input(msg[0]));

                whichfilename = whichfilename + ".doc";
                FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exist();

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));

    if(fileexist == True):
        adminfile = open(whichfilename,"r");
    else:
        adminfile = open(whichfilename,"x");

    adminfile.close();

if __name__ == "__main__":
    main();

