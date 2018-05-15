#include "StdAfx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <functional>
#include <stdlib.h>
#include "TApplication.h"
#include <TGraph.h>
#include <TH1F.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TAxis.h>
#include <TPolyMarker.h> 
#include <algorithm>
#include <numeric>
#include <TMultiGraph.h>
#include <TLegend.h>
#include <TLegendEntry.h>
#include <TPave.h>
#include <TString.h>


using namespace std;

/*
	File outputs: A single canvas with six sub-canvases
	Changed variables: manually change between Di-Tautrigger to Single-Tautrigger by changing every related strings below	
					   (calling vector<string> on strings did not work when I tried) 
	Environment settings: need folders with names "Summaryplots_..." to get .root files 
						  labels and colors are already embedded in .root files 

*/

void run(int argc = 0, char* argv[] = 0)
{
	TApplication theApp("App", &argc, argv);
	//vector<string> ls_title = { " Single Tau Trigger Rate", " Di-Tau L2 Trigger Rate ", " Tau L2 Trigger Rate (K-fold Average)", " Di-Tau L2 Trigger Rate (K-fold Average)" };
	auto c1 = new TCanvas("c1", " Single Tau Trigger");
	c1->Divide(3, 2);
	TGraph *g1[5];
	TGraph *g2[5];
	TGraph *g3[5];

	TH1F *h1[5];
	TH1F *h2[5];
	TH1F *h3[5];
	TH1F *h4[5];
	TLegend *Lroc[5];


	auto legend1 = new TLegend(0.6, 0.7, 0.9, 0.9);
	auto legend2 = new TLegend(0.6, 0.2, 0.9, 0.4);
	auto legend4 = new TLegend(0.4, 0.5, 0.8, 0.7);

	
	auto mg1 = new TMultiGraph("MG1", " Single Tau Trigger Rate");
	auto mg2 = new TMultiGraph("MG2", " Single Tau Trigger Performance");
	auto mg3 = new TMultiGraph("MG3", " ROC Curves");

	
	vector<string> ls_et = { "0","10","20","30","40" };
	vector<string> ls_type = { "back_TauTrigRate","back_Di-TauTrigRate" ,"tau_TauTrigRate" ,"tau_Di-TauTrigRate"};

	
	for (int i = 1; i < 6; i++) {

		if (i == 1) {
			TFile* f0_rcS = new TFile("Summaryplots_ViPt0/ViPt0tau_TauTrigRate.root");
			TFile* f0_rcB = new TFile("Summaryplots_ViPt0/ViPt0back_TauTrigRate.root");
			TFile* f0_roc = new	TFile("Summaryplots_ViPt0/ViPt0ROC.root");	

			g1[i] = new TGraph();
			g2[i] = new TGraph();
			g1[i] = (TGraph*)f0_rcB->Get("ViPt0back_TauTrigRate");
			g2[i] = (TGraph*)f0_rcS->Get("ViPt0tau_TauTrigRate");
			g1[i]->SetMarkerStyle(7);
			g1[i]->SetMarkerColor(i + 1);
			g2[i]->SetMarkerStyle(22);
			g2[i]->SetMarkerColor(i + 1);
			legend1->AddEntry(g1[i], "Visual Tau  Pt > 0 GeV", "p");
			legend2->AddEntry(g2[i], "Visual Tau  Pt > 0 GeV", "p");

			g3[i] = new TGraph();
			g3[i] = (TGraph*)f0_roc->Get("ViPt0ROC");
			Lroc[i] = (TLegend*)f0_roc->Get("TPave");
			legend4->AddEntry(g3[i],Lroc[i]->GetEntry()->GetLabel(),"l");

		    f0_rcS->Close();
			f0_rcB->Close();
			f0_roc->Close();



		}
		
		if (i == 2) {
			TFile* f1_rcS = new TFile("Summaryplots_ViPt10/ViPt10tau_TauTrigRate.root");
			TFile* f1_rcB = new TFile("Summaryplots_ViPt10/ViPt10back_TauTrigRate.root");
			TFile* f1_roc = new	TFile("Summaryplots_ViPt10/ViPt10ROC.root");

			g1[i] = new TGraph();
			g2[i] = new TGraph();
			g1[i] = (TGraph*)f1_rcB->Get("ViPt10back_TauTrigRate");
			g2[i] = (TGraph*)f1_rcS->Get("ViPt10tau_TauTrigRate");
			g1[i]->SetMarkerStyle(7);
			g1[i]->SetMarkerColor(i + 1);
			g2[i]->SetMarkerStyle(23);
			g2[i]->SetMarkerColor(i + 1);
			legend1->AddEntry(g1[i], "Visual Tau  Pt > 10 GeV", "p");
			legend2->AddEntry(g2[i], "Visual Tau  Pt > 10 GeV", "p");

			g3[i] = new TGraph();
			g3[i] = (TGraph*)f1_roc->Get("ViPt10ROC");
			Lroc[i] = (TLegend*)f1_roc->Get("TPave");
			legend4->AddEntry(g3[i], Lroc[i]->GetEntry()->GetLabel(), "l");


			f1_rcS->Close();
			f1_rcB->Close();
			f1_roc->Close();

		}
		if (i == 3) {
			TFile* f2_rcS = new TFile("Summaryplots_ViPt20/ViPt20tau_TauTrigRate.root");
			TFile* f2_rcB = new TFile("Summaryplots_ViPt20/ViPt20back_TauTrigRate.root");
			TFile* f2_roc = new	TFile("Summaryplots_ViPt20/ViPt20ROC.root");

			g1[i] = new TGraph();
			g2[i] = new TGraph();
			g1[i] = (TGraph*)f2_rcB->Get("ViPt20back_TauTrigRate");
			g2[i] = (TGraph*)f2_rcS->Get("ViPt20tau_TauTrigRate");
			g1[i]->SetMarkerStyle(7);
			g1[i]->SetMarkerColor(i + 1);
			g2[i]->SetMarkerStyle(2);
			g2[i]->SetMarkerColor(i + 1);
			legend1->AddEntry(g1[i], "Visual Tau  Pt > 20 GeV", "p");
			legend2->AddEntry(g2[i], "Visual Tau  Pt > 20 GeV", "p");

			g3[i] = new TGraph();
			g3[i] = (TGraph*)f2_roc->Get("ViPt20ROC");
			Lroc[i] = (TLegend*)f2_roc->Get("TPave");
			legend4->AddEntry(g3[i], Lroc[i]->GetEntry()->GetLabel(), "l");


			f2_rcS->Close();
			f2_rcB->Close();
			f2_roc->Close();

		}
		if (i == 4) {
			TFile* f3_rcS = new TFile("Summaryplots_ViPt30/ViPt30tau_TauTrigRate.root");
			TFile* f3_rcB = new TFile("Summaryplots_ViPt30/ViPt30back_TauTrigRate.root");
			TFile* f3_roc = new	TFile("Summaryplots_ViPt30/ViPt30ROC.root");


			g1[i] = new TGraph();
			g2[i] = new TGraph();
			g1[i] = (TGraph*)f3_rcB->Get("ViPt30back_TauTrigRate");
			g2[i] = (TGraph*)f3_rcS->Get("ViPt30tau_TauTrigRate");
			g1[i]->SetMarkerStyle(7);
			g1[i]->SetMarkerColor(i + 1);
			g2[i]->SetMarkerStyle(3);
			g2[i]->SetMarkerColor(i + 1);
			legend1->AddEntry(g1[i], "Visual Tau  Pt > 30 GeV", "p");
			legend2->AddEntry(g2[i], "Visual Tau  Pt > 30 GeV", "p");

			g3[i] = new TGraph();
			g3[i] = (TGraph*)f3_roc->Get("ViPt30ROC");
			Lroc[i] = (TLegend*)f3_roc->Get("TPave");
			legend4->AddEntry(g3[i], Lroc[i]->GetEntry()->GetLabel(), "l");

			f3_rcS->Close();
			f3_rcB->Close();
			f3_roc->Close();


		}

		
		if (i == 5) {
			TFile* f4_rcS = new TFile("Summaryplots_ViPt40/ViPt40tau_TauTrigRate.root");
			TFile* f4_rcB = new TFile("Summaryplots_ViPt40/ViPt40back_TauTrigRate.root");
			TFile* f4_roc = new	TFile("Summaryplots_ViPt40/ViPt40ROC.root");

			g1[i] = new TGraph();
			g2[i] = new TGraph();
			g1[i] = (TGraph*)f4_rcB->Get("ViPt40back_TauTrigRate");
			g2[i] = (TGraph*)f4_rcS->Get("ViPt40tau_TauTrigRate");
			g1[i]->SetMarkerStyle(7);
			g1[i]->SetMarkerColor(i + 1);
			g2[i]->SetMarkerStyle(5);
			g2[i]->SetMarkerColor(i + 1);
			legend1->AddEntry(g1[i], "Visual Tau  Pt > 40 GeV", "p");
			legend2->AddEntry(g2[i], "Visual Tau  Pt > 40 GeV", "p");

			g3[i] = new TGraph();
			g3[i] = (TGraph*)f4_roc->Get("ViPt40ROC");
			Lroc[i] = (TLegend*)f4_roc->Get("TPave");
			legend4->AddEntry(g3[i], Lroc[i]->GetEntry()->GetLabel(), "l");
			

			f4_rcS->Close();
			f4_rcB->Close();
			f4_roc->Close();


		}
		
		

		mg1->Add(g1[i], "cp");
		mg2->Add(g2[i], "p");
		mg3->Add(g3[i], "l");

	}
	
	c1->cd(1);
	mg1->Draw("AP");
	legend1->Draw();
	mg1->GetYaxis()->SetTitle("Background acceptance rate [kHz]");
	mg1->GetXaxis()->SetTitle("Tau cluster Pt threshold [GeV]");
	mg1->SetTitle("Single Tau Trigger Rate");
	mg1->GetXaxis()->SetRangeUser(0, 100);

	c1->cd(2);
	mg2->Draw("AP");
	legend2->Draw();
	mg2->GetYaxis()->SetTitle("Signal Efficiency(%)");
	mg2->GetXaxis()->SetTitle("True Visual Tau Pt [GeV]");
	mg2->SetTitle("Single Tau Trigger Performance");
	mg2->GetXaxis()->SetRangeUser(0, 200);
	
	c1->cd(3);
	mg3->Draw("AL");
	legend4->Draw();
	mg3->GetYaxis()->SetTitle("Signal Efficiency");
	mg3->GetXaxis()->SetTitle("Background Efficiency");
	mg3->SetTitle("ROC Curves");
	mg3->GetXaxis()->SetRangeUser(0, 10);


	c1->cd(4);
	auto legend3 = new TLegend(0.5, 0.6, 0.8, 0.9);
	
	TFile* f0_nnop = new TFile("Summaryplots_ViPt0/ViPt0NN_outputs.root");
	h1[1] = (TH1F*)f0_nnop->Get("selected backgrounds NN output");
	h2[1] = (TH1F*)f0_nnop->Get("selected signals NN output");
	legend3->AddEntry(h1[1], "ViPt0 background", "f");
	legend3->AddEntry(h2[1], "ViPt0 signal", "l");
	TFile* f1_nnop = new TFile("Summaryplots_ViPt10/ViPt10NN_outputs.root");
	h1[2] = (TH1F*)f1_nnop->Get("selected backgrounds NN output");
	h2[2] = (TH1F*)f1_nnop->Get("selected signals NN output");
	legend3->AddEntry(h1[2], "ViPt10 background", "f");
	legend3->AddEntry(h2[2], "ViPt10 signal", "l");
	TFile* f2_nnop = new TFile("Summaryplots_ViPt20/ViPt20NN_outputs.root");
	h1[3] = (TH1F*)f2_nnop->Get("selected backgrounds NN output");
	h2[3] = (TH1F*)f2_nnop->Get("selected signals NN output");
	legend3->AddEntry(h1[3], "ViPt20 background", "f");
	legend3->AddEntry(h2[3], "ViPt20 signal", "l");
	TFile* f3_nnop = new TFile("Summaryplots_ViPt30/ViPt30NN_outputs.root");
	h1[4] = (TH1F*)f3_nnop->Get("selected backgrounds NN output");
	h2[4] = (TH1F*)f3_nnop->Get("selected signals NN output");
	legend3->AddEntry(h1[4], "ViPt30 background", "f");
	legend3->AddEntry(h2[4], "ViPt30 signal", "l");
	TFile* f4_nnop = new TFile("Summaryplots_ViPt40/ViPt40NN_outputs.root");
	h1[5] = (TH1F*)f4_nnop->Get("selected backgrounds NN output");
	h2[5] = (TH1F*)f4_nnop->Get("selected signals NN output");
	legend3->AddEntry(h1[5], "ViPt40 background", "f");
	legend3->AddEntry(h2[5], "ViPt40 signal", "l");
	h2[1]->Draw();
	legend3->Draw();
	h2[1]->SetTitle("NN outputs");
	h2[1]->GetXaxis()->SetTitle("NN outputs");
	h2[1]->GetYaxis()->SetTitle("the number of seeds");
	h1[1]->Draw("SAME");
	for (int i = 2; i < 6; i++) {
		h2[i]->Draw("SAME");
	}
	for (int i = 2; i < 6; i++) {
		h1[i]->Draw("SAME");
	}


	c1->cd(5);
	auto legend5 = new TLegend(0.5, 0.6, 0.8, 0.9);

	TFile* f0_eta = new TFile("Summaryplots_ViPt0/ViPt0Eta.root");
	h3[1] = (TH1F*)f0_eta->Get("selected signals Eta");
	legend5->AddEntry(h3[1], "ViPt0 signal", "l");
	TFile* f1_eta = new TFile("Summaryplots_ViPt10/ViPt10Eta.root");
	h3[2] = (TH1F*)f1_eta->Get("selected signals Eta");
	legend5->AddEntry(h3[2], "ViPt10 signal", "l");
	TFile* f2_eta = new TFile("Summaryplots_ViPt20/ViPt20Eta.root");
	h3[3] = (TH1F*)f2_eta->Get("selected signals Eta");
	legend5->AddEntry(h3[3], "ViPt20 signal", "l");
	TFile* f3_eta = new TFile("Summaryplots_ViPt30/ViPt30Eta.root");
	h3[4] = (TH1F*)f3_eta->Get("selected signals Eta");
	legend5->AddEntry(h3[4], "ViPt30 signal", "l");
	TFile* f4_eta = new TFile("Summaryplots_ViPt40/ViPt40Eta.root");
	h3[5] = (TH1F*)f4_eta->Get("selected signals Eta");
	legend5->AddEntry(h3[5], "ViPt40 signal", "l");
	h3[1]->Draw();
	legend5->Draw();
	h3[1]->SetTitle("Signal Tau Eta");
	h3[1]->GetXaxis()->SetTitle("Eta");
	h3[1]->GetYaxis()->SetTitle("the number of seeds");
	for (int i = 2; i < 6; i++) {
		h3[i]->Draw("SAME");
	}

	c1->cd(6);
	auto legend6 = new TLegend(0.5, 0.6, 0.8, 0.9);

	TFile* f0_phi = new TFile("Summaryplots_ViPt0/ViPt0Phi.root");
	h4[1] = (TH1F*)f0_phi->Get("selected signals Phi");
	legend6->AddEntry(h4[1], "ViPt0 signal", "l");
	TFile* f1_phi = new TFile("Summaryplots_ViPt10/ViPt10Phi.root");
	h4[2] = (TH1F*)f1_phi->Get("selected signals Phi");
	legend6->AddEntry(h4[2], "ViPt10 signal", "l");
	TFile* f2_phi = new TFile("Summaryplots_ViPt20/ViPt20Phi.root");
	h4[3] = (TH1F*)f2_phi->Get("selected signals Phi");
	legend6->AddEntry(h4[3], "ViPt20 signal", "l");
	TFile* f3_phi = new TFile("Summaryplots_ViPt30/ViPt30Phi.root");
	h4[4] = (TH1F*)f3_phi->Get("selected signals Phi");
	legend6->AddEntry(h4[4], "ViPt30 signal", "l");
	TFile* f4_phi = new TFile("Summaryplots_ViPt40/ViPt40Phi.root");
	h4[5] = (TH1F*)f4_phi->Get("selected signals Phi");
	legend6->AddEntry(h4[5], "ViPt40 signal", "l");
	h4[1]->Draw();
	legend6->Draw();
	h4[1]->SetTitle("Signal Tau Phi");
	h4[1]->GetXaxis()->SetTitle("Phi");
	h4[1]->GetYaxis()->SetTitle("the number of seeds");
	for (int i = 2; i < 6; i++) {
		h4[i]->Draw("SAME");
	}

	c1->Print("Summaryplots_SingleTauTrig.pdf");
	c1->Update();

	
	theApp.Run();
}

int main(int argc, char* argv[])
{
	run();
}

#if defined(__CINT__)

void RateCurve_multigraph()
{
	run();
}

#endif