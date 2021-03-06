# coding: utf-8


import wx
import os
import glob




#Original ID list
#measure
ID_MAINFRAME= wx.NewId()
ID_RADIOBUTTON_1= wx.NewId()
ID_RADIOBUTTON_3= wx.NewId()
ID_COMBOBOX_START= wx.NewId()
ID_COMBOBOX_END= wx.NewId()
ID_COMBOBOX_MD= wx.NewId()
ID_COMBOBOX_RECEPTOR= wx.NewId()
ID_COMBOBOX_EXPIMP= wx.NewId()

radiolist=[ID_RADIOBUTTON_1,ID_RADIOBUTTON_3]



class MainFrm(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self,None,ID_MAINFRAME,"MMPBSA_GUI",size=(450,400))
        
        #statusbar
        self.CreateStatusBar()
        self.SetStatusText("[GUI_MMPBSA ver_1.24]")

        #mainframe
        rootWindow= wx.SplitterWindow(self,wx.ID_ANY,style=wx.SP_3D)
        rootPanel_1= ConfigPanel(rootWindow)
        rootPanel_2= ButtonPanel(rootWindow)
        rootWindow.SplitVertically(rootPanel_1,rootPanel_2,300)
        
                
        self.Centre()
        self.Show()
        
        
def Processing():
    target= wx.FindWindowById(ID_MAINFRAME)
    target.SetStatusText("Now Processing... ... ...")
        
        
def ProcessingEnd():
    target= wx.FindWindowById(ID_MAINFRAME)
    target.SetStatusText("[GUI_MMPBSA ver_1.04]")



            

class ConfigPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,wx.ID_ANY)
        
        #Flagの都合上存在するsizer
        baseSizer=wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(baseSizer)
        
        #メインのsizer
        configbox=wx.StaticBox(self,wx.ID_ANY,"[CONFIG]")
        configLayout= wx.StaticBoxSizer(configbox,wx.VERTICAL)
        baseSizer.Add(configLayout,flag=wx.EXPAND|wx.ALL,border=5)
        
        
        #すきま埋め
        configLayout.Add(wx.Size(350,10))
        configLayout.Add(wx.StaticText(configbox,wx.ID_ANY," [Measurement]"))
        
        
        
        #計測回数
        panel_repeat= wx.Panel(configbox,wx.ID_ANY)
        layout_repeat=wx.BoxSizer(wx.HORIZONTAL)
        panel_repeat.SetSizer(layout_repeat)
        
        layout_repeat.Add(wx.Size(10,10))
        layout_repeat.Add(wx.RadioButton(panel_repeat,ID_RADIOBUTTON_1,"1"))
        layout_repeat.Add(wx.Size(20,10))
        layout_repeat.Add(wx.RadioButton(panel_repeat,ID_RADIOBUTTON_3,"3"))
        
        configLayout.Add(panel_repeat,flag=wx.EXPAND)
        configLayout.Add(wx.Size(350,10))
        
        
        
        #タンパクの指定
        reclist=os.listdir('./md1/input_info')
        
        panel_Rec= wx.Panel(configbox,wx.ID_ANY)
        layout_Rec= wx.BoxSizer(wx.HORIZONTAL)
        panel_Rec.SetSizer(layout_Rec)
        
        comboBox_Rec=wx.ComboBox(panel_Rec,ID_COMBOBOX_RECEPTOR,choices=reclist,style=wx.CB_READONLY)
        
        layout_Rec.Add(wx.StaticText(panel_Rec,wx.ID_ANY," [Receptor]"))
        layout_Rec.Add(wx.Size(50,10))        
        layout_Rec.Add(comboBox_Rec)
        
        configLayout.Add(panel_Rec)
        configLayout.Add(wx.Size(350,20))
        
        
        
        
        #start & end
        #スマートに要素を取得
        compounds=[r.split('/')[-1].split(".")[0] for r in glob.glob('./md1/structs/*.mol2')]
        
        
        
        panel_DXX=wx.Panel(configbox,wx.ID_ANY)
        layout_DXX=wx.BoxSizer(wx.HORIZONTAL)
        panel_DXX.SetSizer(layout_DXX)
        
        comboBox_Start=wx.ComboBox(panel_DXX,ID_COMBOBOX_START,choices=sorted(compounds),style=wx.CB_READONLY)
        comboBox_End=wx.ComboBox(panel_DXX,ID_COMBOBOX_END,choices=sorted(compounds)[::-1],style=wx.CB_READONLY)
        
        layout_DXX.Add(wx.StaticText(panel_DXX,wx.ID_ANY," [Start]"))
        layout_DXX.Add(wx.Size(5,10))        
        layout_DXX.Add(comboBox_Start)
        layout_DXX.Add(wx.Size(20,10))
        layout_DXX.Add(wx.StaticText(panel_DXX,wx.ID_ANY," [End]"))
        layout_DXX.Add(wx.Size(5,10))
        layout_DXX.Add(comboBox_End)
        
        configLayout.Add(panel_DXX)
        configLayout.Add(wx.Size(350,20))
        
        
        
        
        
     
        #MD
        setlist=os.listdir('./md1/cfiles')
        
        panel_MD= wx.Panel(configbox,wx.ID_ANY)
        layout_MD= wx.BoxSizer(wx.HORIZONTAL)
        panel_MD.SetSizer(layout_MD)
        
        comboBox_MD=wx.ComboBox(panel_MD,ID_COMBOBOX_MD,choices=setlist,style=wx.CB_READONLY)
        
        layout_MD.Add(wx.StaticText(panel_MD,wx.ID_ANY," [MD]"))
        layout_MD.Add(wx.Size(25,10))        
        layout_MD.Add(comboBox_MD)
        
        configLayout.Add(panel_MD)
        configLayout.Add(wx.Size(350,20))
        
        
        
    
        
        
        
        
        
        
class ButtonPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,wx.ID_ANY)
        
        buttonLayout= wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(buttonLayout)
        
        
        
        button_RENAME= wx.Button(self,wx.ID_ANY,"Convert_SDF")
        button_Prep_MD= wx.Button(self,wx.ID_ANY,"Prep_MD")
        button_Run_MD= wx.Button(self,wx.ID_ANY,"Run_MD")
        button_MMPBSA= wx.Button(self,wx.ID_ANY,"MMPBSA")
        button_Analysis= wx.Button(self,wx.ID_ANY,"Analysis")
        button_Run_ALL= wx.Button(self,wx.ID_ANY,"RUN_ALL")
        
        
        button_RENAME.Bind(wx.EVT_BUTTON,self.Rename)
        button_Prep_MD.Bind(wx.EVT_BUTTON,self.Prep)
        button_Run_MD.Bind(wx.EVT_BUTTON,self.Run_MD)
        button_MMPBSA.Bind(wx.EVT_BUTTON,self.MMPBSA)
        button_Analysis.Bind(wx.EVT_BUTTON,self.Analysis)
        button_Run_ALL.Bind(wx.EVT_BUTTON,self.Run_All)
        
        
        
        buttonLayout.Add(wx.Size(150,5))
        buttonLayout.Add(wx.StaticText(self,wx.ID_ANY,"[START]"),flag=wx.EXPAND)
        buttonLayout.Add(wx.Size(150,5))
        buttonLayout.Add(button_RENAME,flag=wx.EXPAND)
        buttonLayout.Add(wx.Size(150,5),flag=wx.EXPAND)
        buttonLayout.Add(button_Prep_MD,flag=wx.EXPAND)
        buttonLayout.Add(button_Run_MD,flag=wx.EXPAND)
        buttonLayout.Add(button_MMPBSA,flag=wx.EXPAND)
        buttonLayout.Add(button_Analysis,flag=wx.EXPAND)
        buttonLayout.Add(wx.Size(150,20))
        buttonLayout.Add(button_Run_ALL,flag=wx.EXPAND)
        
        
        

        
        
    def OnClick(self,event):
        Run().Testmode()
        
        
    def Rename(self,event):
        Run().Rename()

    def Prep(self,event):
        Run().Prep()
        
    def Run_MD(self,event):
        Run().Run_MD()
        
    def MMPBSA(self,event):
        Run().MMPBSA()
        
    def Analysis(self,event):
        Run().Analysis()
        
    def Run_All(self,event):
        Run().Run_All()

        
        
        
        
        
        
class GetVar:
    
    def __init__(self):
        self.cmmc="No country for old men"
        
    def Measure(self):
        for i in radiolist:
            target=wx.FindWindowById(i)
            if target.GetValue() == True:
                return target.GetLabel().encode('utf-8')
    
    def Receptor(self):
        target= wx.FindWindowById(ID_COMBOBOX_RECEPTOR)
        return target.GetValue()
    
    
    def Start(self):
        target=wx.FindWindowById(ID_COMBOBOX_START)
        return target.GetValue()
    
    def Start_n(self):
        target=wx.FindWindowById(ID_COMBOBOX_START).GetValue()
        return str(int(target[1:3]))
        
        
    def End(self):
        target=wx.FindWindowById(ID_COMBOBOX_END)
        return target.GetValue()
    
    def End_m(self):
        target=wx.FindWindowById(ID_COMBOBOX_END).GetValue()
        return str(int(target[1:3]))
        
        
        
        
    def MD(self):
        target=wx.FindWindowById(ID_COMBOBOX_MD)
        return target.GetValue()
        
    def Water(self):
        target=wx.FindWindowById(ID_COMBOBOX_MD)
        return target.GetValue()[0:3]
   

        


    
    
        
class Run():
    
    def __init__(self):
        self.repeat= GetVar().Measure()
        self.receptor= GetVar().Receptor()
        self.start= GetVar().Start_n()
        self.stop= GetVar().End_m()
        self.MDset= GetVar().MD()
        self.water= GetVar().Water()
        
        
    def Testmode(self):
        print self.repeat,self.receptor, self.start, self.stop, self.MDset
        
        

    def Rename(self):
        Processing()
        os.system("python2.7 ./system/convert.py")
        ProcessingEnd()
        
    def Prep(self):
        Processing()
        os.system("python2.7 ./system/prep5.0.py "+ self.start+" "+self.stop+" "+self.receptor+" "+self.water)
        ProcessingEnd()
        
    def Run_MD(self):
        Processing()
        os.system("python2.7 ./system/copydir.py "+self.repeat)
        os.system("python2.7 ./system/md.py "+self.start+" "+self.stop+" "+ self.MDset+" "+self.repeat)
        ProcessingEnd()
        
        
    def MMPBSA(self):
        Processing()
        os.system("python2.7 ./system/prep_mmpbsa.py "+self.start+" "+self.stop+" "+ self.MDset+" "+self.repeat+" "+self.receptor)
        os.system("python2.7 ./system/run_mmpbsa.py "+self.start+" "+self.stop+" "+ self.MDset+" "+self.repeat+" "+self.receptor)
        os.system("python2.7 ./system/CONF.py "+self.start+" "+self.stop+" "+self.MDset+" "+self.repeat)
        ProcessingEnd()
            
        
    def Analysis(self):
        Processing()
        os.system("python2.7 ./system/analyze.py "+self.repeat)
        os.system("python2.7 ./system/decomp.py "+self.start+" "+self.stop+" "+self.MDset+" "+self.repeat+" "+self.receptor)
        os.system("python2.7 ./system/mol2depict.py "+self.start+" "+self.stop)
        os.system("python2.7 ./system/report.py ")
        ProcessingEnd()
        
        
    def Run_All(self):
        Processing()
        os.system("python2.7 ./system/prep5.0.py "+ self.start+" "+self.stop+" "+self.receptor+" "+self.water)
        
        os.system("python2.7 ./system/copydir.py "+self.repeat)
        os.system("python2.7 ./system/md.py "+self.start+" "+self.stop+" "+ self.MDset+" "+self.repeat)
        
        os.system("python2.7 ./system/prep_mmpbsa.py "+self.start+" "+self.stop+" "+ self.MDset+" "+self.repeat+" "+self.receptor)
        os.system("python2.7 ./system/run_mmpbsa.py "+self.start+" "+self.stop+" "+ self.MDset+" "+self.repeat+" "+self.receptor)
        os.system("python2.7 ./system/CONF.py "+self.start+" "+self.stop+" "+self.MDset+" "+self.repeat)
        
        os.system("python2.7 ./system/analyze.py "+self.repeat)
        os.system("python2.7 ./system/decomp.py "+self.start+" "+self.stop+" "+self.MDset+" "+self.repeat+" "+self.receptor)
        os.system("python2.7 ./system/mol2depict.py "+self.start+" "+self.stop)
        os.system("python2.7 ./system/report.py ")
        ProcessingEnd()
           

            
            
            
            
            
            
            

if __name__ == "__main__":

    app= wx.App(False)
    
    
    bitmap= wx.Bitmap("./system/splash.png",wx.BITMAP_TYPE_PNG)
    splashScreen= wx.SplashScreen(bitmap,wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,6000, None, -1, wx.DefaultPosition, wx.DefaultSize,wx.BORDER_SIMPLE | wx.STAY_ON_TOP)
    wx.Yield()
    
    if len(glob.glob("./md1/sdf/*.sdf")) > 0:
    	os.system("python2.7 ./system/convert.py")
    else:
    	pass
    	    
    
    import time
    time.sleep(3)
    splashScreen.Destroy()
    
    
    
    MainFrm()
    app.MainLoop()
    




