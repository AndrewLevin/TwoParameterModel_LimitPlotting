
void cmsLabel(TCanvas *canvas,
	      double lumi,
	      bool prelim = false,
	      const TString& lumiLabel = "fb",
	      double s = 8.)
{
  TLatex l;
  l.SetNDC();
  l.SetTextFont(42);
  l.SetTextAlign(31);
  l.SetTextSize(0.045);

  canvas->cd();
  TString prelimText;
  if (prelim)
    prelimText = " preliminary";

  l.DrawLatex(1. - canvas->GetRightMargin(),
	      1. - canvas->GetTopMargin() + 0.01,
Form("CMS%s, #scale[0.5]{#lower[-0.15]{#it{#int}}}#it{L} dt = %0.1f#kern[0.2]{%s}^{-1}, #sqrt{#it{s}} = %.0f#kern[0.1]{TeV}",
     prelimText.Data(), lumi, lumiLabel.Data(), s));
  canvas->Update();
}

void plotLimitStyle()
{
  // import os
  // macroPath = gROOT.GetMacroPath()
  // macroPath += os.environ["CMSSW_BASE"] + "/src/ElectroWeakAnalysis/VPlusJets/test:"
  // gROOT.SetMacroPath(macroPath)
  // del os

  gROOT->SetStyle("Plain");
  gStyle->SetPadTickX(1);
  gStyle->SetPadTickY(1);
  gStyle->SetOptStat("iouRMe");
  gStyle->SetPalette(1);
  gStyle->SetOptFit(1112);
  gStyle->SetOptTitle(0);
  
  gStyle->SetCanvasDefH(600); // Height of canvas
  gStyle->SetCanvasDefW(600); // Width of canvas
  gStyle->SetErrorX(0.);
  
  gStyle->SetMarkerStyle(20);
  
  // For the fit/function:
  gStyle->SetFuncColor(2);
  gStyle->SetFuncStyle(1);
  gStyle->SetFuncWidth(1);
  
  //  Margins:
  gStyle->SetPadTopMargin(0.06);
  gStyle->SetPadBottomMargin(0.15);
  gStyle->SetPadLeftMargin(0.18); // was 0.16
  gStyle->SetPadRightMargin(0.06);// was 0.02
  
  gStyle->SetTitleColor(1, "XYZ");
  gStyle->SetTitleFont(42, "XYZ");
  gStyle->SetTitleSize(0.07, "XYZ");
  gStyle->SetTitleXOffset(0.9);
  gStyle->SetTitleYOffset(1.3); // was 1.25
  
  //  For the axis labels:
  gStyle->SetLabelColor(1, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");
  gStyle->SetLabelOffset(0.007, "XYZ");
  gStyle->SetLabelSize(0.06, "XYZ");
  gStyle->SetNdivisions(505, "XYZ");
  
}

