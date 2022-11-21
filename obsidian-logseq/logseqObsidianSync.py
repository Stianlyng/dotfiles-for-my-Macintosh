

import os
import glob
import time


def readTextFile(path):
    with open(path, 'r') as txt:
        lines = txt.readlines()
    return lines    

def writeTextFile(path, filename, textArray):

    filename = filename.split('/')[-1]
    
    with open(path+filename, 'w') as txt:
        txt.writelines(textArray)


def log2obs(lines):

    block = []

    for i in range(len(lines)):

        line = lines[i].replace('- #','#').replace('\t','').replace('- >','>').lstrip(" ")
        if '- #' in lines[i] or i == 0:
            block.append(line)
        elif i > 0 and block[-1][0] == '#':
            block.append(line)
        elif '>' in lines[i]:
            blockQuote = line.lstrip(" ")
            block.append(blockQuote)
        else:
            if lines[i].count('\t') == lines[i-1].count('\t'):
                tabs = block[-1].count('\t')
                block.append((tabs * '\t') + line)
            else:
                prev = (lines[i].count('\t')) - (lines[i-1].count('\t')) 
                tabs = prev + block[i-1].count('\t')
                block.append((tabs * '\t') + line)

        
        # Format picture
        if '](../assets/' in block[i]:

            img = getImageSyntax(block[i])
            if img != -1:
                block[i] = block[i].replace(img[0],f"![[{img[-1]}]]").replace('../assets/', '')

            
        
    return block

def getImageSyntax(line):
    start = line.find('![')
    if start != -1:
        middle = line.find('](')

        end = -1
        nestedElement = 0
        for i in range(len(line) - middle):
            
            char = line[i + middle]
            if char == '(':
                nestedElement += 1
            elif char == ')':
                nestedElement -= 1
            if nestedElement == 0 and char == ')':
                end = i + middle + 1
        return [line[start:end], line[start:middle+1], line[middle+2:end-1]]
    else:
        return -1

def checkFileNameFor(symbol,path):
    lst = getAllDocsInDir(path)
    for i in lst:
        if symbol in i:

            print(lst)

def getAllDocsInDir(path):
    return glob.glob(f"{path}*.md")

def getLastModifiedMarkdownDoc(path):

    # search all files inside a specific folder
    # *.* means file name with any extension
    directoryList = glob.glob(f"{path}*.md")
    
    res = 0
    filePath = ''
    for i in directoryList:

        ti_m = os.path.getmtime(i)
        if ti_m > res:
            res = ti_m
            filePath = i
        
    return filePath

def convertToObsidian(path,filename):
      txtArr = readTextFile(filename)
      formatter = log2obs(txtArr)
      writeTextFile(path, filename, formatter)

syncConfig = {}

app = 'logseq'
convertAll = False
obsidianPath = "/Users/stig/Documents/obsidian/notes/"
logseqPath = "/Users/stig/Documents/obsidian/logseq/pages/"
if app == 'logseq':
    if convertAll is True:
        filenames = getAllDocsInDir(logseqPath)
        for i in filenames:
            convertToObsidian(obsidianPath,i)
    else:
        filename = getLastModifiedMarkdownDoc(logseqPath)
        convertToObsidian(obsidianPath,filename)

#print(time.time())
    
#with open("/Users/stig/Documents/obsidian/system/syncConfig.md", 'a') as txt:
#    txt.write(f"last_obsidian_sync: {time}")
