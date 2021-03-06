# coding: utf-8
import sys
import multiprocessing 
import os
import numpy as np


param =sys.argv
n=int(param[1])
m=int(param[2])
MDset=param[3]


#情報収集フェイズ
f=open("./cfiles/"+MDset+"/pbsa_info")
x=f.readlines()

start= str(x[0].split()[-1])
stop= str(x[1].split()[-1])
offset=1


# for test only

# for test only


os.mkdir("./Confene")
os.chdir("./Confene")

while n <= m:

# name define fo DXX
    if n < 10:
        DXX="D0%s" %(n)
    else:
        DXX="D%s" %(n)



    def prep():
        os.makedirs(DXX + "//PDB//MOL2")
        os.chdir(DXX + "/PDB")

        try:
            x=open("conf.in","a")

            x.write("trajin ../../../MMPBSA_am1/" + DXX + "/PBSA/lig.mdcrd " + str(start) + " " + str(stop) + " " + str(offset) + " \n")
            x.write("trajout ./CONF.pdb start 1 offset 1 multi pdb \n")
            x.write("go")
            x.close()
        except:
            print"Sorry, the file is not exist"

        try:
            os.system("cpptraj ../../../MMPBSA_am1/" + DXX + "/PBSA/lig.top ./conf.in")
        except:
            print "cpptraj error"


        for n in range(1, int(stop)+1):
            try:
                os.rename("CONF.pdb."+ str(n),"CONF."+str(n) +".pdb")
                os.system("molcharge -method gasteiger -in CONF."+ str(n) +".pdb"+" -out ./MOL2/CONF"+ str(n) + ".mol2")
            except:
                print "molcharge error"

        os.chdir("./MOL2")




    def main(number):
        os.system("freeform -calc conf -useInput3D -in CONF" + str(number) +".mol2 -prefix " +str(number) + " " )



    def abst():
        y=open("../../TdS_Estr.dat","a")
        y.write("TdS, Estr, \n")


        TdS=[]
        Estr=[]
        for n in range(1,int(stop)+1):
            z=open( str(n) + ".log","r")

            for line in z.readlines():
                if "Input3D min at confidx" in line:
                    #writing
                    result=line.split()
                    tds=result[14]
                    estr=result[17]
                    y.write( tds  + "  " + estr + ", \n")

                    #for calc
                    TdS.append(float(tds.rstrip(',')))
                    Estr.append(float(estr))

            z.close()

        
        y.write("Average:  TdS= "+ str(np.average(TdS)) + "   Estr= " +str(np.average(Estr))+ "\n")
        y.write("STD:  TdS= "+ str(np.std(TdS)) + "   Estr= " +str(np.std(Estr))+ "\n")
        y.close()


        
        
        
        
        
   
        
        
    if os.path.exists("../structs/"+DXX+".mol2"): 
        print "Hello world"
        prep()
                
        p = multiprocessing.Pool(6)
        p.map(main, xrange(1,int(stop)+1))
        print "freeform finished"

        
        abst()
        
        
        #fin
        os.chdir("../../..")
    
    else:
        print "Sorry %s not found" %(DXX)

    n += 1

os.chdir("..")
