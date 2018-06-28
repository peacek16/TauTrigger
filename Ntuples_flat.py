import ROOT
from ROOT import TH1F, TCanvas, TFile, TColor,THStack,TLegend,TLatex, TChain, TVector3
import numpy as np


"""
      File ouputs:  flat files containing strings of multiple variables 
                    lines of signals followed by lines of backgrounds 
      Changed variables: string name of FLEt, Ntuple files, and Et layers 
      Environment settings: need Ntuple files of signals and backgrounds
                            recommend run it in Tier3, and feed it in the NN model there 

"""
FLEt = open("L2TauEt_ViPt0Et5Eta1.4_Train.data","w")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(0)

signalFile = TFile("v2/output_Z200.root")
signal = signalFile.Get("mytree") 
backFile = TFile("v2/output_MB200.root")
back = backFile.Get("mytree")

count = 0
for entry in signal:
    count+=1
    #L0cells = getattr(entry,"L0CellEt[17][5]")
    #L1cells = getattr(entry,"L1CellEt[17][5]")
    L2cells = getattr(entry,"L2CellEt[17][5]")
    #L3cells = getattr(entry,"L3CellEt[17][5]")
    #Hadcells = getattr(entry,"HadCellEt[17][5]") 
    seed = getattr(entry,"seed")
    eta = seed.Eta()
    phi = seed.Phi()
    viTau = getattr(entry,"mc_visibleTau")
    vipt = viTau.Pt()
    EM_pt = getattr(entry,"TauCluster_EM")
    Had_pt = getattr(entry,"TauCluster_Had")
    obsv_pt = EM_pt + Had_pt
    bcid = getattr(entry,"bcid") 
    trk = getattr(entry,"mc_tracks")
    pi0 = getattr(entry,"mc_pi0")
    arr_L2cells = np.asarray(L2cells)
    L2cells_2D = arr_L2cells.reshape((17,5)).transpose()
    if seed.Et()>5000 and vipt>0 and -1.4<seed.Eta()<1.4:    # cuts  applied 
       # FLEt.write(','.join(str(L0cells[i]) for i in range(len(L0cells)))+',')
       # FLEt.write(','.join(str(L1cells[i]) for i in range(len(L1cells)))+',')
        FLEt.write(','.join(str(L2cells_2D[i][j]) for i in range(1,4) for j in range(4,13))) # add "," if inputs are all layers
       # FLEt.write(','.join(str(L3cells[i]) for i in range(len(L3cells)))+',')
       # FLEt.write(','.join(str(Hadcells[i]) for i in range(len(Hadcells))))
        FLEt.write(",1,"+str(vipt)+","+str(obsv_pt)+","+str(bcid)+","+str(trk)+","+str(eta)+","+str(phi)+","+str(pi0))
        FLEt.write("\n")

for entry in back:
    #L0cells = getattr(entry,"L0CellEt[17][5]")
    #L1cells = getattr(entry,"L1CellEt[17][5]")
    L2cells = getattr(entry,"L2CellEt[17][5]")
    #L3cells = getattr(entry,"L3CellEt[17][5]")
    #Hadcells = getattr(entry,"HadCellEt[17][5]")
    seed = getattr(entry,"seed")
    eta = seed.Eta()
    phi = seed.Phi()
    EM_pt = getattr(entry,"TauCluster_EM")
    Had_pt = getattr(entry,"TauCluster_Had")
    obsv_pt = EM_pt + Had_pt
    bcid = getattr(entry,"bcid")
    if seed.Et()>5000 and -2.4<seed.Eta()<2.4:          # cuts applied 
        #FLEt.write(','.join(str(L0cells[i]) for i in range(len(L0cells)))+',')
        #FLEt.write(','.join(str(L1cells[i]) for i in range(len(L1cells)))+',')
        FLEt.write(','.join(str(L2cells[i]) for i in range(len(L2cells))))   # add "," if inputs are all layers
        #FLEt.write(','.join(str(L3cells[i]) for i in range(len(L3cells)))+',')
        #FLEt.write(','.join(str(Hadcells[i]) for i in range(len(Hadcells))))
        FLEt.write(",0,"+str(0)+","+str(obsv_pt)+","+str(bcid)+","+str(99)+","+str(eta)+","+str(phi)+","+str(99))
        FLEt.write("\n")
FLEt.close()

