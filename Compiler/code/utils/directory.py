#Este modulo contiene los path de input y output, el de input es el path del archivo de cool que se va a compilar y el outut es el nombre del archivo de mips
#donde se va a guardar el resultado de compilar el input.

input_path = r'C:\Users\David\Documents\Version del compilador de Rayniel 9 de junio\Compiler\input\life.cl'
output_path = r'C:\Users\David\Documents\Version del compilador de Rayniel 9 de junio\Compiler\output\life1.s'



#import os
#from pathlib import Path, PureWindowsPath


#def standar(s ):
#  filename = PureWindowsPath(s)
#  correct_path = Path(filename)
#  return correct_path


#r_directory = os.getcwd()
#r_directory = PureWindowsPath(r_directory)

#directory = PureWindowsPath((r_directory.parent).parent)

#print(str(directory))
#first = 0
#second = 0
#for i in range(len(r_directory)):
#  if r_directory[i] == "\\" :
#    second = first
 #   first = i
#directory = ""
#for i in range(len(r_directory)):
#  if i> second:
#    break
#  directory += r_directory[i]
#current_directory = PureWindowsPath(r'' +  str(directory) + r'input\current_directory.txt')
#with open(current_directory) as file:
#  name_cl = file.read(1024)
#name_spim = r''
#for i in range(len(name_cl)):
#  if name_cl[i] == '.':
#    break
#  name_spim+= name_cl[i]
#name_spim = name_spim + r'.s'
#current_cl = Path(r'' + str(directory) + r'test\test_case' + '\\' + name_cl)
#output_cl = Path(r'' + directory + r'output' + '\\' + name_spim)

#current_cl = standar(current_cl)
#output_cl = standar(output_cl)
#directory = standar(directory)
#current_directory = standar(current_directory)