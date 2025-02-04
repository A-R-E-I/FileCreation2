import os.path
import sys
from os import path

msg = ["New file name:","Existing file name:"];

def main():
    AskInfo();

def AskInfo():
    checkpoint="askinfo"
    whichoption= str(input("1-Create new file\n"
                           "2-Search for an existing file\n"
                           "3-exit\n"
                           "Select an option by typing 1, 2, or 3: "));
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich,pointcheck):
    global whichfilename;
    match(pointcheck):
        case 'askinfo':
            optwhich = ord(str(optionwhich));
            if(optwhich < 49 or optwhich > 51):
                print("Incorrect response.")
                AskInfo();
            else:
                match(optwhich):
                    case 49:
                        whichfilename = str(input(msg[0]));
                    case 50:
                        whichfilename = str(input(msg[1]));
                    case 51:
                        print("Goodbye");
                        sys.exit();

                whichfilename = whichfilename + ".txt";
                FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));

    if(fileexist == True):
        adminfile = open(whichfilename,"r");
        print("File exist");
    else:
        adminfile = open(whichfilename,"x");
        print("text file created")

    adminfile.close();

if __name__ == "__main__":
    main();
