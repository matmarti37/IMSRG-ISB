ulimit -s unlimited
         
nudel f_180011.trl
nudel f_180011.lnz
nudel f_180011.tmp
nudel f_180011.lev
nudel f_180111.trl
nudel f_180111.lnz
nudel f_180111.tmp
nudel f_180111.lev
nudel f_180211.trl
nudel f_180211.lnz
nudel f_180211.tmp
nudel f_180211.lev
nudel f_180311.trl
nudel f_180311.lnz
nudel f_180311.tmp
nudel f_180311.lev
nudel f_180411.trl
nudel f_180411.lnz
nudel f_180411.tmp
nudel f_180411.lev
         
nuaddint f_180xy.addint f_180.int f_180.ant
nucp  f_180.ppar p.par
nucp  f_180.npar n.par
nudel as.op
nudel bs.op
nudel s.oph

nudel f_180sl.inf
NuShellX < f_180.modelx > f_180mod.out
NuShellX < f_180.levelx > f_180lev.out
source shellx.bat > f_180.cpu
nuren shellx.bat shellx1.bat
nucp  xy1200.lph f_180011.eng f_180.modelx f_180.levelx xy1200.lpe > nucp.txt
nuren f_180011.lp xy1200.lp
nuren f_180011.ls xy1200.ls
nuren f_180011.nhw xy1200.nhw
nucp  xy1202.lph f_180111.eng f_180.modelx f_180.levelx xy1202.lpe > nucp.txt
nuren f_180111.lp xy1202.lp
nuren f_180111.ls xy1202.ls
nuren f_180111.nhw xy1202.nhw
nucp  xy1204.lph f_180211.eng f_180.modelx f_180.levelx xy1204.lpe > nucp.txt
nuren f_180211.lp xy1204.lp
nuren f_180211.ls xy1204.ls
nuren f_180211.nhw xy1204.nhw
nucp  xy1206.lph f_180311.eng f_180.modelx f_180.levelx xy1206.lpe > nucp.txt
nuren f_180311.lp xy1206.lp
nuren f_180311.ls xy1206.ls
nuren f_180311.nhw xy1206.nhw
nucp  xy1208.lph f_180411.eng f_180.modelx f_180.levelx xy1208.lpe > nucp.txt
nuren f_180411.lp xy1208.lp
nuren f_180411.ls xy1208.ls
nuren f_180411.nhw xy1208.nhw
         
nudel f_181011.trl
nudel f_181011.lnz
nudel f_181011.tmp
nudel f_181011.lev
nudel f_181111.trl
nudel f_181111.lnz
nudel f_181111.tmp
nudel f_181111.lev
nudel f_181211.trl
nudel f_181211.lnz
nudel f_181211.tmp
nudel f_181211.lev
nudel f_181311.trl
nudel f_181311.lnz
nudel f_181311.tmp
nudel f_181311.lev
nudel f_181411.trl
nudel f_181411.lnz
nudel f_181411.tmp
nudel f_181411.lev
         
nuaddint f_181xy.addint f_181.int f_181.ant
nucp  f_181.ppar p.par
nucp  f_181.npar n.par
nudel as.op
nudel bs.op
nudel s.oph

nudel f_181sl.inf
NuShellX < f_181.modelx > f_181mod.out
NuShellX < f_181.levelx > f_181lev.out
source shellx.bat > f_181.cpu
nuren shellx.bat shellx1.bat
nucp  xy1210.lph f_181011.eng f_181.modelx f_181.levelx xy1210.lpe > nucp.txt
nuren f_181011.lp xy1210.lp
nuren f_181011.ls xy1210.ls
nuren f_181011.nhw xy1210.nhw
nucp  xy1212.lph f_181111.eng f_181.modelx f_181.levelx xy1212.lpe > nucp.txt
nuren f_181111.lp xy1212.lp
nuren f_181111.ls xy1212.ls
nuren f_181111.nhw xy1212.nhw
nucp  xy1214.lph f_181211.eng f_181.modelx f_181.levelx xy1214.lpe > nucp.txt
nuren f_181211.lp xy1214.lp
nuren f_181211.ls xy1214.ls
nuren f_181211.nhw xy1214.nhw
nucp  xy1216.lph f_181311.eng f_181.modelx f_181.levelx xy1216.lpe > nucp.txt
nuren f_181311.lp xy1216.lp
nuren f_181311.ls xy1216.ls
nuren f_181311.nhw xy1216.nhw
nucp  xy1218.lph f_181411.eng f_181.modelx f_181.levelx xy1218.lpe > nucp.txt
nuren f_181411.lp xy1218.lp
nuren f_181411.ls xy1218.ls
nuren f_181411.nhw xy1218.nhw
nulev f_18y     
levp f_18y     
ulimit -s unlimited
         
nudel o_180020.trl
nudel o_180020.lnz
nudel o_180020.tmp
nudel o_180020.lev
nudel o_180120.trl
nudel o_180120.lnz
nudel o_180120.tmp
nudel o_180120.lev
nudel o_180220.trl
nudel o_180220.lnz
nudel o_180220.tmp
nudel o_180220.lev
nudel o_180320.trl
nudel o_180320.lnz
nudel o_180320.tmp
nudel o_180320.lev
nudel o_180420.trl
nudel o_180420.lnz
nudel o_180420.tmp
nudel o_180420.lev
         
nuaddint o_180xy.addint o_180.int o_180.ant
nucp  o_180.ppar p.par
nucp  o_180.npar n.par
nudel as.op
nudel bs.op
nudel s.oph
nudel o_180sl.inf
NuShellX < o_180.modelx > o_180mod.out
NuShellX < o_180.levelx > o_180lev.out
nucp nul > opd.dat
source shellx.bat > o_180.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  xy0200.lph o_180020.eng o_180.modelx o_180.levelx xy0200.lpe > nucp.txt
nuren o_180020.lp xy0200.lp
nuren o_180020.ls xy0200.ls
nuren o_180020.nhw xy0200.nhw
nucp  xy0202.lph o_180120.eng o_180.modelx o_180.levelx xy0202.lpe > nucp.txt
nuren o_180120.lp xy0202.lp
nuren o_180120.ls xy0202.ls
nuren o_180120.nhw xy0202.nhw
nucp  xy0204.lph o_180220.eng o_180.modelx o_180.levelx xy0204.lpe > nucp.txt
nuren o_180220.lp xy0204.lp
nuren o_180220.ls xy0204.ls
nuren o_180220.nhw xy0204.nhw
nucp  xy0206.lph o_180320.eng o_180.modelx o_180.levelx xy0206.lpe > nucp.txt
nuren o_180320.lp xy0206.lp
nuren o_180320.ls xy0206.ls
nuren o_180320.nhw xy0206.nhw
nucp  xy0208.lph o_180420.eng o_180.modelx o_180.levelx xy0208.lpe > nucp.txt
nuren o_180420.lp xy0208.lp
nuren o_180420.ls xy0208.ls
nuren o_180420.nhw xy0208.nhw
         
nudel o_181020.trl
nudel o_181020.lnz
nudel o_181020.tmp
nudel o_181020.lev
nudel o_181120.trl
nudel o_181120.lnz
nudel o_181120.tmp
nudel o_181120.lev
nudel o_181220.trl
nudel o_181220.lnz
nudel o_181220.tmp
nudel o_181220.lev
nudel o_181320.trl
nudel o_181320.lnz
nudel o_181320.tmp
nudel o_181320.lev
nudel o_181420.trl
nudel o_181420.lnz
nudel o_181420.tmp
nudel o_181420.lev
         
nuaddint o_181xy.addint o_181.int o_181.ant
nucp  o_181.ppar p.par
nucp  o_181.npar n.par
nudel as.op
nudel bs.op
nudel s.oph
nudel o_181sl.inf
NuShellX < o_181.modelx > o_181mod.out
NuShellX < o_181.levelx > o_181lev.out
nucp nul > opd.dat
source shellx.bat > o_181.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  xy0210.lph o_181020.eng o_181.modelx o_181.levelx xy0210.lpe > nucp.txt
nuren o_181020.lp xy0210.lp
nuren o_181020.ls xy0210.ls
nuren o_181020.nhw xy0210.nhw
nucp  xy0212.lph o_181120.eng o_181.modelx o_181.levelx xy0212.lpe > nucp.txt
nuren o_181120.lp xy0212.lp
nuren o_181120.ls xy0212.ls
nuren o_181120.nhw xy0212.nhw
nucp  xy0214.lph o_181220.eng o_181.modelx o_181.levelx xy0214.lpe > nucp.txt
nuren o_181220.lp xy0214.lp
nuren o_181220.ls xy0214.ls
nuren o_181220.nhw xy0214.nhw
nucp  xy0216.lph o_181320.eng o_181.modelx o_181.levelx xy0216.lpe > nucp.txt
nuren o_181320.lp xy0216.lp
nuren o_181320.ls xy0216.ls
nuren o_181320.nhw xy0216.nhw
nucp  xy0218.lph o_181420.eng o_181.modelx o_181.levelx xy0218.lpe > nucp.txt
nuren o_181420.lp xy0218.lp
nuren o_181420.ls xy0218.ls
nuren o_181420.nhw xy0218.nhw
nulev o_18y     
levp o_18y     
ulimit -s unlimited
         
nudel ne180002.trl
nudel ne180002.lnz
nudel ne180002.tmp
nudel ne180002.lev
nudel ne180102.trl
nudel ne180102.lnz
nudel ne180102.tmp
nudel ne180102.lev
nudel ne180202.trl
nudel ne180202.lnz
nudel ne180202.tmp
nudel ne180202.lev
nudel ne180302.trl
nudel ne180302.lnz
nudel ne180302.tmp
nudel ne180302.lev
nudel ne180402.trl
nudel ne180402.lnz
nudel ne180402.tmp
nudel ne180402.lev
         
nuaddint ne180xy.addint ne180.int ne180.ant
nucp  ne180.ppar p.par
nucp  ne180.npar n.par
nudel as.op
nudel bs.op
nudel s.oph
nudel ne180sl.inf
NuShellX < ne180.modelx > ne180mod.out
NuShellX < ne180.levelx > ne180lev.out
nucp nul > opd.dat
source shellx.bat > ne180.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  xy2200.lph ne180002.eng ne180.modelx ne180.levelx xy2200.lpe > nucp.txt
nuren ne180002.lp xy2200.lp
nuren ne180002.ls xy2200.ls
nuren ne180002.nhw xy2200.nhw
nucp  xy2202.lph ne180102.eng ne180.modelx ne180.levelx xy2202.lpe > nucp.txt
nuren ne180102.lp xy2202.lp
nuren ne180102.ls xy2202.ls
nuren ne180102.nhw xy2202.nhw
nucp  xy2204.lph ne180202.eng ne180.modelx ne180.levelx xy2204.lpe > nucp.txt
nuren ne180202.lp xy2204.lp
nuren ne180202.ls xy2204.ls
nuren ne180202.nhw xy2204.nhw
nucp  xy2206.lph ne180302.eng ne180.modelx ne180.levelx xy2206.lpe > nucp.txt
nuren ne180302.lp xy2206.lp
nuren ne180302.ls xy2206.ls
nuren ne180302.nhw xy2206.nhw
nucp  xy2208.lph ne180402.eng ne180.modelx ne180.levelx xy2208.lpe > nucp.txt
nuren ne180402.lp xy2208.lp
nuren ne180402.ls xy2208.ls
nuren ne180402.nhw xy2208.nhw
         
nudel ne181002.trl
nudel ne181002.lnz
nudel ne181002.tmp
nudel ne181002.lev
nudel ne181102.trl
nudel ne181102.lnz
nudel ne181102.tmp
nudel ne181102.lev
nudel ne181202.trl
nudel ne181202.lnz
nudel ne181202.tmp
nudel ne181202.lev
nudel ne181302.trl
nudel ne181302.lnz
nudel ne181302.tmp
nudel ne181302.lev
nudel ne181402.trl
nudel ne181402.lnz
nudel ne181402.tmp
nudel ne181402.lev
         
nuaddint ne181xy.addint ne181.int ne181.ant
nucp  ne181.ppar p.par
nucp  ne181.npar n.par
nudel as.op
nudel bs.op
nudel s.oph
nudel ne181sl.inf
NuShellX < ne181.modelx > ne181mod.out
NuShellX < ne181.levelx > ne181lev.out
nucp nul > opd.dat
source shellx.bat > ne181.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  xy2210.lph ne181002.eng ne181.modelx ne181.levelx xy2210.lpe > nucp.txt
nuren ne181002.lp xy2210.lp
nuren ne181002.ls xy2210.ls
nuren ne181002.nhw xy2210.nhw
nucp  xy2212.lph ne181102.eng ne181.modelx ne181.levelx xy2212.lpe > nucp.txt
nuren ne181102.lp xy2212.lp
nuren ne181102.ls xy2212.ls
nuren ne181102.nhw xy2212.nhw
nucp  xy2214.lph ne181202.eng ne181.modelx ne181.levelx xy2214.lpe > nucp.txt
nuren ne181202.lp xy2214.lp
nuren ne181202.ls xy2214.ls
nuren ne181202.nhw xy2214.nhw
nucp  xy2216.lph ne181302.eng ne181.modelx ne181.levelx xy2216.lpe > nucp.txt
nuren ne181302.lp xy2216.lp
nuren ne181302.ls xy2216.ls
nuren ne181302.nhw xy2216.nhw
nucp  xy2218.lph ne181402.eng ne181.modelx ne181.levelx xy2218.lpe > nucp.txt
nuren ne181402.lp xy2218.lp
nuren ne181402.ls xy2218.ls
nuren ne181402.nhw xy2218.nhw
nulev ne18y     
levp ne18y     
