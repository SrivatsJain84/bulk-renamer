import os

folder  = input(str("Enter the path of the folder: "))													#enter the path
file_extention = input(str("What type of file do you want to rename(example - .txt): "))						#enter file extention
new_name = input(str("What name do you wanna give to your file(example - cat): "))								#enter new name of that type of files
a = 1

for filename in os.listdir(folder):
	if filename.endswith(file_extention):
		old = os.path.join(folder, filename)
		new = os.path.join(folder, f"{new_name}_{a}{file_extention}")
		os.rename(old ,new)
		a += 1

#This is safe but always read the code before running it on your device#
#TOUCH GRASS:)#
