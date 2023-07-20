import PySimpleGUI as sg
from zip_creator import make_archive

compress_ = [sg.Text("Select files to compress:"), sg.Input(tooltip="Target file"), sg.FilesBrowse("Choose", key = "files")]
destination_ = [sg.Text("Select file destination:"), sg.InputText(tooltip="File destination"), sg.FolderBrowse("Choose", key =  "folder")]
compress_button = [sg.Button("Compress"), sg.Text(key="output")]

window = sg.Window("File Zipper", layout= [compress_, destination_, compress_button])



while True:
    event, values = window.read()
    print (event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed")

window.close()
                  