def copy_file():
    try:
        file = open("fileToCopy.txt", "r")
        toCopy = open("copyFile.txt", "w")
        text = file.readlines()
        for line in text:
            if(not line.startswith('#')):
                toCopy.write(line)
    finally:
        file.close()
        toCopy.close()

copy_file()
