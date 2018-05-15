import ROOT
from ROOT import TH1F, TCanvas, TFile, TColor,THStack,TLegend,TLatex, TChain, TVector3
import numpy as np
from scipy import interp
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(0)


def GetBinContentList(hist):
    ls_bincontent = []
    N = hist.GetSize()
    for i in range(N):
        ls_bincontent.append(hist.GetBinContent(i))
    return(ls_bincontent)

def GenXList(hist):
    ls_x = []
    N = hist.GetSize()
    for i in range(N):
        x = hist.GetXaxis().GetBinCenter(i)
        ls_x.append(x)
    return(ls_x)


def GetTrigRate(hist,num,divider,N0):
    ls_hist = GetBinContentList(hist)
    N0 = N0 /divider
    ls_rate = []
    n = hist.GetSize()
    for i in range(n):
        N = sum(ls_hist[i:])
        x = 28.6*((N/N0)**num)*1000
        ls_rate.append(x)
    return(ls_rate)

def FindThreshold(hist):
    ls_thes = GenXList(hist)
    ls_hist = GetBinContentList(hist)
    n = hist.GetSize()
    min = 200
    for i in range(n):
        count = sum(ls_hist[i:])/sum(ls_hist)
        if abs(count-0.9) < min and 0.88<count<1:
            min = abs(count-0.9)
            index = i
    return([sum(ls_hist[index:])/sum(ls_hist),ls_thes[index]])


def GetTrigRateCF(hist,num,divider,hist0):
    ls_hist = GetBinContentList(hist)
    ls_hist0 = GetBinContentList(hist0)
    ls_rate  = []
    n = hist.GetSize()
    for i in range(n):
        N = ls_hist[i]
        N0 = ls_hist0[i]
        if N0!=0:
            x = ((N/N0)**num)*100
            ls_rate.append(x)
        else:
            ls_rate.append(0)
    return(ls_rate)
    


def MBRate(hist_back,i,case,N0):
    ls_rate = GetTrigRate(hist_back,1,1,N0)
    name = ls_case[i]+"back"
    canvas[name] = TCanvas()
    graph[name] = ROOT.TGraph(len(ls_rate),np.array(GenXList(hist_back)),np.array(ls_rate))
    myfile[name] = TFile("Summaryplots_"+ls_case[i]+"/"+name+"_TauTrigRate.root","NEW")
    ROOT.gDirectory.Append(graph[name])
    graph[name].SetTitle(" Single Tau L2 Trigger Rate")
    graph[name].GetXaxis().SetTitle("Tau Cluster Pt Threshold [GeV]")       #x-axis
    graph[name].GetYaxis().SetTitle("Background Acceptance Rate [kHz]")
    graph[name].GetXaxis().SetRangeUser(0,100)   
    graph[name].SetMarkerColorAlpha(ls_color[i],1)
    graph[name].SetMarkerStyle(22)
    graph[name].SetName(name+"TauTrigRate")
    graph[name].Draw("AP")
    graph[name].Write(name+"_TauTrigRate")
    ROOT.gDirectory.Write()
    myfile[name].Write()
    myfile[name].Close()

    ls_rate2 = GetTrigRate(hist_back,2,1,N0)
    canvas[name+"2"] = TCanvas()
    graph[name+"2"] = ROOT.TGraph(len(ls_rate2),np.array(GenXList(hist_back)),np.array(ls_rate2))
    myfile[name+"2"] = TFile("Summaryplots_"+ls_case[i]+"/"+name+"_Di-TauTrigRate.root","NEW")
    ROOT.gDirectory.Append(graph[name+"2"])
    graph[name+"2"].SetTitle(" Di-Tau L2 Trigger Rate")
    graph[name+"2"].GetXaxis().SetTitle("Tau Cluster Pt Threshold [GeV]")        #x-axis
    graph[name+"2"].GetYaxis().SetTitle("Background Acceptance Rate [kHz]")
    graph[name+"2"].GetXaxis().SetRangeUser(0,100)   
    graph[name+"2"].SetMarkerColorAlpha(ls_color[i], 1)
    graph[name+"2"].SetMarkerStyle(23)
    graph[name+"2"].SetName(name+"_Di-TauTrigRate")
    graph[name+"2"].Draw("AP")
    graph[name+"2"].Write(name+"_Di-TauTrigRate")
    ROOT.gDirectory.Write()
    myfile[name+"2"].Write()
    myfile[name+"2"].Close()

def SRate(hist_signal,i,case,hist0):
    ls_rate = GetTrigRateCF(hist_signal,1,1,hist0)
    name = ls_case[i]+"tau"
    canvas[name] = TCanvas()
    graph[name] = ROOT.TGraph(len(ls_rate),np.array(GenXList(hist_signal)),np.array(ls_rate))
    myfile[name] = TFile("Summaryplots_"+ls_case[i]+"/"+name+"_TauTrigRate.root","NEW")
    ROOT.gDirectory.Append(graph[name])
    graph[name].SetTitle(" Single Tau L2 Trigger Performance")
    graph[name].GetXaxis().SetTitle("True Visual Tau Pt [GeV]")
    graph[name].GetYaxis().SetTitle("Signal efficiency(%)")
    graph[name].GetXaxis().SetRangeUser(0,150)   
    graph[name].SetMarkerColorAlpha(ls_color[i], 1)
    graph[name].SetMarkerStyle(26)
    graph[name].SetName(name+"_TauTrigRate")
    graph[name].Draw("AP")
    graph[name].Write(name+"_TauTrigRate")
    ROOT.gDirectory.Write()
    myfile[name].Write(name+"_TauTrigRate")
    myfile[name].Close()

    ls_rate2 = GetTrigRateCF(hist_signal,2,1,hist0)
    canvas[name+"2"] = TCanvas()
    graph[name+"2"] = ROOT.TGraph(len(ls_rate2),np.array(GenXList(hist_signal)),np.array(ls_rate2))
    myfile[name+"2"] = TFile("Summaryplots_"+ls_case[i]+"/"+name+"_Di-TauTrigRate.root","NEW")
    ROOT.gDirectory.Append(graph[name+"2"])
    graph[name+"2"].SetTitle(" Di-Tau L2 Trigger Performance")
    graph[name+"2"].GetXaxis().SetTitle("True Visual Tau Pt [GeV]")
    graph[name+"2"].GetYaxis().SetTitle("Signal efficiency(%)")
    graph[name+"2"].GetXaxis().SetRangeUser(0,150)   
    graph[name+"2"].SetMarkerColorAlpha(ls_color[i], 1)
    graph[name+"2"].SetMarkerStyle(32)
    graph[name+"2"].SetName(name+"_Di-TauTrigRate")
    graph[name+"2"].Draw("AP")
    graph[name+"2"].Write(name+"_Di-TauTrigRate")
    ROOT.gDirectory.Write()
    myfile[name+"2"].Write(name+"_Di-TauTrigRate")
    myfile[name+"2"].Close()



"""
    File Outputs: NN outputs, Di-Tau Trig and Single-Tau Trig Performance curve, Di-Tau Trig and Single-Tau Trig Background Acceptance curve, 
                  ROC curve, Eta and Phi histograms. 
    Changed variables: n = definition of True visual Tau cut. 
    Environment settings: need NN ouputs from 5 K-foldings, and ROC outputs from 5 K-foldings 
                          which can be produced from Neural Network models on Tier3. This current NN model 
                          is "Model80.50" that is a fully-connected NN with layer1 = 80 and layer2 =50. The NN outputs
                          are floating value (0,1). 

                          folder outputs are named "Summaryplots_..." which contains all results of this script 
                          in .root files. They can be displayed on the same canvas by running 
                          the C++ script "RateCurve_multigraph.cpp"


"""
n = 0   #  0 ="Et0ViPt0", 1 = "ViPt0", 2 = "ViPt10", 3 = "ViPt20", 4 = "ViPt30", 5 = "ViPt40"

hist_selectbacks = {}
hist_selectTaus = {}
canvas = {}
graph = {}
myfile = {}
legend = {}
ls_name = ["KF1","KF2","KF3","KF4","KF5"]    # 5 batches of K-folding 
ls_case = ["Et0ViPt0","ViPt0","ViPt10","ViPt20","ViPt30","ViPt40"]
ls_color = [ROOT.kBlack,ROOT.kBlue,ROOT.kRed,ROOT.kCyan,ROOT.kMagenta,ROOT.kGreen]
case = ls_case[n]   
                                                                     
t = TCanvas()
legend["NNoutputs"]= TLegend(0.6,0.5,0.8,0.7)
legend["Eta"]= TLegend(0.6,0.5,0.8,0.7)
legend["Phi"]= TLegend(0.6,0.5,0.8,0.7)
hist_selectbacks["allselect"] = TH1F("selected backgrounds (FP)","",100,0,100)
hist_selectbacks["allselect_N0"] = TH1F("use for num entries","",100,0,100)
hist_opbacks = TH1F("selected backgrounds NN output","",100,0,1)
hist_opbacks.SetFillColor(ls_color[n])
hist_opbacks.SetFillStyle(3003)
legend["NNoutputs"].AddEntry(hist_opbacks,case+"background","f")


hist_selectTaus["allselect"] = TH1F("selected signals (TP)","",200,0,200)
hist_selectTaus["baseline"] = TH1F("baseline signals","",200,0,200)
hist_opTaus = TH1F("selected signals NN output","",100,0,1)
hist_opTaus.SetLineColor(ls_color[n])
hist_opTaus.SetLineWidth(3)

hist_etaTaus = TH1F("selected signals Eta","",100,-1.4,1.4)
hist_etaTaus.SetLineColor(ls_color[n])
hist_etaTaus.SetFillStyle(3)

hist_phiTaus = TH1F("selected signals Phi","",100,-3.14,3.14)
hist_phiTaus.SetLineColor(ls_color[n])
hist_phiTaus.SetFillStyle(3)

legend["NNoutputs"].AddEntry(hist_opTaus,case+"signal","l")
legend["Eta"].AddEntry(hist_etaTaus,case+"signal","l")
legend["Phi"].AddEntry(hist_phiTaus,case+"signal","l")



# True visual tau Pt histogram from n=0 as a baseline  for Performance curves
for i in range(5):
    f = open("Model80.50_Et5"+ls_case[0]+"/NNs_outputs"+ls_name[i]+".txt","r")
                                                    #change num case
    for lines in f:
        ls_lines = lines.split(" ")
        for j in range(len(ls_lines)):
            sub_lines = ls_lines[j]
            ls_sub_lines = sub_lines.split(",")
            if len(ls_sub_lines) == 9:
                output = float(ls_sub_lines[0])
                true = float(ls_sub_lines[1])
                Vi_Pt = float(ls_sub_lines[2])
                Obsv_Pt = float(ls_sub_lines[3])
                bcid = float(ls_sub_lines[4].strip("\n"))
                if Vi_Pt!=0:
                    hist_selectTaus["baseline"].Fill(Vi_Pt/1000)    #x-axis
               
    f.close()

# True visual tau Pt histogram from n 
# Tau NN ouput histogram  
# Phi histogram
# Eta histogram 
for i in range(5):
    f = open("Model80.50_Et5"+ls_case[n]+"/NNs_outputs"+ls_name[i]+".txt","r")
                                                    #change num case
    for lines in f: 
        ls_lines = lines.split(" ")
        for j in range(len(ls_lines)):
            sub_lines = ls_lines[j]
            ls_sub_lines = sub_lines.split(",")
            if len(ls_sub_lines) == 9:
                output = float(ls_sub_lines[0])
                true = float(ls_sub_lines[1])
                Vi_Pt = float(ls_sub_lines[2])
                Obsv_Pt = float(ls_sub_lines[3])
                bcid = float(ls_sub_lines[4])
                trk = float(ls_sub_lines[5])
                eta = float(ls_sub_lines[6])
                phi = float(ls_sub_lines[7])
                pi0 = float(ls_sub_lines[8].strip("\n"))
                if Vi_Pt!=0:
                    hist_selectTaus["allselect"].Fill(Vi_Pt/1000)    #x-axis
                    hist_opTaus.Fill(output)
                    hist_etaTaus.Fill(eta)
                    hist_phiTaus.Fill(phi)
               
    f.close()




# Observable tau pt histogram of accepted backgrounds 
# Observable tau pt histogram of all backgrounds (Vi_Pt = 0) for Di and Single Background Acceptance curve 
# Background NN ouput histogram 
the_leg = FindThreshold(hist_opTaus)[1]
for i in range(5):
    f = open("Model80.50_Et5"+ls_case[n]+"/NNs_outputs"+ls_name[i]+".txt","r")
                                                 
    for lines in f: 
        ls_lines = lines.split(" ")
        for j in range(len(ls_lines)):
            sub_lines = ls_lines[j]
            ls_sub_lines = sub_lines.split(",")
            if len(ls_sub_lines) == 9:
                output = float(ls_sub_lines[0])
                true = float(ls_sub_lines[1])
                Vi_Pt = float(ls_sub_lines[2])
                Obsv_Pt = float(ls_sub_lines[3])
                bcid = float(ls_sub_lines[4])
                trk = float(ls_sub_lines[5])
                eta = float(ls_sub_lines[6])
                phi = float(ls_sub_lines[7])
                pi0 = float(ls_sub_lines[8].strip("\n"))
                if output >= the_leg and Vi_Pt==0:
                    hist_selectbacks["allselect"].Fill(Obsv_Pt/1000)      
                if Vi_Pt==0: 
                    hist_selectbacks["allselect_N0"].Fill(Obsv_Pt/1000)
                    hist_opbacks.Fill(output)
               
    f.close()

canvas["NNoutputs"] = TCanvas()
myfile["NNoutputs"] = TFile("Summaryplots_"+ls_case[n]+"/"+case+"NN_outputs"+".root","NEW")
ROOT.gDirectory.Append(hist_opbacks)
ROOT.gDirectory.Append(hist_opTaus)
hist_opbacks.Scale(0.2)
hist_opTaus.Scale(0.2)
hist_opTaus.Write(case+"NN_outputs"+"_Taus")
ROOT.gDirectory.Write()
myfile["NNoutputs"].Write()
myfile["NNoutputs"].Close()

canvas["Eta"] = TCanvas()
myfile["Eta"] = TFile("Summaryplots_"+ls_case[n]+"/"+case+"Eta"+".root","NEW")
ROOT.gDirectory.Append(hist_etaTaus)
hist_etaTaus.Scale(0.2)
hist_etaTaus.Write(case+"Eta"+"_Taus")
ROOT.gDirectory.Write()
myfile["Eta"].Write()
myfile["Eta"].Close()

canvas["Phi"] = TCanvas()
myfile["Phi"] = TFile("Summaryplots_"+ls_case[n]+"/"+case+"Phi"+".root","NEW")
ROOT.gDirectory.Append(hist_phiTaus)
hist_phiTaus.Scale(0.2)
hist_phiTaus.Write(case+"Phi"+"_Taus")
ROOT.gDirectory.Write()
myfile["Phi"].Write()
myfile["Phi"].Close()



# ROC curves
dict_fpr = {}
dict_tpr = {}
dict_the = {}
dict_auc = {}
tprs = []
thes = []
aucs = []
mean_fpr = np.linspace(0, 1, 100)

for i in range(5):
    f2 = open("Model80.50_Et5"+ls_case[n]+"/ROC_outputs"+ls_name[i]+".txt","r")
    dict_fpr[ls_name[i]] = []
    dict_tpr[ls_name[i]] = []
    dict_the[ls_name[i]] = []
    for lines in f2:
        ls_lines = lines.split(":")
        for j in range(len(ls_lines)):
            sub_lines = ls_lines[j]
            ls_sub_lines = sub_lines.split(",")
            if len(ls_sub_lines) == 4:
                fpr = float(ls_sub_lines[0])
                tpr = float(ls_sub_lines[1])
                the = float(ls_sub_lines[2])
                auc = float(ls_sub_lines[3])
                dict_fpr[ls_name[i]].append(fpr)
                dict_tpr[ls_name[i]].append(tpr)
                dict_the[ls_name[i]].append(the)
                aucs.append(auc)

    tprs.append(interp(mean_fpr,np.array(dict_fpr[ls_name[i]]),np.array(dict_tpr[ls_name[i]])))
    thes.append(interp(mean_fpr,np.array(dict_fpr[ls_name[i]]),np.array(dict_the[ls_name[i]])))
    tprs[-1][0] = 0.0
    thes[-1][0] = 0.0
    
    f2.close()


canvas["ROC"] = TCanvas()
mean_tpr = np.mean(tprs, axis=0)
mean_the = np.mean(thes, axis=0)
mean_tpr[-1] = 1.0
mean_auc = np.mean(aucs)  #not exactly correct
std_auc = np.std(aucs)
name = "ROC"
graph[name] = ROOT.TGraph(len(mean_fpr),mean_fpr,mean_tpr)
legend[name] = TLegend(0.5,0.6,0.8,0.8)
for i in range(len(mean_fpr)):
     if FindThreshold(hist_opTaus)[0] <= list(mean_tpr)[i] :     #(0.88-0.93)
         fpr_leg = list(mean_fpr)[i] 
         tpr_leg = list(mean_tpr)[i]
         break
legend[name].AddEntry(graph[name], ls_case[n]+" WP(%0.2f,%0.2f) = %2d%% & AUC = %0.2f" % (fpr_leg,tpr_leg,the_leg*100,mean_auc),"l")
myfile[name] = TFile("Summaryplots_"+ls_case[n]+"/"+case+name+".root","NEW")
ROOT.gDirectory.Append(graph[name])
ROOT.gDirectory.Append(legend[name])
graph[name].SetTitle("ROC Curve")
graph[name].GetXaxis().SetTitle("Background Efficiency")       #x-axis
graph[name].GetYaxis().SetTitle("Signal Efficiency")  
graph[name].SetLineColor(ls_color[n])
graph[name].Draw("AL")
legend[name].Draw()
graph[name].Write(case+name)
legend[name].Write(case+name+"leg")
ROOT.gDirectory.Write()
myfile[name].Write()
myfile[name].Close()


N0 =  hist_selectbacks["allselect_N0"].GetEntries()

# Di-Tau Trig and Single-Tau Trig Background Acceptance curve 
MBRate(hist_selectbacks["allselect"], n, case,N0)

# Di-Tau Trig and Single-Tau Trig Performance curve
SRate(hist_selectTaus["allselect"], n, case,hist_selectTaus["baseline"])

