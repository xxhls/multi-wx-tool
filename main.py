import os
import sys
import subprocess


if __name__ == '__main__':

    path = ""

    if not os.path.exists('config'):
        with open('config', 'a') as f:
            print("第一次使用程序，请先录入微信可执行文件地址：")
            address = input(">>")
            path = address.replace("\\", "/").replace("\"", "")
            f.write(path)
    else:
        with open('config', 'r') as f:
            path = f.read()

    number = int(input("请输入要打开的微信客户端的个数："))

    template = ["@echo off\n", "start \"\" \"微信EXE地址\"\n", "exit\n"]
    with open('run.bat', 'w', encoding='utf-8') as f:
        f.write(template[0])
        command = template[1].replace("微信EXE地址", path)
        while number != 0:
            f.write(command)
            number -= 1
        f.write(template[2])

    subprocess.Popen(
        "cmd.exe /c" + "run.bat",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    sys.exit(0)
