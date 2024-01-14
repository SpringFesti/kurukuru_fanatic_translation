import os

def to_utf8():
    for in_file in os.listdir("scenario"):
        with open("scenario/" + in_file, encoding="UTF-16LE") as f:
            content = f.read()
        with open("scenario_utf8/" + in_file, encoding="UTF-8", mode="w") as f:
            f.write(content)

def to_utf16():
    for in_file in os.listdir("scenario_utf8"):
        with open("scenario_utf8/" + in_file, encoding="UTF-8") as f:
            content = f.read()
        with open("scenario/" + in_file, encoding="UTF-16LE", mode="w") as f:
            f.write(content)


to_utf8()