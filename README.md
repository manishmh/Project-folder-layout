# Project-folder-layout

## This programme currently works on linux devices only.

This programme let's you run command anywhere in your local system to create layout of folder and files<br/> of your project with boiler plate of respective of languages. <br/>
<br/>
**Java,  C++,  C,  Html,  CSS,  Python**<br/>
<br/>
## How to set up and use this programme.<br/>

**Step 1:** <br/>
Download Python file and set it's path to .bashrc <br/>
<br/>
open bashrc file
```vim
vim~/.bashrc
```
Add this code and path to the flle your downloaded
```vim
export PATH="$PATH:$HOME/path to the folder"
```
**step 2:**<br/>
open the pyhton file in any editor and edit the path of the boiler plate.<br/>
Add the path to the boiler plate in line 24 in path varible
<br/><br/>
**step 3:**<br/>
Change the access mode of make.py python file<br/>
```vim
chmod +x make.py
```
</br> ................................................................................................................
## Your programme is ready to run.
**Let's create a website project layout as an example**<br/><br/>
![cli](https://user-images.githubusercontent.com/84000636/186934556-979a79a2-1c65-49bd-989e-0667fc2cf2d8.png)<br/>
- make.py : python file which runs the code
- website : Project type
- portfolio : name of the project
- about, works, blog, contact : name of the pages you have in templates file for the website.
</br></br>


**You can add many files and no files, just add . at the end of folder name and it will create only index file.** <br/>
![Screenshot from 2022-08-26 20-56-33](https://user-images.githubusercontent.com/84000636/186939766-f9defc1a-343b-44bc-a3a6-78789ef83090.png)</br>

This creates a folder named portfolio with static templates and server.py and each folder containing respective files</br>
It will automatically open sublime code with the project. but if you prefer vscode or other editor replace **sublime-text.subl .** with **code .** at line 33</br></br>
![Folder](https://user-images.githubusercontent.com/84000636/186936491-dd7c82fe-45c6-4f30-93d7-b28c1a524dcc.png)<br/></br>
## Server.py file with pre written and ready to run code<br/>
![Server](https://user-images.githubusercontent.com/84000636/186938851-225ec3fb-f51a-4f64-90d2-d550df2bd563.png)
<br/></br>
**This programme is mostly modified for web project.</br>
you can create python project and replacing website with python and similier with java C C++**</br> <br/>
![Screenshot from 2022-08-26 21-05-32](https://user-images.githubusercontent.com/84000636/186961748-6e589e3b-dac1-4f00-97fa-c5f7bc5f1c9c.png)
</br>
![Screenshot from 2022-08-26 21-05-51](https://user-images.githubusercontent.com/84000636/186961954-2f575340-161d-4e72-8700-1fcd2e27bfe5.png)




