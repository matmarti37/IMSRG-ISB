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
                os.system("bash runshell.sh")
                os.chdir("../../..")
