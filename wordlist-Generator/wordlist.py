#!/usr/bin/python
import itertools 
import time
import sys


info = '''
                              
######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################

#######################################################################
# High Speed Wordlist Generator : Compitable To All Operating Systems #
#######################################################################
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
usages Example:>>
        Please Enter Here All Word for combination :>> ABCabc123';./
        please enter here lengh of words :>>4
        please enetr here name of Wordlist :>>>pass.txt
**********************************************************************
**********************************************************************
'''
print info
print ""
chrs=raw_input("[+] Please Enter Here All Word for combination :>> ")
print ""
l=int(raw_input("[+] Please Enter Minimum Lenth Of Words  : >>  "))
k = l
print ""
j=int(raw_input("[+] Please Enter Maximum Lenth Of Words  : >>  "))
n = j+1
print ""
mtl=len(chrs)
p=[]
zt = raw_input("[+] Please Enetr Here Name Of Wordlist File :>>> ")
for ltp in xrange(k, n):
	ans=mtl**ltp
	p.append(ans)
tline=sum(p)
print "[+] Numbers Of Total Lines : ", tline
raw_input('[+] Are You Ready ?[Press Enter]')

print "\n\n+++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++++++++++++++++++\n \n"
time1=time.asctime()
start=time.time()

psd = open(zt, 'a')
for i in xrange(k,n):
  r=i*100/n
  l=str(r)+' percent '
  sys.stdout.write("\r%s" % l)
  sys.stdout.flush()
  psd.flush()
  for xs in itertools.product(chrs, repeat=i):
    psd.write(''.join(xs)+'\n')
psd.flush()    
psd.close()
sys.stdout.write("\rDone Sucessfully")
print '\n\n+++++++++++++++++++++++++ Process Report +++++++++++++++++++++++++++++++++++++\n'
print '\t [+] Process Started                      :   ', time1
end=time.time()
print '\t [+] Process Completed                    :   ', time.asctime()
totaltime=end-start
print '\t [+] Total Time Consumed                  :   ', totaltime, 'second'
rate=tline/totaltime
print '\t [+] Rate Of Words Generating Per Seconds :   ', rate 

print '\n+++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++++++++++++++++++'

print '''
\t***************************************************
\t*       Successfully created thanks for using     *
\t***************************************************

'''
print ""
raw_input("[*] Press Enter For Exit")
