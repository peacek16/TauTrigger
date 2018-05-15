import ROOT
from ROOT import TH1F, TCanvas, TFile, TColor,THStack,TLegend,TLatex, TChain, TVector3
import numpy as np
from scipy import interp
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(0)


"""
    File outputs: ROC curves of a defined "n" model .root extension
    Changed variables:  n which is an NN model name 
    Environment settings: need ROC outputs from the model. 
                          to compare with other models, make a folder Models_Et5ViPt0 and save all models there 
                          so that they will be displayed on the same canvas by Model_test.cpp
"""


n = "300.100.100.50"
canvas = {}
graph = {}
myfile = {}
legend = {}
ls_name = ["KF1","KF2","KF3","KF4","KF5"]
ls_color = [ROOT.kBlack,ROOT.kBlue,ROOT.kRed,ROOT.kCyan,ROOT.kMagenta,ROOT.kGreen]                                                                                                       #change num case

dict_fpr = {}
dict_tpr = {}
dict_the = {}
dict_auc = {}
tprs = []
thes = []
aucs = []
mean_fpr = np.linspace(0, 1, 100)
#ths = 0
#fpr_leg =0
#tpr_leg = 0
#num_ths = 0
for i in range(5):
    f2 = open("ModelL2"+n+"_Et5ViPt0"+"/ROC_outputs"+ls_name[i]+".txt","r")
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
name = "ROC"
canvas["ROC"] = TCanvas()
mean_tpr = np.mean(tprs, axis=0)
mean_the = np.mean(thes, axis=0)
mean_tpr[-1] = 1.0
mean_auc = np.mean(aucs)  #not exactly correct
std_auc = np.std(aucs)
graph[name] = ROOT.TGraph(len(mean_fpr),mean_fpr,mean_tpr)
legend[name] = TLegend(0.5,0.6,0.8,0.8)
for i in range(len(mean_fpr)):
     if 0.88<= list(mean_tpr)[i] <=0.93 :   
         fpr_leg = list(mean_fpr)[i] 
         tpr_leg = list(mean_tpr)[i]
         the_leg = list(mean_the)[i]  # not the same way as getting the working point in RateCurves.py
         break
legend[name].AddEntry(graph[name], "Model"+n+" WP(%0.2f,%0.2f) = %2d%% & AUC = %0.2f" % (fpr_leg,tpr_leg,the_leg*100,mean_auc),"l")
myfile[name] = TFile("Models_Et5ViPt0/Model"+n+".root","NEW")
ROOT.gDirectory.Append(graph[name])
ROOT.gDirectory.Append(legend[name])
graph[name].SetTitle("ROC Curve(L2)")
graph[name].GetXaxis().SetTitle("Background Efficiency")      
graph[name].GetYaxis().SetTitle("Signal Efficiency")  
graph[name].SetLineColor(ls_color[m])
graph[name].Draw("AL")
legend[name].Draw()
graph[name].Write("Model"+n)
legend[name].Write("Model"+n+"leg")
ROOT.gDirectory.Write()
myfile[name].Write()
myfile[name].Close()
