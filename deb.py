import os
print("安装deb在全部发行版")
deb = input("你的deb链接:")
name = input("输入应用名字:")
os.system("mkdir "+name)
os.system("dpkg -x "+deb+" ./"+name)
y = input("你要安装吗(y/n):")
if y == y:
    os.system("sudo cp -frp ./"+name+"/* /")
else:
    os.system("exit")
