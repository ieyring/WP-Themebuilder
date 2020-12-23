import os
import sys, getopt

class generator:
  theme = ''

  def __init__(self,themename):
    self.theme = themename

  def createBase(self):
    if not os.path.exists(self.theme):
      os.makedirs(theme)
      os.makedirs(theme+"/css")
      os.makedirs(theme+"/fonts")
      os.makedirs(theme+"/js")
      os.makedirs(theme+"/template-parts")
      f = open(theme+"/style.css","w+")
      mystring = '''/*
      Template Name: 
      Theme Name: %s Template
      Theme URI: https://e-si.de
      Description: Theme für %s
      Author: Ingo Eyring
      Author URI: https://e-si.de
      */
      .hide {display: none}
      '''
      f.write(mystring.format(theme,theme))
      f.close()




def main (argv):
    theme = ''
    try:
        opts, args = getopt.getopt(argv,"t:")
    except getopt.GetoptError:
      print('createwptheme.py -t <themename>')
      sys.exit(2)    
    for opt, arg in opts:
      if opt == '-t':
         print('build theme: ',arg)
         theme = arg
      else:
        print('No Themename found: createwptheme.py -t <themename>')

    if theme != '':
        


if __name__ == "__main__":
   main(sys.argv[1:])
   