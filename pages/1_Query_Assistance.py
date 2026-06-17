import streamlit as st

from services.data_loader import *
from services.knowledge_base import *
from services.semantic_search import *

complaints = load_complaints()
acks = load_acknowledgements()

kb = build_closed_ticket_kb(
    complaints,
    acks
)

search_engine = SemanticSearch()

st.title("Query Assistance")

subject = st.text_input(
    "Subject"
)

description = st.text_area(
    "Description"
)

if st.button("Search"):

    results = search_engine.search(
        subject,
        description
    )

    st.subheader(
        "Suggested Solutions"
    )

    st.dataframe(results)