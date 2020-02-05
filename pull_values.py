import os

# Scalar 0: VCoul
# Scalar 1: Rp2
# Scalar 2: Rn2
# Scalar 3: Iso2
# Tensor 0: Tz=-1 -> Tz=0
# Tensor 1: Tz=0 -> Tz=1

elist = [10]
Alist = [10,14,18,22,26,30,34]

ELEM = ['n','H','He','Li','Be','B','C','N',
       'O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K',
       'Ca','Sc','Ti','V','Cr','Mn','Fe','Co',  'Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y',
       'Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In',  'Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb',
       'Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb']# ,'Bi','Po','At','Rn','Fr','Ra','Ac','Th','U','Np','Pu']

# Function to extract the operator value from the files
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
# Function to extract transition matrix elements
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
# Function to extract the binding energies
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

def mass_calculator(energy,A,element):
    Z = int(ELEM.index(element))
    N = int(A - Z)
    mass = (energy + Z*mP + N*mN)*1e6
    massA = mass/amuFactor
    DmA = massA - A
    DmK = DmA*amuFactor*1e-3
    #return(DmK) # Returns mass excess in MeV
    return(energy) # Returns binding energy (as given, just to keep it simple)

def imme_coefficients(T1,T0,Tm1):
    b = 500 * (T1 - Tm1)
    c = 500 * (T1 + Tm1 - 2*T0)
    return(b,c)

# Dictionary to store the data
dictionary = {}
trdict = {}
interactions = ["EM"]

# Loops through all files and fills the dictionary
for A in Alist:
    A = int(A)
    ELES = [ELEM[int(A/2-1)],ELEM[int(A/2)],ELEM[int(A/2+1)]]

    # Creates a new element list in the format for nutbar
    ele = [0,0,0]
    i=0
    for i in range(0,3):
        if len(ELES[i]) == 1:
            ele[i] = ELES[i].lower()+"_"
        if len(ELES[i]) == 2:
            ele[i] = ELES[i].lower()

    for element in ELES:
        for e in elist:
            for Int in interactions:
                # Moves into the nushell/nutbar file
                filehead = Int+"/A"+str(A)+"/Ref"+str(A)+str(element)+"_e"+str(e)
                os.chdir(filehead)

                # Creates a dictionary element for a reference state
                reference = Int+"/Ref"+str(A)+str(element)+"_e"+str(e)
                dictionary[reference] = {}
                # Calls the get_operator value for each operator and stores them in a list
                i=0
                for state in ele:
                    BE = get_energy(str(state)+str(A)+"y.lpt")
                    VCoul = get_operator("nutbar_scalar0_"+str(state)+str(A)+"0.dat")
                    Rp2 = get_operator("nutbar_scalar1_"+str(state)+str(A)+"0.dat")
                    Rn2 = get_operator("nutbar_scalar2_"+str(state)+str(A)+"0.dat")
                    Iso2 = get_operator("nutbar_scalar3_"+str(state)+str(A)+"0.dat")
                    dictionary[reference][ELES[i]] = [BE,VCoul,Rp2,Rn2,Iso2]
                    i = i + 1

                    TR1 = float(get_transition("nutbar_tensor0_"+str(ele[1])+str(A)+"0.dat"))
                    TR12= TR1**2
                    TR1 = 1 - 0.5*TR12
                    TR2 = float(get_transition("nutbar_tensor0_"+str(ele[0])+str(A)+"0.dat"))
                    TR22= TR2**2
                    TR2 = 1 - 0.5*TR22
                    trdict[reference] = [TR1,TR2]
                os.chdir("../../..")

# At this point I have the dictionary created and it is now extracting to the right lists (i.e. sorting)
mN = 939.5654133
mP = 938.2720813
amuFactor = 9.314940954e8

# This creates lists with the same value for various reference states as well as B and C coefficients
# Call with T1_listname,T0_listname,Tm1_listname,B_listname,C_listname = createlist("Reference","Value")
def createlist(Int,ref,value):
    e = elist[0]
    T1 = []
    T0 = []
    Tm1= []
    B  = []
    C  = []

    # Gives an index for the reference state
    refs = ["T1","T0","Tm1","Ind"]
    ref_index = refs.index(ref)

    # Gives an index for what I want to extract
    values = ["BE","VCoul","Rp2","Rn2","Iso2"]
    value_index = int(values.index(value))

    # This does the individual reference state - because they're all different
    if ref_index == 3:
        for A in Alist:
            ELES = [ELEM[int(A/2-1)],ELEM[int(A/2)],ELEM[int(A/2+1)]]
            T1.extend([dictionary[Int+"/Ref"+str(A)+str(ELES[0])+"_e"+str(e)][ELES[0]][value_index]])
            T0.extend([dictionary[Int+"/Ref"+str(A)+str(ELES[1])+"_e"+str(e)][ELES[1]][value_index]])
            Tm1.extend([dictionary[Int+"/Ref"+str(A)+str(ELES[2])+"_e"+str(e)][ELES[2]][value_index]])
    # This does the reference states
    else:
        for A in Alist:
            ELES = [ELEM[int(A/2-1)],ELEM[int(A/2)],ELEM[int(A/2+1)]]
            T1.extend([dictionary[Int+"/Ref"+str(A)+str(ELES[ref_index])+"_e"+str(e)][ELES[0]][value_index]])
            T0.extend([dictionary[Int+"/Ref"+str(A)+str(ELES[ref_index])+"_e"+str(e)][ELES[1]][value_index]])
            Tm1.extend([dictionary[Int+"/Ref"+str(A)+str(ELES[ref_index])+"_e"+str(e)][ELES[2]][value_index]])

    i = 0
    while i < len(T1):
        b,c = imme_coefficients(float(T1[i]),float(T0[i]),float(Tm1[i]))
        B.extend([b])
        C.extend([c])
        i = i+1


    return(T1,T0,Tm1,B,C)

# This performs the same function as createlists but for the transitions
def createtransitions(Int,ref):
    Tr1 = []
    Tr2 = []

    refs = ["T1","T0","Tm1"]
    ref_index = refs.index(ref)

    for A in Alist:
        ELES = [ELEM[int(A/2-1)],ELEM[int(A/2)],ELEM[int(A/2+1)]]
        Tr1.extend([trdict[Int+"/Ref"+str(A)+str(ELES[ref_index])+"_e"+str(e)][0]])
        Tr2.extend([trdict[Int+"/Ref"+str(A)+str(ELES[ref_index])+"_e"+str(e)][1]])

    return(Tr1,Tr2)
