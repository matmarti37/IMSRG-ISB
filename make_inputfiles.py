import os

interactions = ["EM"]
elist = [10]
Alist = [10,14,18,22,26,30,34]

ELEM = ['n','H','He','Li','Be','B','C','N',
       'O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K',
       'Ca','Sc','Ti','V','Cr','Mn','Fe','Co',  'Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y',
       'Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In',  'Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb',
       'Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb']# ,'Bi','Po','At','Rn','Fr','Ra','Ac','Th','U','Np','Pu']

for Int in interactions:
    for A in Alist:
            A = int(A)
            ELES = [ELEM[int(A/2-1)],ELEM[int(A/2)],ELEM[int(A/2+1)]]
            for element in ELES:
                for e in elist:
                    # Changes directory
                    filehead = Int+"/A"+str(A)+"/Ref"+str(A)+str(element)+"_e"+str(e)
                    os.chdir(filehead)

                    # Creates a .ans file for shell
                    anstext = "-\nlpe\nimsrg\nn\nimsrg\n"+str(ELEM.index(ELES[1]))+"\n"+str(A)+"\n0,4,1\n2\n-\nlpe\nimsrg\nn\nimsrg\n"+str(ELEM.index(ELES[0]))+"\n"+str(A)+"\n0,4,1\n2\n-\nlpe\nimsrg\nn\nimsrg\n"+str(ELEM.index(ELES[2]))+"\n"+str(A)+"\n0,4,1\n2\n-\nst"
                    os.system("touch ansfile.ans")
                    ansfile = open("ansfile.ans","w")
                    ansfile.write(anstext)

                    # Creates a new element list in the format for nutbar
                    ele = [0,0,0]
                    i=0
                    for i in range(0,3):
                        if len(ELES[i]) == 1:
                            ele[i] = ELES[i].lower()+"_"
                        if len(ELES[i]) == 2:
                            ele[i] = ELES[i].lower()

                    # Create the nutbar input files
                    nutin = [0,0,0]
                    i=0
                    for i in range(0,3):
                        nutin[i] = "imsrg\n"+str(ele[i])+str(A)+"0\n"+str(ele[i])+str(A)+"0\nVCoul.int Rp2.int Rn2.int Iso2.int\n0 1\n2 2\n0 1\n2 2"
                    transin = [0,0]
                    i=0
                    for i in range(0,2):
                        transin[i] = "imsrg\n"+str(ele[i+1])+str(A)+"0\n"+str(ele[i])+str(A)+"0\nFermi_1b.op Fermi_2b.op\n0 1\n2 2\n0 1\n2 2"

                    os.system("touch input0.input")
                    os.system("touch input1.input")
                    os.system("touch input2.input")
                    os.system("touch transin0.input")
                    os.system("touch transin1.input")

                    input0 = open("input0.input","w")
                    input0.write(nutin[0])

                    input1 = open("input1.input","w")
                    input1.write(nutin[1])

                    input2 = open("input2.input","w")
                    input2.write(nutin[2])

                    transin0 = open("transin0.input","w")
                    transin0.write(transin[0])

                    transin1 = open("transin1.input","w")
                    transin1.write(transin[1])

                    # Copies the runshell bash script into directory and goes back to parent
                    os.system("cp ../../../runshell.sh .")
                    os.chdir("../../..")
