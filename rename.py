import os

folder  = "C:/Users/PC/Downloads/images/wallpapers"													#enter the path
file_extention = input(str("What type of file do you want to rename: "))						#enter file extention
new_name = input(str("What name do you wanna give to your file: "))								#enter new name of 
																								#that type of files
a = 36

for filename in os.listdir(folder):
	if filename.endswith(file_extention):
		old = os.path.join(folder, filename)
		new = os.path.join(folder, f"{new_name}_{a}{file_extention}")
		os.rename(old ,new)
		a += 1