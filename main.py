import os

dirs = []

def listdirs(rootdir):

    for it in os.scandir(rootdir):
        if it.is_dir():
            dirs.append(it.path)
            listdirs(it)
    return dirs


def makeBook():
    stack = []
    dirs.clear()
    c = os.getcwd()
    c = '/home/gareth/Downloads/'
    listdir = []
    tmpDirs = listdirs(c)
    for l in tmpDirs:
        listdir.append(l.replace(c, ''))

    if listdir:
        d = listdir[0].split('/')
        depth = len(d)
        startCount = depth - 1
        count = depth
        lastDepth = depth - 1

        for l in listdir:
            line = ""
            d = l.split('/')
            depth = len(d)
            delta = depth - lastDepth
            entry = str(d[-1:][0])
            if delta > 0:                   # deeper nesting
                for pp in range(abs(delta)):
                    stack.append(1)
                count = 1
            if delta < 0:                   # shallower nesting
                for pp in range(abs(delta)):
                    count = stack.pop()
                count = stack.pop()
                stack.append(count+1)
            if delta == 0:
                count = stack.pop()
                stack.append(count+1)
            for level in range(depth - 1):
                line = line + " "
            for level in range(depth):
                line = line + str(stack[level])
                if depth - level > 1:
                    line = line + "."
            count = count + 1
            for fill in range(120 - len(line) - len(entry)):
                line = line + " "
            line = line + entry
            lastDepth = depth
            print(line)

    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makeBook()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
