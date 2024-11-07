import datetime
import os
import shutil

# print(os.chdir("/Users"))  # cd /Users   cd \Users
print(os.getcwd())  # get current working directory
print(os.listdir())
files = os.listdir()

for file in files:
    if file.endswith(".py"):
        print(file)

os.mkdir("test")
os.makedirs("test1/test2/test3")
os.rmdir("test")
os.removedirs("test1/test2/test3")

os.chdir("/Users/kevin/Desktop")
files_on_desktop = os.listdir()
#
today = datetime.date.today()
# os.makedirs(f"movies/{today}")
#
# for file in files_on_desktop:
#     if file.endswith(".mp4"):
#         shutil.move(file, f"movies/{today}/{file}")
#
# today = datetime.date.today()
os.makedirs(f"images/{today}")

for file in files_on_desktop:
    if file.endswith(".png"):
        shutil.move(file, f"images/{today}/{file}")

print(files_on_desktop)
