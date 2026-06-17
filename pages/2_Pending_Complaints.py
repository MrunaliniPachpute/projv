import streamlit as st

from services.data_loader import *
from services.knowledge_base import *
from services.semantic_search import *
from services.ticket_service import *

complaints = load_complaints()
acks = load_acknowledgements()

kb = build_closed_ticket_kb(
    complaints,
    acks
)

search_engine = SemanticSearch()

pending = complaints[
    complaints["STATUS_FLAG"]
    .isin(["P","I"])
]

st.title(
    "Pending Complaints"
)

for _,ticket in pending.iterrows():

    with st.expander(
        f"{ticket['TICKET_NO']} - {ticket['SUBJECT']}"
    ):

        st.write(
            ticket["COMP_BRIEF"]
        )

        matches = search_engine.search(
            ticket["SUBJECT"],
            ticket["COMP_BRIEF"]
        )

        selected = st.selectbox(
            "Suggested Resolution",
            matches["resolution"].tolist(),
            key=ticket["TICKET_NO"]
        )

        if st.button(
            "Approve",
            key=f"a_{ticket['TICKET_NO']}"
        ):

            complaints,acks = (
                approve_resolution(
                    ticket["TICKET_NO"],
                    selected,
                    complaints,
                    acks
                )
            )

            save_complaints(
                complaints
            )

            save_acknowledgements(
                acks
            )

            st.success(
                "Added to database"
            )