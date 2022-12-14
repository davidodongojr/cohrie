
import streamlit as st
import pandas as pd

from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from pathlib import Path
from streamlit_extras.colored_header import colored_header



st.set_page_config(
    page_title= "COHRIE-UGANDA",
    page_icon="cohrieLogo.PNG",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
colored_header(
    label="COLLABORATIVE ONE HEALTH RESEARCH INITIATIVE ON EPIDEMICS (COHRIE)",
    description="Project Title : Surveillance, Control and Prevention of Neglected Zoonotic Diseases in Uganda - A case study of Rift Valley Fever (RVF), Crimean-Congo Hemorrhagic Fever (CCHF)  and Brucellosis at the Human-Animal-Wildlife Interface in Diverse Agricultural systems.",
    color_name="blue-green-70"
    )

#st.sidebar.image("/images/cohrieLogo.png")
    
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

@st.cache
def data_upload():
    df = pd.read_csv("logframe.csv")
    return df

intro_markdown = read_markdown_file("intro.md")
mande =read_markdown_file("mande.md")
df = data_upload()



with st.sidebar:
    colored_header(label="MONITORING AND EVALUATION SYSTEM",
        description="COHRIE-UGANDA",
        color_name="blue-green-70")
    st.image("cohrieLogo.PNG")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠Project Overview", "🏦M&E Overview", "🧰M&E LogFrame", "📈Evaluation", "📖Monitoring"])

with tab1:
   st.markdown(intro_markdown, unsafe_allow_html=True)

with tab2:
    st.markdown(mande, unsafe_allow_html=True)
    st.image("evaluation_framework.png")
    st.subheader("M&E Logframe")

    with st.expander("Indicator List"):
        st.header("list")
    
with tab3:
    st.image("logframe.png")
    st.dataframe(df)
    st.header("AGgrid version")

    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=True,groupable=True)
    gridOptions = gd.build()

    AgGrid(df, gridOptions=gridOptions)

with tab4:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab5:
   st.header("An owl")



