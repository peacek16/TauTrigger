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



/*
		File outputs: a single canvas with multiple ROC curves from different NN models
		Changed variables: string names of models to be tested
		Environment settings: a folder named "Models_[cuts]" with complete ROC curves in .root files of each model
							  ( in this example [cuts] = "Et5ViPt0" ) 

*/
void run(int argc = 0, char* argv[] = 0)
{
	TApplication theApp("App", &argc, argv);
	auto c1 = new TCanvas("c1", " Single Tau L2 Trigger");
	TGraph *g[3];
	TLegend *Lroc[3];
	auto legend = new TLegend(0.4, 0.5, 0.8, 0.7);
	auto mg = new TMultiGraph("MG3", " ROC Curves(L2)");
	for (int i = 1; i < 4; i++) {
		if (i ==1){

			TFile* f0_roc = new	TFile("Models_Et5ViPt0/Model80.50.root");
			g[i] = (TGraph*)f0_roc->Get("Model80.50");
			Lroc[i] = (TLegend*)f0_roc->Get("TPave");
			legend->AddEntry(g[i], Lroc[i]->GetEntry()->GetLabel(), "l");
			f0_roc->Close();
		}

		if (i == 2) {

			TFile* f1_roc = new	TFile("Models_Et5ViPt0/Model300.100.50.root");
			g[i] = (TGraph*)f1_roc->Get("Model300.100.50");
			Lroc[i] = (TLegend*)f1_roc->Get("TPave");
			legend->AddEntry(g[i], Lroc[i]->GetEntry()->GetLabel(), "l");
			f1_roc->Close();
		}

		if (i == 3) {

			TFile* f2_roc = new	TFile("Models_Et5ViPt0/Model300.100.100.50.root");
			g[i] = (TGraph*)f2_roc->Get("Model300.100.100.50");
			Lroc[i] = (TLegend*)f2_roc->Get("TPave");
			legend->AddEntry(g[i], Lroc[i]->GetEntry()->GetLabel(), "l");
			f2_roc->Close();
		}
		mg->Add(g[i], "l");

	}

	mg->Draw("AL");
	legend->Draw();
	mg->GetYaxis()->SetTitle("Signal Efficiency");
	mg->GetXaxis()->SetTitle("Background Efficiency");
	mg->GetXaxis()->SetRangeUser(0, 10);

	c1->Print("Models_ROC_Et5ViPt0.pdf");
	c1->Update();


	theApp.Run();
}

int main(int argc, char* argv[])
{
	run();
}

#if defined(__CINT__)

void Model_test()
{
	run();
}

#endif