#usr/bin/python2
#color
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;36m'
W='\033[0;37m'
W1='\033[1;37m'

# import module
import os,sys,time,marshal,base64

# banner
banner = '''
%s
                                  _ __
   ___  __ _________  __ _  ___  (_) /__
  / _ \/ // / __/ _ \/  ' \/ _ \/ / / -_)
%s / .__/\_, /\__/\___/_/_/_/ .__/_/_/\__/
/_/   /___/              /_/%s
__________________________________________________
| %s[-] Autor : M.Luqman.Arief                     %s|
| %s[-] Team  : X-Garuda_Red                       %s|
| %s[-] GT    : https://github.com/AriefDev        %s|
|________________________________________________|
''' % (Y,R,G,B,G,B,G,B,G)

def clear():
	os.system('clear')
clear()
print banner

def menu():
	print '''
%s(%s01%s)%s.Marhsal
%s(%s02%s)%s.Base64
%s(%s03%s)%s.About
%s(%s04%s)%s.More Tools
%s(%s05%s)%s.Exit/Close
''' % (R,G,R,W1,R,G,R,W1,R,G,R,W1,R,G,R,W1,R,G,R,W1)
	print ('')
	while True:
		menu  = raw_input('%s[%schoose%s]%s >> ' % (R,G,R,W))
		if menu == '1' or menu == '01':
			Marshal()
		elif menu == '2' or menu == '02':
			_base64()
		elif menu == '3' or menu == '03':
			About()
		elif menu == '4' or menu == '04':
			os.system('xdg-open "https://www.github.com/AriefDev"')
		elif menu == '5' or menu == '05':
			print  '%s[%s*%s]%s Exit..' % (R,G,R,W)
			sys.exit()
		elif menu == '':
			pass
		else:
			print  '%s[%s*%s]%s Wrong Input' % (R,G,R,W)




# compile using marshal
def Marshal():
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		file = raw_input('%s[%soutput/file%s]%s >> ' % (R,G,R,W))
		baca = open(file,'r').read()
		com = compile(baca,'','exec')
		encrypt = marshal.dumps(com)
		new_file = open('out/_'+str(file),'w')
		sc = '''
# code by: M.Luqman.Arief
# Team   : X-Garuda_Red
# Github : https://www.github.com/AriefDev/
# Facebook : https://www.facebook.com/profile.php?id=100055134992811
'''
		new_file.write(sc)
		new_file.write('import marshal\n')
		new_file.write('exec(marshal.loads('+repr(encrypt)+'))')
		new_file.close()
		print '%s[%s*%s]%s done file saved out/_' % (R,G,R,W)+str(file)

	except OSError:
		pass
	except IOError,e:
		print  '%s[%s*%s]%s ' % (R,G,R,W),e
	except TypeError,e:
		print '%s[%s*%s]%s ' % (R,G,R,W),e



# compile using base64
def _base64():
	file_name = raw_input("%s[%soutput/file%s]%s >> " % (R,G,R,W))
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
        	file = open("%s" % (file_name),'r')
	        encrypt = base64.b64encode(file.read())
	        file = open("out/_"+str(file_name),"w")
	        sc = '''
# code by: M.Luqman.Arief
# Team   : X-Garuda_Red
# Github : https://www.github.com/AriefDev/
# Facebook : https://www.facebook.com/profile.php?id=100055134992811
'''
		file.write(sc)
	        file.write("import base64\n")
        	ash = "'"
	        file.write("result = %s %s %s \n"% (ash,encrypt,ash))
        	file.write("eval(compile(base64.b64decode(result),'<string>','exec'))\n")
	        file.close()
		print '%s[%s*%s]%s file saved out/_' % (R,G,R,W)+str(file_name)
	except IOError,e:
		print '%s[%s*%s]%s ' % (R,G,R,W),e
	except TypeError,e:
		print '%s[%s*%s]%s ' % (R,G,R,W),e

# about
def About():
	print '''
___________________________________________________________________
Autor    : M.Luqman.Arief
Team     : X-Garuda_Red
Github   : https://www.github.com/AriefDev
Facebook : https://www.facebook.com/profile.php?id=100055134992811
Email    : ariefdev79@gmail.com
___________________________________________________________________
'''
menu()































