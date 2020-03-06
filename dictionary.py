import os

def get_operator(filename):
    file = open(filename)
    data = file.readlines()
    for line in data:
        line = line[:-1]
        line = line.split(" ")
        line = [x for x in line if x != ""]
        if len(line) != 10:
            continue
        if line[0] == "0.0" and line[2] == "0.0":
            return(str(line[9]))

def get_transition(filename):
    file = open(filename)
    data = file.readlines()
    for line in data:
        line = line[:-1]
        line = line.split(" ")
        line = [x for x in line if x != ""]
        if len(line) != 9:
            continue
        if line[0] == "0.0" and line[2] == "0.0":
            return(str(line[8]))

def get_energy(filename):
    imsrg_file = open("imsrg.int")
    imsrg_data = imsrg_file.readlines()
    imsrg_zerobody = float(imsrg_data[4][18:].replace(" ",""))

    file = open(filename)
    data = file.readlines()
    for line in data:
        line = line[:-1]
        line = line.split(" ")
        line = [x for x in line if x != ""]
        if len(line) != 9:
            continue
        if line[1] == "1" and line[4] == "0":
            return(float(line[2])+float(imsrg_zerobody))

def imme_coefficients(T1,T0,Tm1):
    b = 500 * (T1 - Tm1)
    c = 500 * (T1 + Tm1 - 2*T0)
    return(b,c)

elist = [10]
Interactions = ["EM"]
Alist = [10,14,18,22,26,30,34]
refs = ["T1","T0","Tm1"]
values = ["BE","VCoul","Rp2","Rn2","Iso2"]

ELEM = ['n','H','He','Li','Be','B','C','N',
       'O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K',
       'Ca','Sc','Ti','V','Cr','Mn','Fe','Co',  'Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y',
       'Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In',  'Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb',
       'Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb']# ,'Bi','Po','At','Rn','Fr','Ra','Ac','Th','U','Np','Pu']

dict = {}
#   Parameters: int, A, emax, reference, value (BE, VCoul, Rp2, Rn2, Iso2)
tran = {}
#   ParametersL int, A, emax, reference, value (Tr1 vs Tr2)

for Int in Interactions:
    dict[Int] = {}
    tran[Int] = {}
    for e in elist:
        dict[Int][e] = {}
        tran[Int][e] = {}
        for A in Alist:
            dict[Int][e][A] = {}
            tran[Int][e][A] = {}
            ELES = [ELEM[int(A/2-1)],ELEM[int(A/2)],ELEM[int(A/2+1)]]
            ele = [0,0,0]
            i=0
            for i in range(0,3):
                if len(ELES[i]) == 1:
                    ele[i] = ELES[i].lower()+"_"
                if len(ELES[i]) == 2:
                    ele[i] = ELES[i].lower()
            for element in ELES:
                filepath = Int+"/A"+str(A)+"/Ref"+str(A)+str(element)+"_e"+str(e)
                os.chdir(filepath)
                ref_index = ELES.index(element)
                reference = refs[ref_index]
                dict[Int][e][A][reference] = {}
                tran[Int][e][A][reference] = {}


                TR1 = float(get_transition("nutbar_tensor0_"+str(ele[1])+str(A)+"0.dat"))
                TR12= TR1**2
                TR1 = 1 - 0.5*TR12
                TR2 = float(get_transition("nutbar_tensor0_"+str(ele[0])+str(A)+"0.dat"))
                TR22= TR2**2
                TR2 = 1 - 0.5*TR22
                tran[Int][e][A][reference]["TR1"] = TR1
                tran[Int][e][A][reference]["TR2"] = TR2

                for state in ele:
                    dict[Int][e][A][reference][state] = {}
                    dict[Int][e][A][reference][state]["BE"] = get_energy(str(state)+str(A)+"y.lpt")
                    dict[Int][e][A][reference][state]["VCoul"] = get_operator("nutbar_scalar0_"+str(state)+str(A)+"0.dat")
                    dict[Int][e][A][reference][state]["Rp2"] = get_operator("nutbar_scalar1_"+str(state)+str(A)+"0.dat")
                    dict[Int][e][A][reference][state]["Rn2"] = get_operator("nutbar_scalar2_"+str(state)+str(A)+"0.dat")
                    dict[Int][e][A][reference][state]["Iso2"] = get_operator("nutbar_scalar3_"+str(state)+str(A)+"0.dat")
                    #dict[Int][e][A][reference][state] = [BE,VCoul,Rp2,Rn2,Iso2]

                os.chdir("../../..")

print(dict["EM"][10][10]["T1"]["b_"]["Iso2"])
