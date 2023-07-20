import zipfile

def unzip(filepath, destination):
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(destination)



if __name__ == "__main__":
    unzip("compressed.zip", "Unzipped")
    print("hi")