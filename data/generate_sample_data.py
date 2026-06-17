# generate_sample_data.py

import pandas as pd

# -----------------------------

# COMPLAINT_SYS_FEED

# -----------------------------

complaints = [
{
"SR_NO":240001,
"TICKET_NO":"013-MT-2024-240001",
"ESTT_CODE":"013",
"FED_ECODE":"2007CK1197",
"FED_DATE":"30-12-24 10:00:08 AM",
"FED_IP":"10.1.1.12",
"FED_MAC":"NOT FOUND",
"SYSTEM_NO":"MT",
"SUBJECT":"Outlook not opening",
"COMP_BRIEF":"Outlook application closes immediately after launch",
"ASSIGN_TO":"ADMIN01",
"ASSIGN_BY":"2004AD1062",
"ASSIGN_DATE":"30-12-24 10:15:00 AM",
"STATUS_FLAG":"R",
"RECT_BY":"ADMIN01",
"RECT_DATE":"30-12-24 11:20:00 AM",
"PRIOR_FLAG":"HIGH",
"FLAG_TYPE":"ISSUE",
"BKT_FLAG":1,
"LEVEL_FLAG":"L3",
"RECT_ECODE":"2008CK1150"
},
{
"SR_NO":240002,
"TICKET_NO":"017-EFILE-2024-240002",
"ESTT_CODE":"017",
"FED_ECODE":"2004AD1129",
"FED_DATE":"30-12-24 11:20:14 AM",
"FED_IP":"10.1.1.14",
"FED_MAC":"AA-BB-CC-DD",
"SYSTEM_NO":"EFILE",
"SUBJECT":"File movement issue",
"COMP_BRIEF":"Unable to move file to next approval level",
"ASSIGN_TO":"ADMIN02",
"ASSIGN_BY":"2004AD1062",
"ASSIGN_DATE":"30-12-24 11:30:00 AM",
"STATUS_FLAG":"R",
"RECT_BY":"ADMIN02",
"RECT_DATE":"30-12-24 12:05:00 PM",
"PRIOR_FLAG":"MEDIUM",
"FLAG_TYPE":"ISSUE",
"BKT_FLAG":1,
"LEVEL_FLAG":"L2",
"RECT_ECODE":"2008CK1151"
},
{
"SR_NO":240003,
"TICKET_NO":"016-VMS-2024-240003",
"ESTT_CODE":"016",
"FED_ECODE":"2007CK1194",
"FED_DATE":"20-12-24 02:56:43 PM",
"FED_IP":"10.1.1.15",
"FED_MAC":"FF-EE-DD-CC",
"SYSTEM_NO":"VMS",
"SUBJECT":"Other user photo visible",
"COMP_BRIEF":"VMS showing photograph of another employee",
"ASSIGN_TO":"ADMIN03",
"ASSIGN_BY":"2004AD1062",
"ASSIGN_DATE":"20-12-24 03:10:00 PM",
"STATUS_FLAG":"R",
"RECT_BY":"ADMIN03",
"RECT_DATE":"20-12-24 04:00:00 PM",
"PRIOR_FLAG":"HIGH",
"FLAG_TYPE":"ISSUE",
"BKT_FLAG":1,
"LEVEL_FLAG":"L3",
"RECT_ECODE":"2008CK1152"
},
{
"SR_NO":240004,
"TICKET_NO":"013-MT-2024-240004",
"ESTT_CODE":"013",
"FED_ECODE":"2007CK1200",
"FED_DATE":"10-01-25 09:30:00 AM",
"FED_IP":"10.1.1.25",
"FED_MAC":"NOT FOUND",
"SYSTEM_NO":"MT",
"SUBJECT":"Outlook not opening after update",
"COMP_BRIEF":"Outlook crashes after recent update installation",
"ASSIGN_TO":None,
"ASSIGN_BY":None,
"ASSIGN_DATE":None,
"STATUS_FLAG":"P",
"RECT_BY":None,
"RECT_DATE":None,
"PRIOR_FLAG":"HIGH",
"FLAG_TYPE":"ISSUE",
"BKT_FLAG":0,
"LEVEL_FLAG":"L1",
"RECT_ECODE":None
},
{
"SR_NO":240005,
"TICKET_NO":"017-EFILE-2024-240005",
"ESTT_CODE":"017",
"FED_ECODE":"2007CK1201",
"FED_DATE":"11-01-25 10:00:00 AM",
"FED_IP":"10.1.1.30",
"FED_MAC":"MAC-777",
"SYSTEM_NO":"EFILE",
"SUBJECT":"Cannot move file",
"COMP_BRIEF":"File not moving to next workflow stage",
"ASSIGN_TO":None,
"ASSIGN_BY":None,
"ASSIGN_DATE":None,
"STATUS_FLAG":"I",
"RECT_BY":None,
"RECT_DATE":None,
"PRIOR_FLAG":"MEDIUM",
"FLAG_TYPE":"ISSUE",
"BKT_FLAG":0,
"LEVEL_FLAG":"L1",
"RECT_ECODE":None
}
]

# -----------------------------

# ACKNOWLEDGEMENT

# -----------------------------

acknowledgements = [
{
    "SNO":34,
    "ASNO":"013-MT-2024-240001",
    "REMARKS":"Outlook profile found corrupted.",
    "FDATE":"30-12-24 10:30:08 AM",
    "FLAG_NAME":"2008CK1150",
    "FLAG":"ADMIN",
    "AUTOCLOSE":"N"
},
{
    "SNO":35,
    "ASNO":"013-MT-2024-240001",
    "REMARKS":"Created new mail profile and reconfigured account.",
    "FDATE":"30-12-24 11:00:08 AM",
    "FLAG_NAME":"2008CK1150",
    "FLAG":"ADMIN",
    "AUTOCLOSE":"Y"
},

{
    "SNO":36,
    "ASNO":"017-EFILE-2024-240002",
    "REMARKS":"Workflow role mapping missing for employee.",
    "FDATE":"30-12-24 11:40:14 AM",
    "FLAG_NAME":"2008CK1151",
    "FLAG":"ADMIN",
    "AUTOCLOSE":"N"
},
{
    "SNO":37,
    "ASNO":"017-EFILE-2024-240002",
    "REMARKS":"Updated workflow permissions and tested successfully.",
    "FDATE":"30-12-24 11:50:14 AM",
    "FLAG_NAME":"2008CK1151",
    "FLAG":"ADMIN",
    "AUTOCLOSE":"Y"
},

{
    "SNO":38,
    "ASNO":"016-VMS-2024-240003",
    "REMARKS":"Photo cache mismatch observed.",
    "FDATE":"20-12-24 03:10:43 PM",
    "FLAG_NAME":"2008CK1152",
    "FLAG":"ADMIN",
    "AUTOCLOSE":"N"
},
{
    "SNO":39,
    "ASNO":"016-VMS-2024-240003",
    "REMARKS":"Cleared VMS cache and refreshed employee records.",
    "FDATE":"20-12-24 03:45:43 PM",
    "FLAG_NAME":"2008CK1152",
    "FLAG":"ADMIN",
    "AUTOCLOSE":"Y"
}
]

# -----------------------------

# SAVE FILES

# -----------------------------

complaints_df = pd.DataFrame(complaints)
ack_df = pd.DataFrame(acknowledgements)

complaints_df.to_excel(
"COMPLAIN_SYS_FEED.xlsx",
index=False
)

ack_df.to_excel(
"ACKNOWLEDGEMENT.xlsx",
index=False
)

print("Sample files generated successfully.")
print("-> COMPLAIN_SYS_FEED.xlsx")
print("-> ACKNOWLEDGEMENT.xlsx")
