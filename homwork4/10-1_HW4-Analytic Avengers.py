# AUTHOR:     Bilal Zuberi, Clay Coleman, Nick Luthman, Brandon Decker
# COURSE:     ISTM 615
# PROGRAM:    Project 10-1: HTML Converter
# PURPOSE:    Create a program that reads an HTML file and converts it to plain text..
# INPUT:      groceries.html file as input
#
# PROCESS:    A program that removes HTML tags from a file and display output if any list elements specifed in HTML
#
# OUTPUT:     Consolue output of file with HTML tags removed, and an asterisks before list items.
#
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# Specifications
# Store the following data in a file named groceries.html:
# <h1>Grocery List</h1>
# <ul>
# <li>Eggs</li>
# <li>Milk</li>
# <li>Butter</li>
# </ul>
# When the program starts, it should read the contents of the file, remove the HTML
# tags, remove any spaces to the left of the tags, add asterisks (*) before the list items,
# and display the content and the HTML tags on the console as shown above.

#file IO error checking
import os 

#funtion reads the file specified and returns each line as a list
def readFileAsList(fileName: str) -> list:
    try:
        if(os.path.exists(fileName)):
            with open(fileName, "r") as inFile: #open file for reading
                fileAsList = [line.rstrip() for line in inFile] #remove new line character
        else:
            print("Error: groceries.html file not found")
    except:
        #unable to read file, return a blank list
        fileAsList = None
    finally:
        return fileAsList

#function removes all html tags <TAG> </TAG>, and return a formatted list
def removeHTMLTags(htmlList: list) ->list:
    #array to store possibe htmt tags
    tags = ["<h1>", "</h1>","<ul>", "</ul>" ,"<li>", "</li>"]
    LIST_TAG = "<li>"
    ASTR = "* "
    index = 0
    #itterate over each line in list
    while index < len(htmlList):
        #remove all spaces from the line begin and end
        line = htmlList[index].strip()
        #itterate over all tags and look find them in line
        for tag in tags:
            if line.lower().startswith(tag):
                #we have found a list tag, repalce it with (*)
                if(tag == LIST_TAG):
                   line = line.replace(tag, ASTR)
                else:
                   line = line.replace(tag, "")
            if(line.lower().endswith(tag)):
                line = line.replace(tag,"")
                break
        #copy line back to new list
        htmlList[index] = line.strip()
        #go to next item in list
        index += 1 
    
    tagsRemovedList = list(htmlList)
    return tagsRemovedList

#entery point on the program, calls other fuctinons to complete program execution
def main():
    htmlFileName = "groceries.html"
    print("HTML Converter\n")
    #read the file
    htmlFileAsList = readFileAsList(htmlFileName)
    
    #remove the html tags
    if(htmlFileAsList != None):
       tagsRemovedList = removeHTMLTags(htmlFileAsList)
       for line in tagsRemovedList:
           if(line != ""):
               print(line)

if __name__ == "__main__":

    
