from ROOT import *
from array import array
import sys

deltanllfilename=sys.argv[1]
contourfilename=sys.argv[2]

fdeltanll=TFile(deltanllfilename,"r")

fdeltanll.ls() 

fcontour=TFile(contourfilename,"r")



tree=fdeltanll.Get("limit")

graph=TGraph()

first=True

for entry in range(tree.GetEntries()):
    tree.GetEntry(entry)

    if first:
        first=False
        continue

    #if "param2prev" in vars():
    #    print "tree.param2 - param1prev = "+str(tree.param2 - param2prev)

    #param2prev=tree.param2

    graph.SetPoint(graph.GetN(), tree.param1,tree.param2)
    

    #print "tree.param1 = "+str(tree.param1)
    #print "tree.param2 = "+str(tree.param2)

    if "minparam1" not in vars():
        minparam1 = tree.param1
        maxparam1 = tree.param1
        minparam2 = tree.param2
        maxparam2 = tree.param2
        firstparam1 = tree.param1
        firstparam2 = tree.param2
        
    if tree.param1 < minparam1:
        minparam1 = tree.param1
    if tree.param1 > maxparam1:
        maxparam1 = tree.param1        
    if tree.param2 < minparam2:
        minparam2 = tree.param2       
    if tree.param2 > maxparam2:
        maxparam2 = tree.param2 

    if firstparam1 != tree.param1  and "param1interval" not in vars():
        param1interval=abs(firstparam1 - tree.param1)

    if firstparam2 != tree.param2  and "param2interval" not in vars():
        param2interval=abs(firstparam2 - tree.param2)

    if firstparam1 != tree.param1 and abs(firstparam1 - tree.param1) < param1interval:
        param1interval=abs(firstparam1 - tree.param1)

    if firstparam2 != tree.param2 and abs(firstparam2 - tree.param2) < param2interval:
        param2interval=abs(firstparam2 - tree.param2)

if "param1interval" not in vars() or "param1interval" not in vars():
    print "\"param1interval\" not in vars() or \"param1interval\" not in vars(), exiting"
    sys.exit(0);

print "minparam1 = "+str(minparam1)
print "maxparam1 = "+str(maxparam1)
print "minparam2 = "+str(minparam2)
print "maxparam1 = "+str(maxparam2)
print "param1interval = "+str(param1interval)
print "param2interval = "+str(param2interval)

print "(maxparam1-minparam1)/param1interval = "+str((maxparam1-minparam1)/param1interval)
print "(maxparam2-minparam2)/param2interval = "+str((maxparam2-minparam2)/param2interval)

#int rounds down
print "int((maxparam1-minparam1)/param1interval) = "+str(int((maxparam1-minparam1)/param1interval))
print "int((maxparam2-minparam2)/param2interval) = "+str(int((maxparam2-minparam2)/param2interval))

hist=TProfile2D("myhist","myhist",int((maxparam1-minparam1)/param1interval + 0.1)+1,minparam1-param1interval/2,maxparam1+param2interval/2, int((maxparam2-minparam2)/param2interval + 0.1)+1,minparam2-param2interval/2,maxparam2+param2interval/2)
hist2=TProfile2D("myhist2","myhist2",int((maxparam1-minparam1)/param1interval + 0.1)+1,minparam1-param1interval/2,maxparam1+param2interval/2, int((maxparam2-minparam2)/param2interval + 0.1)+1,minparam2-param2interval/2,maxparam2+param2interval/2)

graph.GetXaxis().SetRangeUser(10,20)
graph.GetYaxis().SetRangeUser(-35,-25)

tree.Draw("1:param2:param1 >> myhist","deltaNLL > 5.99/2","prof2d,colz")
tree.Draw("-1:param2:param1 >> myhist2","deltaNLL < 5.99/2","prof2d,colz")
#tree.Draw("param1:param2 >> myhist","deltaNLL ","")

gDirectory.ls()

#first=True

#for entry in range(tree.GetEntries()):
#    tree.GetEntry(entry)
#
#    if first:
#        first=False
#        continue
#
#    if tree.deltaNLL < 5.99/2:
#        continue
#
#    hist.SetBinContent(hist.FindFixBin(tree.param1,tree.param2),tree.deltaNLL)



gStyle.SetFuncStyle(1)
gStyle.SetFuncWidth(1)

hist.SetTitle("")
hist2.SetTitle("")
hist.GetXaxis().SetTitle("F_{S0} (TeV^{-4})")
hist.GetYaxis().SetTitle("F_{S1} (TeV^{-4})")
hist.SetStats(0)
hist2.SetStats(0)

hist.Draw("col")
hist2.Draw("SAME col")

fcontour.ls()

g=fcontour.Get("Graph")

g.SetLineWidth(2)
g.SetLineStyle(1)

g.SetLineColor(kBlack)

g.SetTitle("")



g.Draw("C SAME")

gPad.Update()

c1.SaveAs("contour_check.pdf")

raw_input()
