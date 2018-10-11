import os


def print_file(filename):
    print(f"\nFile : {filename}")
    print('-' * 60)
    with open(filename) as f:
        for idx,line in enumerate(f):
            print(f"{idx+1} : {line}",end='')


# Get all files and folders from the given path
allfiles = os.walk(r"e:\classroom\python\sep7\demo")
for (dirname, directories, files) in allfiles:
    # print directory name
    if dirname.find('.git') >= 0:
        continue

    # print files in that directory
    for file in files:
        if file.endswith('.py'):
            print_file( dirname + "\\" + file)
