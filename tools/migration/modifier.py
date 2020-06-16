import json
import re

def handleFileOfDeclaration(element4File2Exp, moduleName):
    fileOfDeclaration = (open(element4File2Exp[0], 'r+'))
    fileOfDeclarationText = fileOfDeclaration.readlines()
    fileOfDeclarationText.append(
        "\nvar "+moduleName+" = ( function () {\nreturn {\n")
    [fileOfDeclarationText.append("{0} : {0}".format(
        element4Func2Exp["name"])) for element4Func2Exp in element4File2Exp[1]]
    fileOfDeclarationText.append("\n}\n})()\n")
    print(fileOfDeclarationText)
    fileOfDeclaration.seek(0)
    fileOfDeclaration.writelines(fileOfDeclarationText)
    fileOfDeclaration.close()

def handleCallSites4Func(element4Func2Exp, moduleName):
    for callFile, lineNos in (element4Func2Exp['Called@'].items()):
        fileOfCallSite = (open(callFile, 'r+'))
        fileOfCallSiteText = (fileOfCallSite.readlines())
        for line in lineNos:
            print(fileOfCallSiteText[line-1], "\n changed to:\n")
            fileOfCallSiteText[line-1] = (re.sub(re.escape(element4Func2Exp['name']),
                                                 moduleName+"."+element4Func2Exp['name'], fileOfCallSiteText[line-1]))
            print(fileOfCallSiteText[line-1], "\n")
        fileOfCallSite.seek(0)
        fileOfCallSite.writelines(fileOfCallSiteText)
        fileOfCallSite.close()

def genModuleName(fileName):
    return "DPR_"+fileName.split("/")[-1].split(".")[0]+"_mod"

def exposeFiles(dataFileName,beginningIndex,endIndex):
  funcsToExpByfile = json.load(open(dataFileName,"r",encoding="utf8"))
  for element4File2Exp in funcsToExpByfile[beginningIndex:endIndex]:
      print(element4File2Exp[0])
      moduleName = genModuleName(element4File2Exp[0])
      handleFileOfDeclaration(element4File2Exp, moduleName)
      for element4Func2Exp in (element4File2Exp[1]):
          print("\nfunction - ", element4Func2Exp['name'], "\n")
          handleCallSites4Func(element4Func2Exp, moduleName)

exposeFiles("functionsToExposeForFile.json",beginningIndex=0,endIndex=2)
