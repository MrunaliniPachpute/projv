import pandas as pd

from services.resolution_builder import (
    build_resolution
)

def build_closed_ticket_kb(
    complaints,
    acknowledgements,
    admin_codes=None
):

    closed = complaints[
        complaints["STATUS_FLAG"]=="R"
    ]

    records=[]

    for _,row in closed.iterrows():

        resolution = build_resolution(
            row["TICKET_NO"],
            acknowledgements,
            admin_codes
        )

        records.append({
            "ticket_no":row["TICKET_NO"],
            "subject":row["SUBJECT"],
            "complaint":row["COMP_BRIEF"],
            "resolution":resolution
        })

    return pd.DataFrame(records)