from pull_values import createlist
from pull_values import createtransitions
import matplotlib.pyplot as plt
title_font = {'fontname':'Arial', 'size':'18', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}
axis_fontx = {'fontname':'Arial', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'top'}
axis_fonty = {'fontname':'Arial', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

A = [10,14,18,22,26,30,34]

##################################
##################################
# Plotting functions
##################################
##################################
def writePreliminary():
	bottom,top = plt.ylim()
	plt.text(8,(bottom+top)/2,'PRELIMINARY',va='center',ha='center',rotation=45,fontsize=50,color='0.8',zorder=1)
	return()
def writeVSIMSRG():
	bottom,top = plt.ylim()
	plt.text(6,bottom+(top-bottom)/10,'VS-IMSRG',va='center',ha='left',fontsize=18)
	return()
def plottitles(titlestring,ylabel,xlabel='$A$',xlow=4,xhigh=40):
	#writePreliminary()
	#writeVSIMSRG()
	plt.xlim(xlow,xhigh)
	plt.title(titlestring,**title_font)
	plt.xlabel(xlabel,**axis_fontx)
	plt.ylabel(ylabel,**axis_fonty)
	plt.legend(loc='upper right',fontsize='medium')
	plt.tight_layout()
	return()
##################################
##################################

##################################
##################################
# This function calls all of the lists
# They are named as REFERENCE_VALUE where
# REFERENCE is in ["T1","T0","Tm1","Ind"] and
# VALUE is in ["BE","VCoul","Rp2","Rn2","Iso2"]
##################################
##################################
def pulllist(Int,ref,val):
    T1,T0,Tm1,B,C = createlist(Int,ref,val)
    list = [T1,T0,Tm1,B,C]
    return(list)

refs = ["T1","T0","Tm1","Ind"]
vals = ["BE","VCoul","Rp2","Rn2","Iso2"]
interactions = ["EM"]
for ref in refs:
    for val in vals:
        for Int in interactions:
            globals()[ref + "_" + val] = pulllist(Int,ref,val)
##################################
##################################

##################################
##################################
# This function creates lists of transitions
# They are the |V|^2, not the delta_C
##################################
##################################
def pulltrans(Int,ref,val):
    Tr1,Tr2 = createtransitions(Int,ref)
    if val == "Tr1":
        return(Tr1)
    if val == "Tr2":
        return(Tr2)

refs = ["T1","T0","Tm1"]
vals = ["Tr1","Tr2"]
interactions = ["EM"]
for ref in refs:
    for val in vals:
        for Int in interactions:
            globals()[ref + "_" + val] = pulltrans(Int,ref,val)
##################################
##################################



##################################
##################################
# This plots the B coefficients of binding energy
##################################
##################################
plt.plot(A,T1_BE[3],color='r',marker='*',label="Ref $T=1$")
plt.plot(A,T0_BE[3],color='g',marker='o',label="Ref $T=0$")
plt.plot(A,Tm1_BE[3],color='b',marker='^',label="Ref $T=-1$")
plt.plot(A,Ind_BE[3],color='k',marker='s',label="Ref Ind.")
titlestring = "IMME $B$ Coefficient"
ylabel = "$B$ Coefficient (keV)"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/BCoefficient_BE.pdf")
#plt.show()
plt.close()
##################################
##################################

##################################
##################################
# This plots the C coefficients of binding energy
##################################
##################################
plt.plot(A,T1_BE[4],color='r',marker='*',label="Ref $T=1$")
plt.plot(A,T0_BE[4],color='g',marker='o',label="Ref $T=0$")
plt.plot(A,Tm1_BE[4],color='b',marker='^',label="Ref $T=-1$")
plt.plot(A,Ind_BE[4],color='k',marker='s',label="Ref Ind.")
titlestring = "IMME $C$ Coefficient"
ylabel = "$C$ Coefficient (keV)"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/CCoefficient_BE.pdf")
#plt.show()
plt.close()
##################################
##################################

##################################
##################################
# This plots the B and C coefficients without VCoul
##################################
##################################
# Creates lists for the differences
T1_B_noCoul = []
T0_B_noCoul = []
Tm1_B_noCoul= []
Ind_B_noCoul= []

T1_C_noCoul = []
T0_C_noCoul = []
Tm1_C_noCoul= []
Ind_C_noCoul= []
i = 0
while i < len(A):
    T1_B_noCoul.extend([T1_BE[3][i] - T1_VCoul[3][i]])
    T0_B_noCoul.extend([T0_BE[3][i] - T0_VCoul[3][i]])
    Tm1_B_noCoul.extend([Tm1_BE[3][i] - Tm1_VCoul[3][i]])
    Ind_B_noCoul.extend([Ind_BE[3][i] - Ind_VCoul[3][i]])

    T1_C_noCoul.extend([T1_BE[4][i] - T1_VCoul[4][i]])
    T0_C_noCoul.extend([T0_BE[4][i] - T0_VCoul[4][i]])
    Tm1_C_noCoul.extend([Tm1_BE[4][i] - Tm1_VCoul[4][i]])
    Ind_C_noCoul.extend([Ind_BE[4][i] - Ind_VCoul[4][i]])
    i = i+1

# Does the plotting
plt.plot(A,T1_B_noCoul,color='r',marker='*',label="Ref $T=1$")
plt.plot(A,T0_B_noCoul,color='g',marker='o',label="Ref $T=0$")
plt.plot(A,Tm1_B_noCoul,color='b',marker='^',label="Ref $T=-1$")
plt.plot(A,Ind_B_noCoul,color='k',marker='s',label="Ref Ind.")
titlestring = "IMME $B$ Coefficient"
ylabel = "$B$ Coefficient (keV)"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/BCoefficient_BE_NoCoul.pdf")
#plt.show()
plt.close()

plt.plot(A,T1_C_noCoul,color='r',marker='*',label="Ref $T=1$")
plt.plot(A,T0_C_noCoul,color='g',marker='o',label="Ref $T=0$")
plt.plot(A,Tm1_C_noCoul,color='b',marker='^',label="Ref $T=-1$")
plt.plot(A,Ind_C_noCoul,color='k',marker='s',label="Ref Ind.")
titlestring = "IMME $C$ Coefficient"
ylabel = "$C$ Coefficient (keV)"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/CCoefficient_BE_NoCoul.pdf")
#plt.show()
plt.close()
##################################
##################################

##################################
##################################
# This plots delta_C for the first transition (Tm1->T0)
##################################
##################################
plt.plot(A,T1_Tr1,color='r',marker='*',label="Ref $T=1$")
plt.plot(A,T0_Tr1,color='g',marker='o',label="Ref $T=0$")
plt.plot(A,Tm1_Tr1,color='b',marker='^',label="Ref $T=-1$")
titlestring = "$\delta_C$ for $T_z=-1$ to $T_z=0$ Transition"
ylabel = "$\delta_C$"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/Delta_C_Tr1.pdf")
#plt.show()
plt.close()
##################################
##################################

##################################
##################################
# This plots delta_C for the second transition (T0->T1)
##################################
##################################
plt.plot(A,T1_Tr2,color='r',marker='*',label="Ref $T=1$")
plt.plot(A,T0_Tr2,color='g',marker='o',label="Ref $T=0$")
plt.plot(A,Tm1_Tr2,color='b',marker='^',label="Ref $T=-1$")
titlestring = "$\delta_C$ for $T_z=0$ to $T_z=1$ Transition"
ylabel = "$\delta_C$"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/Delta_C_Tr2.pdf")
#plt.show()
plt.close()
##################################
##################################

##################################
##################################
# This plots delta_C for the both transition (Tm1->T0->T1)
##################################
##################################
plt.plot(A,T1_Tr1,color='r',marker='*',label="Tr1 - Ref $T=1$")
plt.plot(A,T0_Tr1,color='g',marker='o',label="Tr1 - Ref $T=0$")
plt.plot(A,Tm1_Tr1,color='b',marker='^',label="Tr1 - Ref $T=-1$")
plt.plot(A,T1_Tr2,'--',color='r',marker='*',label="Tr2 - Ref $T=1$")
plt.plot(A,T0_Tr2,'--',color='g',marker='o',label="Tr2 - Ref $T=0$")
plt.plot(A,Tm1_Tr2,'--',color='b',marker='^',label="Tr2 - Ref $T=-1$")
titlestring = "$\delta_C$ for $T_z=-1$ to $T_z=0$ to $T_z=1$ Transitions"
ylabel = "$\delta_C$"
plottitles(titlestring,ylabel)
plt.savefig("./Plots/Delta_C_Both.pdf")
#plt.show()
plt.close()
##################################
##################################
