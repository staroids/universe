import os, sys
import yaml
import re

categories = ["analytics", "business", "others"]
packageFileName = "package.yaml"

def errorExit(msg):
  print(msg)
  sys.exit(1)

allPackages = {}

def validatePackageYaml(registryClass, filename):
  print("validate " + str(filename))
  if not os.path.isfile(filename):
    errorExit("Not found " + filename)

  with open(filename) as file:
    package = yaml.full_load(file)

  assert package["name"] != None
  assert package["name"] not in allPackages
  assert package["description"] != None
  assert package["category"] in categories
  assert re.match("http(s)?://.*[.](svg|jpg|jpeg|png)", package["logo"].lower())
  assert len(package["repository"].split("/")) == 2
  
  package["class"] = registryClass
  allPackages[package["name"]] = package


def loadRegistry(dir):
  if not os.path.isdir(dir):
    return
  for d in os.listdir(dir):
    dirname = os.fsdecode(d)
    packageYamlFile = os.path.join(dir, dirname, packageFileName)
    validatePackageYaml(dir, packageYamlFile)

loadRegistry('incubator')
loadRegistry('production')
loadRegistry('enterprise')

with open("packages.yaml", "w") as outfile:
  yaml.dump(allPackages, outfile, default_flow_style=False)

print(str(len(allPackages)) + " packages loaded")
