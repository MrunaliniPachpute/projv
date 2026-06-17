from datetime import datetime

def approve_resolution(
    ticket_no,
    resolution,
    complaints,
    acknowledgements
):

    acknowledgements.loc[
        len(acknowledgements)
    ] = {

        "TICKET_NO":ticket_no,
        "REMARKS":resolution,
        "FDATE":datetime.now()
    }

    complaints.loc[
        complaints["TICKET_NO"]
        ==
        ticket_no,
        "STATUS_FLAG"
    ] = "R"

    return complaints, acknowledgements