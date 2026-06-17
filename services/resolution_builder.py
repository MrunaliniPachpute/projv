def build_resolution(ticket_no,
                     ack_df,
                     admin_codes=None):

    rows = ack_df[
        ack_df["ASNO"] == ticket_no
    ]

    if admin_codes:

        rows = rows[
            rows["EMP_CODE"].isin(admin_codes)
        ]

    remarks = rows["REMARKS"].fillna("")

    return "\n".join(
        remarks.tolist()
    )