call nusetbab
ulimit -s unlimited

call nuoperb imsrg     > nuoperb.bxt

call nush ansfile   xy0 0e > xy0 0e.cpu
call nufout xy0 0e >nufout.bxt

call nush ansfile   xy2 0e > xy2 0e.cpu
call nufout xy2 0e >nufout.bxt

call nush ansfile   xy4 0e > xy4 0e.cpu
call nufout xy4 0e >nufout.bxt

call nush ansfile   xy6 0e > xy6 0e.cpu
call nufout xy6 0e >nufout.bxt

call nush ansfile   xy8 0e > xy8 0e.cpu
call nufout xy8 0e >nufout.bxt

call nush ansfile   xy0 1e > xy0 1e.cpu
call nufout xy0 1e >nufout.bxt

call nush ansfile   xy2 1e > xy2 1e.cpu
call nufout xy2 1e >nufout.bxt

call nush ansfile   xy4 1e > xy4 1e.cpu
call nufout xy4 1e >nufout.bxt

call nush ansfile   xy6 1e > xy6 1e.cpu
call nufout xy6 1e >nufout.bxt

call nush ansfile   xy8 1e > xy8 1e.cpu
call nufout xy8 1e >nufout.bxt
nulev p_30y     
levp p_30y     
ulimit -s unlimited

call nuoperb imsrg     > nuoperb.bxt

call nush ansfile   xy0 0e > xy0 0e.cpu
call nufout xy0 0e >nufout.bxt

call nush ansfile   xy2 0e > xy2 0e.cpu
call nufout xy2 0e >nufout.bxt

call nush ansfile   xy4 0e > xy4 0e.cpu
call nufout xy4 0e >nufout.bxt

call nush ansfile   xy6 0e > xy6 0e.cpu
call nufout xy6 0e >nufout.bxt

call nush ansfile   xy8 0e > xy8 0e.cpu
call nufout xy8 0e >nufout.bxt

call nush ansfile   xy0 1e > xy0 1e.cpu
call nufout xy0 1e >nufout.bxt

call nush ansfile   xy2 1e > xy2 1e.cpu
call nufout xy2 1e >nufout.bxt

call nush ansfile   xy4 1e > xy4 1e.cpu
call nufout xy4 1e >nufout.bxt

call nush ansfile   xy6 1e > xy6 1e.cpu
call nufout xy6 1e >nufout.bxt

call nush ansfile   xy8 1e > xy8 1e.cpu
call nufout xy8 1e >nufout.bxt
nulev si30y     
levp si30y     
ulimit -s unlimited

call nuoperb imsrg     > nuoperb.bxt

call nush ansfile   xy0 0e > xy0 0e.cpu
call nufout xy0 0e >nufout.bxt

call nush ansfile   xy2 0e > xy2 0e.cpu
call nufout xy2 0e >nufout.bxt

call nush ansfile   xy4 0e > xy4 0e.cpu
call nufout xy4 0e >nufout.bxt

call nush ansfile   xy6 0e > xy6 0e.cpu
call nufout xy6 0e >nufout.bxt

call nush ansfile   xy8 0e > xy8 0e.cpu
call nufout xy8 0e >nufout.bxt

call nush ansfile   xy0 1e > xy0 1e.cpu
call nufout xy0 1e >nufout.bxt

call nush ansfile   xy2 1e > xy2 1e.cpu
call nufout xy2 1e >nufout.bxt

call nush ansfile   xy4 1e > xy4 1e.cpu
call nufout xy4 1e >nufout.bxt

call nush ansfile   xy6 1e > xy6 1e.cpu
call nufout xy6 1e >nufout.bxt

call nush ansfile   xy8 1e > xy8 1e.cpu
call nufout xy8 1e >nufout.bxt
nulev s_30y     
levp s_30y     

call nuend ansfile  
