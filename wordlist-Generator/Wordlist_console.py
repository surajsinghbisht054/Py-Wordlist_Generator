#!/usr/bin/python
import itertools 
import time
import sys
import optparse as th
parser=th.OptionParser()
parser.add_option('-m', dest="max", type='int', help=" For Selecting Maximum Numbers")
parser.add_option('-n', dest="min",  type='int', help=" For Selecting Minimum Numbers")
parser.add_option('-o', dest="output", default="pass.txt", type='string', help=" For Selecting Output Path")
parser.add_option('-w', dest="word", default="0123456789", type='string', help=" For Selecting All Alphabet And Numbers ")

option, remainder=parser.parse_args()


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

usages>>
      Example:
-m   maximum lengh
-n    minimum lenght
-w    all word for combination
-o    output

***************************************************************
***************************************************************
'''
print info

chrs=option.word
l=option.min
k = l
j=option.max
n = j+1
mtl=len(chrs)
p=[]
zt =option.output
for ltp in xrange(k, n):
	ans=mtl**ltp
	p.append(ans)
tline=sum(p)
print "Numbers Of Total Lines : ", tline
raw_input('Are You Ready ?[Press Enter]')

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
psd = open(zt, 'r')
psd1=psd.read()
j=psd1.count('\n')
try:
    rate=j/totaltime
except:
    rate=800000
print '\t [+] Rate Of Words Generating Per Seconds :   ', rate 

print "\t [+] Total Available lines                :   ", j
print '\n+++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++++++++++++++++++'
psd.close()
print '''
\t***************************************************
\t*       Successfully created thanks for using     *
\t***************************************************

'''


