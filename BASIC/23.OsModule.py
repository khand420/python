import os 

os.getcwd()  #Print current working directory
os.name()   #os module name in window

os.chdir('C://')
# os.getcwd()
os.chdir('C://projects//') #for changing directory
os.mkdir('newDirectory')   #for make directory
os.rmdir('newDirectory')   #for remove directory
os.makedirs('newDirectory//new2')   #for remove directory
os.listdir() #give list of all directory

clear = lambda:os.system('cls') #clear the screen of the command prompt
clear()

os.path.exists('C://')