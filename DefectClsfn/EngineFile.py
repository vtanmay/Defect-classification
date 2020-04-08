import DefectClsfn.CommonLibrary as cmnLib

# fetch defect data from JIRA - WB-2908, PLAT-216, WB-2806
print("=== defect summary==",cmnLib.getDefectSummary(prProject='WB',prDefectId='WB-2806'))