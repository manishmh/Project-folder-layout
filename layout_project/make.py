#! /usr/bin/python3

from pathlib import Path
import sys
import os
from string import Template

# sys files
pt = sys.argv[1]  # type of the project 
folder_name = sys.argv[2]  # project folder name
files = sys.argv[3:]  # names of the files

# create the folder of the project
try:
    os.mkdir(folder_name)
except OSError as error:
    print('directory already exist!')

# get the directory and add the newly created folder
cwd = os.getcwd()
cwd = os.path.join(cwd, folder_name)

# Boiler plate path for files
path = '/home/manish/manish/python/projects/create_project/boiler_plate/'


def open_applications():
    # os.system('firefox')
    os.chdir("/")
    os.chdir(cwd)
    os.system('ls')
    # os.system('code .')
    os.system('sublime-text.subl .')


def replace_text(read_file, names):
    x = Template(f'{read_file}')
    y = x.substitute({'about': names})
    return y


def type_website():
    os.makedirs(f'{cwd}/static/assets/images')  # make static folder
    os.mkdir(f'{cwd}/templates')  # make templates folder
    os.mkdir(f'{cwd}/static/css')  # make directory for css
    os.mkdir(f'{cwd}/static/js')  # make directory for javascript

    # make server.py FLASK file
    with open(f'{cwd}/server.py', mode='w') as file:
        with open(f'{path + "server.txt"}', 'r') as html_file:
            file.write(f'{html_file.read()}')

    with open(f'{cwd}/templates/index.html', mode='w') as file:
        with open(f'{path + "html_file.txt"}', 'r') as html_file:
            file.write(f'{html_file.read()}')

    with open(f'{cwd}/static/css/style.css', mode='w') as file:
        with open(f'{path + "css_file.txt"}', 'r') as html_file:
            file.write(f'{html_file.read()}')

    for names in files:
        if names == '.':
            break
        else:
            with open(f'{cwd}/templates/{names}.html', mode='w') as file:
                with open(f'{path + "html_file.txt"}', 'r') as html_file:
                    file.write(f'{html_file.read()}')


# make files and replace text in java files
def make_file(extention, file_name):
    for names in files:
        if names == '.':
            break
        else:
            with open(f'{cwd}/{names}{extention}', mode='w') as file:
                with open(f'{path + file_name}', 'r') as bp:
                    if extention == '.java':
                        x = Template(bp.read())
                        y = x.substitute({'file_name': names, 'folder_name': folder_name, 'title': names})
                        file.write(y)
                    else:
                        file.write(f'{bp.read()}')                    



# main function to run the file
def main():
    if pt == 'web' or pt == 'Web' or pt == 'WEB' or pt =='website' or pt == 'Website' or pt == 'WEBSITE' or pt == 'html' or pt == 'Html' or pt == 'HTML':
        type_website()
        open_applications()

    elif pt == 'python' or pt == 'Python' or pt == 'PYTHON' or pt == 'py' or pt == 'Py' or pt == 'PY':
        extention = '.py'
        make_file(extention, 'py.txt')
        open_applications()

    elif pt == 'java' or pt == 'Java' or pt == 'JAVA' or pt == 'j':
        extention = '.java'
        make_file(extention, 'java_file.txt')
        open_applications()

    elif pt == 'C' or pt == 'c':
        extention = '.c'
        make_file(extention, 'c_file.txt')
        open_applications()

    elif pt == 'cpp' or pt == 'Cpp' or pt == 'CPP' or pt == 'c++' or pt == 'C++':
        extention = '.cpp'
        make_file(extention, 'cpp_file.txt')
        open_applications()

main()
