import os
print("Install deb in all linux")
deb = input("Your deb link:")
name = input("Enter the app name:")
os.system("mkdir "+name)
os.system("dpkg -x "+deb+" ./"+name)
y = input("Do you want to install(y/n):")
if y == y:
    os.system("sudo cp -frp ./"+name+"/* /")
else:
    os.system("exit")

