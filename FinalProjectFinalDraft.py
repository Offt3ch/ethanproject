import tkinter as tk
from tkinter import messagebox
import time
import random
from playsound import playsound
from multiprocessing import Process

sel = 0;
sel1 = 0;
sel2 = 0;

def menu1():
    root=tk.Tk() 
    RockButton = tk.Button(root, text='Rock Music', command=rock, fg = 'white', bg = 'black').pack()
    PopButton = tk.Button(root, text='Pop Music', command=pop,fg='white', bg='blue').pack()
       
    quit_button = tk.Button(root, text='Quit', fg='white', bg='red',command=root.destroy),pack()
    root.mainloop()

def rock(self):
    global variable
    sel = 1;
    root1 = tk.Tk()
    RockMajorButton = tk.Button(root1, text='Major', command=rockmajor, fg='black', bg='white').pack()
    RockMinorButton = tk.Button(root1, text='Minor', command=rockminor, fg='black', bg='white').pack()
    RockGoBack = tk.Button(root1, text='Go Back',command=root1.destroy)
    root1.mainloop()
    
def pop(self):
    global variable
    sel = 2
    root2 = tk.Tk()
    PopMajorButton = tk.Button(root2, text='Major', command=popmajor, fg='black', bg='white').pack()
    PopMinorButton = tk.Button(root2, text='Minor', command=popminor, fg='black', bg='white').pack()
    PopGoBackButton = tk.Button(root2, text='Go Back',command=root2.destroy).pack()
    root2.mainloop()
    
def rockmajor(self):
    global variable
    sel1 = 1
    root3 = tk.Tk()
    EButton = tk.Button(root3, text='E', command=Egui, fg='black', bg='white').pack()
    FButton = tk.Button(root3, text='F', command=Fgui, fg='black', bg='white').pack()
    FsButton = tk.Button(root3, text='F Sharp or G Flat', command=Fsgui, fg='black', bg='white').pack()
    GButton = tk.Button(root3, text='G', command=Ggui, fg='black', bg='white').pack()
    GsButton = tk.Button(root3, text='G Sharp or A Flat', command=Gsgui, fg='black', bg='white').pack()
    AButton = tk.Button(root3, text='A', command=Agui, fg='black', bg='white').pack()
    AsButton = tk.Button(root3, text='A Sharp or B Flat', command=Asgui, fg='black', bg='white').pack()
    BButton = tk.Button(root3, text='B', command=Bgui, fg='black', bg='white').pack()
    CButton = tk.Button(root3, text='C', command=Cgui, fg='black', bg='white').pack()
    CsButton = tk.Button(root3, text='C Sharp or D Flat', command=Csgui, fg='black', bg='white').pack()
    DButton = tk.Button(root3, text='D', command=Dgui, fg='black', bg='white').pack()
    DsButton = tk.Button(root3, text='D Sharp or E Flat', command=Dsgui, fg='black', bg='white').pack()
    RockMajorScaleGoBackButton = tk.Button(root3, text='Go Back',command=root3.destroy).pack()
    root3.mainloop()
        
def rockminor(self):
    global variable
    sel1 = 2
    root4 = tk.Tk()
    EButton = tk.Button(root4, text='E', command=Egui, fg='black', bg='white').pack()
    FButton = tk.Button(root4, text='F', command=Fgui, fg='black', bg='white').pack()
    FsButton = tk.Button(root4, text='F Sharp or G Flat', command=Fsgui, fg='black', bg='white').pack()
    GButton = tk.Button(root4, text='G', command=Ggui, fg='black', bg='white').pack()
    GsButton = tk.Button(root4, text='G Sharp or A Flat', command=Gsgui, fg='black', bg='white').pack()
    AButton = tk.Button(root4, text='A', command=Agui, fg='black', bg='white').pack()
    AsButton = tk.Button(root4, text='A Sharp or B Flat', command=Asgui, fg='black', bg='white').pack()
    BButton = tk.Button(root4, text='B', command=Bgui, fg='black', bg='white').pack()
    CButton = tk.Button(root4, text='C', command=Cgui, fg='black', bg='white').pack()
    CsButton = tk.Button(root4, text='C Sharp or D Flat', command=Csgui, fg='black', bg='white').pack()
    DButton = tk.Button(root4, text='D', command=Dgui, fg='black', bg='white').pack()
    DsButton = tk.Button(root4, text='D Sharp or E Flat', command=Dsgui, fg='black', bg='white').pack()
    RockMinorScaleGoBackButton = tk.Button(root4, text='Go Back',command=root4.destroy).pack()
    root4.mainloop()
 
        
def popmajor(self):
    global variable
    sel1 = 1
    root5 = tk.Tk()
    EButton = tk.Button(root5, text='E', command=Egui, fg='black', bg='white').pack()
    FButton = tk.Button(root5, text='F', command=Fgui, fg='black', bg='white').pack()
    FsButton = tk.Button(root5, text='F Sharp or G Flat', command=Fsgui, fg='black', bg='white').pack()
    GButton = tk.Button(root5, text='G', command=Ggui, fg='black', bg='white').pack()
    GsButton = tk.Button(root5, text='G Sharp or A Flat', command=Gsgui, fg='black', bg='white').pack()
    AButton = tk.Button(root5, text='A', command=Agui, fg='black', bg='white').pack()
    AsButton = tk.Button(root5, text='A Sharp or B Flat', command=Asgui, fg='black', bg='white').pack()
    BButton = tk.Button(root5, text='B', command=Bgui, fg='black', bg='white').pack()
    CButton = tk.Button(root5, text='C', command=Cgui, fg='black', bg='white').pack()
    CsButton = tk.Button(root5, text='C Sharp or D Flat', command=Csgui, fg='black', bg='white').pack()
    DButton = tk.Button(root5, text='D', command=Dgui, fg='black', bg='white').pack()
    DsButton = tk.Button(root5, text='D Sharp or E Flat', command=Dsgui, fg='black', bg='white').pack()
    PopMajorGoBackButton = tk.Button(root5, text='Go Back',command=root5.destroy).pack()
    root5.mainloop()
    
    
def popminor(self):
    global variable
    sel1 = 2
    root6 = tk.Tk()
    EButton = tk.Button(root6, text='E', command=Egui, fg='black', bg='white').pack()
    FButton = tk.Button(root6, text='F', command=Fgui, fg='black', bg='white').pack()
    FsButton = tk.Button(root6, text='F Sharp or G Flat', command=Fsgui, fg='black', bg='white').pack()
    GButton = tk.Button(root6, text='G', command=Ggui, fg='black', bg='white').pack()
    GsButton = tk.Button(root6, text='G Sharp or A Flat', command=Gsgui, fg='black', bg='white').pack()
    AButton = tk.Button(root6, text='A', command=Agui, fg='black', bg='white').pack()
    AsButton = tk.Button(root6, text='A Sharp or B Flat', command=Asgui, fg='black', bg='white').pack()
    BButton = tk.Button(root6, text='B', command=Bgui, fg='black', bg='white').pack()
    CButton = tk.Button(root6, text='C', command=Cgui, fg='black', bg='white').pack()
    CsButton = tk.Button(root6, text='C Sharp or D Flat', command=Csgui, fg='black', bg='white').pack()
    DButton = tk.Button(root6, text='D', command=Dgui, fg='black', bg='white').pack()
    DsButton = tk.Button(root6, text='D Sharp or E Flat', command=Dsgui, fg='black', bg='white').pack()
    PopMinorGoBackButton = tk.Button(root6, text='Go Back',command=root6.destroy).pack()
    root6.mainloop()
            
    def Egui(self):
        global variable
        sel2 = 1
    
    def Fgui(self):
        global variable
        sel2 = 2

    def Fsgui(self):
        global variable
        sel2 = 3
     
    def Ggui(self):
        global variable
        sel2 = 4
    
    def Gsgui(self):
        global variable
        sel2 = 5
  
    def Agui(self):
        global variable
        sel2 = 6

    def Asgui(self):
        global variable
        sel2 = 7
    
    def Bgui(self):
        global variable
        sel2 = 8
  
    def Cgui(self):
        global variable
        sel2 = 9
    
    def Csgui(self):
        global variable
        sel2 = 10
    
    def Dgui(self):
        global variable
        sel2 = 11
        
    def Dsgui(self):
        global variable
        sel2 = 12
      
def e():
    pe1 = './pe1.wav';
    pe2 = './pe2.wav';
    pe3 = './pe3.wav';
    pe4 = './pe4.wav';

    re1 = './re1.wav';
    re2 = './re2.wav';
    re3 = './re3.wav';
    re4 = './re4.wav';
    pope = [pe1,pe2,pe3,pe4];
    rocke = [re1,re2,re3,re4];
    
    return pope, rocke;

def f():
    pf1 = './pf1.wav';
    pf2 = './pf2.wav';
    pf3 = './pf3.wav';
    pf4 = './pf4.wav';
    
    rf1 = './rf1.wav';
    rf2 = './rf2.wav';
    rf3 = './rf3.wav';
    rf4 = './rf4.wav';
    
    popf = [pf1,pf2,pf3,pf4];
    rockf = [rf1,rf2,rf3,rf4];
    
    return popf, rockf;

def fsharp():
    pfs1 = './pfs1.wav';
    pfs2 = './pfs2.wav';
    pfs3 = './pfs3.wav';
    pfs4 = './pfs4.wav';
    
    rfs1 = './rfs1.wav';
    rfs2 = './rfs2.wav';
    rfs3 = './rfs3.wav';
    rfs4 = './rfs4.wav';
    
    popfs = [pfs1,pfs2,pfs3,pfs4];
    rockfs = [rfs1,rfs2,rfs3,rfs4];
    
    return popfs, rockfs;

def g():
    pg1 = './pg1.wav';
    pg2 = './pg2.wav';
    pg3 = './pg3.wav';
    pg4 = './pg4.wav';
    
    rg1 = './rg1.wav';
    rg2 = './rg2.wav';
    rg3 = './rg3.wav';
    rg4 = './rg4.wav';
    
    popg = [pg1,pg2,pg3,pg4];
    rockg = [rg1,rg2,rg3,rg4];
    
    return popg, rockg;
    
def gsharp():
    pgs1 = './pgs1.wav';
    pgs2 = './pgs2.wav';
    pgs3 = './pgs3.wav';
    pgs4 = './pgs4.wav';
    
    rgs1 = './rgs1.wav';
    rgs2 = './rgs2.wav';
    rgs3 = './rgs3.wav';
    rgs4 = './rgs4.wav';
    
    popgs = [pgs1,pgs2,pgs3,pgs4];
    rockgs = [rgs1,rgs2,rgs3,rgs4];
    
    return popgs, rockgs;

def a():
    pa1 = './pa1.wav';
    pa2 = './pa2.wav';
    pa3 = './pa3.wav';
    pa4 = './pa4.wav';

    ra1 = './ra1.wav';
    ra2 = './ra2.wav';
    ra3 = './ra3.wav';
    ra4 = './ra4.wav';
    
    popa = [pa1,pa2,pa3,pa4];
    rocka = [ra1,ra2,ra3,ra4];
    
    return popa, rocka;
    
def asharp():
    pas1 = './pas1.wav';
    pas2 = './pas2.wav';
    pas3 = './pas3.wav';
    pas4 = './pas4.wav';

    ras1 = './ras1.wav';
    ras2 = './ras2.wav';
    ras3 = './ras3.wav';
    ras4 = './ras4.wav';
    
    popas = [pas1,pas2,pas3,pas4];
    rockas = [ras1,ras2,ras3,ras4];
    
    return popas, rockas;

def b():
    pb1 = './pb1.wav';
    pb2 = './pb2.wav';
    pb3 = './pb3.wav';
    pb4 = './pb4.wav';
    
    rb1 = './rb1.wav';
    rb2 = './rb2.wav';
    rb3 = './rb3.wav';
    rb4 = './rb4.wav';
    
    popb = [pb1,pb2,pb3,pb4];
    rockb = [rb1,rb2,rb3,rb4];
    
    return popb, rockb;
    
def c():   
    pc1 = './pc1.wav';
    pc2 = './pc2.wav';
    pc3 = './pc3.wav';
    pc4 = './pc4.wav';
    
    rc1 = './rc1.wav';
    rc2 = './rc2.wav';
    rc3 = './rc3.wav';
    rc4 = './rc4.wav';
    
    popc = [pc1,pc2,pc3,pc4];
    rockc = [rc1,rc2,rc3,rc4];
    
    return popc, rockc;

def csharp():
    pcs1 = './pcs1.wav';
    pcs2 = './pcs2.wav';
    pcs3 = './pcs3.wav';
    pcs4 = './pcs4.wav';
    
    rcs1 = './rcs1.wav';
    rcs2 = './rcs2.wav';
    rcs3 = './rcs3.wav';
    rcs4 = './rcs4.wav';
    
    popcs = [pcs1,pcs2,pcs3,pcs4];
    rockcs = [rcs1,rcs2,rcs3,rcs4];
    
    return popcs, rockcs;

def d():
    pd1 = './pd1.wav';
    pd2 = './pd2.wav';
    pd3 = './pd3.wav';
    pd4 = './pd4.wav';
    
    rd1 = './rd1.wav';
    rd2 = './rd2.wav';
    rd3 = './rd3.wav';
    rd4 = './rd4.wav';

    popd = [pd1,pd2,pd3,pd4];
    rockd = [rd1,rd2,rd3,rd4];
    
    return popd, rockd;
    
def dsharp():
    pds1 = './pds1.wav';
    pds2 = './pds2.wav';
    pds3 = './pds3.wav';
    
    rds1 = './rds1.wav';
    rds2 = './rds2.wav';
    rds3 = './rds3.wav';

    popds = [pds1,pds2,pds3];
    rockds = [rds1,rds2,rds3];
    
    return popds, rockds;
    
def scale():
    scale = [];
    
    if sel == 1 and sel1 == 1 and sel2 == 1: #Rock Major E
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
        
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 1: # Rock Minor E
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
        
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 2: #Rock Major F
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
        
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 2: #Rock Minor F
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
        
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 3: #Rock Major Fs
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
        
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 3: #Rock Minor Fs
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
        
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 4: #Rock Major G
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
        
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 4: #Rock Minor G
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
        
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
    
    elif sel == 1 and sel1 == 1 and sel2 == 5: #Rock Major Gs
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
        
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 5: #Rock Minor Gs
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
        
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 6: #Rock Major A
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
        
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 6: #Rock Minor A
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
        
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 7: #Rock Major As
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
        
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 7: #Rock Minor As
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
        
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 8: #Rock Major B
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
        
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 8: #Rock Minor B
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
        
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 9: #Rock Major C
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
        
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 9: #Rock Minor C
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
        
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 10: #Rock Major Cs
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
        
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 10: #Rock Minor Cs
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
        
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
            
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 11: #Rock Major D
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
        
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 11: #Rock Minor D
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
        for n in range(0,len(rocke),1):
            scale.append(rocke[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
        
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
            
        for n in range(0,len(rocka),1):
            scale.append(rocka[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
    elif sel == 1 and sel1 == 1 and sel2 == 12: #Rock Major Ds
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockg),1):
            scale.append(rockg[n]);
        
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockc),1):
            scale.append(rockc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(rockd[n]);
            
    elif sel == 1 and sel1 == 2 and sel2 == 12: #Rock Minor Ds
        for n in range(0,len(rockds),1):
            scale.append(rockds[n]);
            
        for n in range(0,len(rockf),1):
            scale.append(rockf[n]);
            
        for n in range(0,len(rockfs),1):
            scale.append(rockfs[n]);
        
        for n in range(0,len(rockgs),1):
            scale.append(rockgs[n]);
            
        for n in range(0,len(rockas),1):
            scale.append(rockas[n]);
            
        for n in range(0,len(rockb),1):
            scale.append(rockb[n]);
            
        for n in range(0,len(rockcs),1):
            scale.append(rockcs[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 1: #Pop Major E
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
        
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 1: # Pop Minor E
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
        
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 2: #pop Major F
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
        
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 2: #pop Minor F
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
        
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 3: #pop Major Fs
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
        
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 3: #pop Minor Fs
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
        
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 4: #pop Major G
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
        
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(rockd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 4: #pop Minor G
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
        
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
    
    elif sel == 2 and sel1 == 1 and sel2 == 5: #pop Major Gs
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
        
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 5: #pop Minor Gs
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
        
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 6: #pop Major A
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
        
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 6: #pop Minor A
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
        
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 7: #pop Major As
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
        
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 7: #pop Minor As
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
        
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 8: #pop Major B
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
        
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 8: #pop Minor B
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
        
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 9: #pop Major C
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
        
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 9: #pop Minor C
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
        
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 10: #pop Major Cs
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
        
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 10: #pop Minor Cs
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
        
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
            
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 11: #pop Major D
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
        
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 11: #pop Minor D
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
        for n in range(0,len(pope),1):
            scale.append(pope[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
        
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
            
        for n in range(0,len(popa),1):
            scale.append(popa[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
    elif sel == 2 and sel1 == 1 and sel2 == 12: #pop Major Ds
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popg),1):
            scale.append(popg[n]);
        
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popc),1):
            scale.append(popc[n]);
            
        for n in range(0,len(popd),1):
            scale.append(popd[n]);
            
    elif sel == 2 and sel1 == 2 and sel2 == 12: #pop Minor Ds
        for n in range(0,len(popds),1):
            scale.append(popds[n]);
            
        for n in range(0,len(popf),1):
            scale.append(popf[n]);
            
        for n in range(0,len(popfs),1):
            scale.append(popfs[n]);
        
        for n in range(0,len(popgs),1):
            scale.append(popgs[n]);
            
        for n in range(0,len(popas),1):
            scale.append(popas[n]);
            
        for n in range(0,len(popb),1):
            scale.append(popb[n]);
            
        for n in range(0,len(popcs),1):
            scale.append(popcs[n]);
            
    return scale;
 
def sound():
    t_end = time.time() + 60;
    while time.time() < t_end:
        for n in range(0,len(sca),1):
            playtime = random.randint(0,1);
            rannumerator = random.randint(1,8);
            denominator = 8;
            fraction = rannumerator/denominator;
            playtime = playtime + fraction
            note = random.randint(1,len(sca));
            playnote = sca[note-1];
        playsound(playnote);
    
    return playtime;

    

pope, rocke = e();
popf, rockf = f();
popfs, rockfs = fsharp();
popg, rockg = g();
popgs, rockgs = gsharp();
popa, rocka = a();
popas, rockas = asharp();
popb, rockb = b();
popc, rockc = c();
popcs, rockcs = csharp();
popd, rockd = d();
popds, rockds = dsharp();
sca = scale();
play = sound();

if __name__ == "__main__":
    print('here');
    p = Process(target=sound);
    p.start();
    time.sleep(play);
    p.terminate();