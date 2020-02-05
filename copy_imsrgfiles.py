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
                # Creates a new file for a reference state if it doesn't exist and then goes into that file
                filehead = Int+"/A"+str(A)+"/Ref"+str(A)+str(element)+"_e"+str(e)
                if not os.path.exists(filehead):
                    os.makedirs(filehead)
                os.chdir(filehead)

                # Copies the imsrg files from ~/imsrg/work/scripts/output to the current directory and renames them
                os.system("rm *")
                os.system("cp ~/imsrg/work/scripts/output/**"+str(element)+str(A)+"_e"+str(e)+"* .")
                os.system("rm BCH*")
                os.system("mv *1b.op Fermi_1b.op")
                os.system("mv *2b.op Fermi_2b.op")
                os.system("mv *Iso2.int Iso2.int")
                os.system("mv *Rn2.int Rn2.int")
                os.system("mv *Rp2.int Rp2.int")
                os.system("mv *VCoul.int VCoul.int")

                os.system("mv *"+str(A)+".int imsrg.int")
                os.system("mv *.sp imsrg.sp")

                # Changes back to the parent directory
                os.chdir("../../..")
