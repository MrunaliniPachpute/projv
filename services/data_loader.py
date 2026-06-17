import pandas as pd
from config.settings import *

def load_complaints():
    return pd.read_excel(COMPLAINT_FILE)

# FUTURE LOADING QUERIES
# SELECT * FROM COMPLAIN_SYS_FEED
# SELECT * FROM ACKNOWLEDGEMENT
# and UPDATE STATUS_FLAG='R'
# INSERT ACKNOWLEDGEMENT, other things remains same!

def load_acknowledgements():
    return pd.read_excel(ACK_FILE)

def save_complaints(df):
    df.to_excel(COMPLAINT_FILE,index=False)

def save_acknowledgements(df):
    df.to_excel(ACK_FILE,index=False)