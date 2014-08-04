from ROOT import *
from array import array
import sys

if len(sys.argv) != 3:
    print "usage: python2.6 "+sys.argv[0]+" expected_contour_filename observed_contour_filename"
    sys.exit()

gStyle.SetCanvasDefH(600); 
gStyle.SetCanvasDefW(600); 
gStyle.SetErrorX(0.);

gStyle.SetPadTopMargin(0.06);
gStyle.SetPadBottomMargin(0.15);
gStyle.SetPadLeftMargin(0.18)
gStyle.SetPadRightMargin(0.06);

gStyle.SetLabelColor(1, "XYZ");
gStyle.SetLabelFont(42, "XYZ");
gStyle.SetLabelOffset(0.007, "XYZ");
gStyle.SetLabelSize(0.04, "XYZ");
gStyle.SetNdivisions(505, "XYZ");

gStyle.SetMarkerStyle(20);

expectedcontourfilename=sys.argv[1]
observedcontourfilename=sys.argv[2]

f_expected_contour=TFile(expectedcontourfilename,"r")
f_observed_contour=TFile(observedcontourfilename,"r")

g_exp=f_expected_contour.Get("Graph")
g_obs=f_observed_contour.Get("Graph")

g_obs.SetLineWidth(2)

SMpoint = TGraph(1);
SMpoint.SetPoint(1,0,0);


legend = TLegend(0.562,0.746,0.904,0.877,"","NDC");
legend.SetFillStyle(0);
legend.SetBorderSize(0);
legend.SetTextFont(42);

legend.AddEntry(g_exp,"Expected 95% CL","L")
legend.AddEntry(g_obs,"Observed 95% CL","L")
legend.AddEntry(SMpoint,"SM","Po")


g_exp.Draw("AC")
g_obs.Draw("C")
SMpoint.Draw("SAME Po");
legend.Draw()

CMSLabel = TLatex (0.18, 0.95, "#bf{CMS (preliminary)}");
CMSLabel.SetNDC ();
CMSLabel.SetTextAlign (10);
CMSLabel.SetTextFont (42);
CMSLabel.SetTextSize (0.040);
CMSLabel.Draw ("same") ;

lumiLabel=TLatex (0.95, 0.95, "19.4 fb^{-1} (8 TeV)");
lumiLabel.SetNDC ();
lumiLabel.SetTextAlign (30);
lumiLabel.SetTextFont (42);
lumiLabel.SetTextSize (0.040);
lumiLabel.Draw("same")

c1.SaveAs("contourplot.pdf")

raw_input()
