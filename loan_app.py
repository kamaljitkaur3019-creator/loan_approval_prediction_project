import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(page_title="LOAN APPROVAL ANALYSIS", layout="wide")
st.sidebar.title("LOAN APPROVAL ANALYSIS")
st.sidebar.markdown("---")
st.sidebar.write("**PROJECT NAME:** LOAN APPROVAL ANALYSIS")
st.sidebar.write("**TOOLS USED:**")
st.sidebar.write("- Python")
st.sidebar.write("- Pandas")
st.sidebar.write("- NumPy")
st.sidebar.write("- Plotly")
st.sidebar.write("- Seaborn")
st.sidebar.write("- Matplotlib")
st.sidebar.write("- Streamlit")
st.sidebar.markdown("---")
st.sidebar.success("Data Exploration and Visualization Dashboard")
st.title("LOAN APPROVAL ANALYSIS")
st.info("""
This dashboard provides an interactive analysis of the Loan Approval dataset.
It includes dataset exploration, preprocessing, statistical analysis and graphical visualization.
""")
st.divider()
page = st.sidebar.radio("SELECT SECTION",["COLUMN NAMES","DATASET","STATISTICS","MISSING VALUES","GRAPHS","CONCLUSION"])
@st.cache_data
def load_data():
    df=pd.read_csv("loan_approval_dataset.csv")
    return df
df = load_data()
st.sidebar.title("LOAN APPROVAL ANALYSIS")
st.sidebar.write("DATA EXPLORATION AND VISUALIZATION")
df.columns=df.columns.str.strip()
graph = st.sidebar.selectbox(
    "SELECT GRAPH",
    [
    "BOX PLOT",
    "HISTOGRAM",
    "PARALLEL COORDINATES",
    "SUNBURST GRAPH",
    "TREEMAP",
    "SCATTER GRAPH",
    "PIE GRAPH",
    "HEATMAP GRAPH"
    ]
)
st.divider()
if page == "COLUMN NAMES":
    st.subheader("COLUMNS NAME")
    st.dataframe(pd.DataFrame({"Column Names": df.columns}))
    st.divider()
elif page == "DATASET":
    st.subheader("FIRST FIVE ROWS OF DATASET")
    st.dataframe(df.head())
    st.subheader("LAST FIVE ROWS OF DATASET")
    st.dataframe(df.tail())
    st.divider()
    st.subheader("SHAPE OF DATASET(ROWS AND COLUMNS)")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
    st.divider()
    st.subheader("DATA TYPES")
    st.dataframe(df.dtypes.reset_index())
    st.divider()
elif page == "STATISTICS":
    st.subheader("STATISTICAL INFORMATION")
    st.dataframe(df.describe(include= "all"))
    st.divider()
elif page == "MISSING VALUES":
    st.subheader("MISSING VALUES OF EACH COLUMNS")
    st.dataframe(df.isnull().sum())
    st.divider()
elif page == "GRAPHS":
    if graph == "BOX PLOT":
        st.subheader("BOX PLOT")
        fig = px.box(df, x="loan_status", y="income_annum",color="education", points="all",title="Income distribution by Loan status")
        fig.update_layout( title_x=0.5,template="plotly_white")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
        fig = px.box(df, x="loan_status", y="cibil_score",color="education", points="all", title="loan status vs cibil score")
        fig.update_layout( title_x=0.5,template="plotly_white",legend_title="Education")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
        fig = px.box(df, y=["residential_assets_value","commercial_assets_value","luxury_assets_value","bank_asset_value"],points="all", title="Distribution of Assets Values and Outliers")
        fig.update_layout( title_x=0.5,template="plotly_white",xaxis_title="Asset types",yaxis_title="Asset value")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "HISTOGRAM":
        st.subheader("HISTOGRAM")
        fig = px.histogram(df, x="income_annum", color="loan_status", text_auto=True,marginal="box", nbins=20, title="Income Distribution")
        fig.update_layout(title_x=0.5,template="plotly_white",width=1000, height=500,legend_title="Loan Status")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
        fig = px.histogram(df, x="cibil_score", color="loan_status", marginal="box",text_auto=True,nbins=30, title="CIBIL Score Distribution")
        fig.update_layout(title_x=0.5,template="plotly_white",width=1000, height=500,legend_title="Loan Status")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
        fig = px.histogram(df, x="education", color="loan_status", barmode="group",text_auto=True, title="Education vs loan status")
        fig.update_layout(title_x=0.5,template="plotly_white",xaxis_title="Education level",yaxis_title="Number of Applicants",legend_title="Loan Status")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
        fig = px.histogram(df, x="self_employed", color="loan_status", barmode="group",text_auto=True, title="Self employed vs loan status")
        fig.update_layout(title_x=0.5,template="plotly_white",xaxis_title="Self Employed",yaxis_title="Number of Applicants",legend_title="Loan Status")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "PARALLEL COORDINATES":
        st.subheader("PARALLEL COORDINATES")
        fig=px.parallel_coordinates(df,dimensions=["income_annum","loan_amount","loan_term","cibil_score"],color="cibil_score",color_continuous_scale=px.colors.sequential.Viridis,title="Parallel Coordinations Analysis")
        fig.update_layout(title_x=0.5,template="plotly_white",coloraxis_colorbar_title="CIBIL Score")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "SUNBURST GRAPH":
        st.subheader("SUNBURST GRAPH")
        fig=px.sunburst(df, path=["education","loan_status","self_employed"],title="Education, Loan status and Employment")
        fig.update_traces(textinfo="label+percent entry")
        fig.update_layout(title_x=0.5, template="plotly_white", width=700, height=500,margin=dict(t=50,l=20,r=20,b=20))
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "TREEMAP":
        st.subheader("TREEMAP")
        fig=px.treemap(df,path=["loan_status","education","self_employed"],title="Loan Status Hierarchy")
        fig.update_traces(textinfo="label+value")
        fig.update_layout(title_x=0.5,template="plotly_white",margin=dict(t=50,l=20,r=20,b=20))
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "PIE GRAPH":
        st.subheader("PIE GRAPH")
        fig = px.pie(df, names="education", title="Education Distribution",hole=0.4)
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(title_x=0.5, template="plotly_white", width=700, height=500,legend_title="Education")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
        fig = px.pie(df, names="self_employed", title="Self Employed",hole=0.4)
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(title_x=0.5, template="plotly_white", width=700, height=500,legend_title="Eployment Status")
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "SCATTER GRAPH":
        st.subheader("SCATTER GRAPH")
        fig = px.scatter(df, x="income_annum", y="loan_amount", color="loan_status", size="cibil_score", symbol="education", title="Relationship between income annum and loan amount")
        fig.update_layout( title_x=0.5,template="plotly_white",xaxis_title="Annual Income",yaxis_title="Loan Amount",legend_title="Loan Status",width=1200,height=700)
        fig.update_traces(marker=dict(line=dict(width=1)))
        st.plotly_chart(fig,use_container_width=True)
        st.divider()
    elif graph == "HEATMAP GRAPH":
        st.subheader("HEATMAP GRAPH")
        fig,ax=plt.subplots(figsize=(12,8))
        corr=df.select_dtypes(include="number").corr()
        sns.heatmap(corr, annot=True,cmap="coolwarm",ax=ax)
        st.pyplot(fig)
        st.divider()
    st.success("ANALYSIS COMPLETED SUCCESSFULLY")
    st.divider()
elif page == "CONCLUSION":
    st.subheader("CONCLUSION")
    st.write("""
    This Loan Approval Analysis project successfully demonstrates the complete process of data exploration, preprocessing, and visualization using Python and Streamlit. The dataset was carefully examined by analyzing its structure, removing unnecessary spaces, checking missing values and duplicates, and generating statistical summaries to improve data quality. 
    Interactive visualizations including Histogram, Box Plot, Scatter Plot, Pie Chart, Tree Map, Parallel Coordinates, Sunburst, and Heatmap were created to identify trends, compare different variables, and understand the relationships among applicant characteristics and loan-related attributes.
    The Streamlit application presents all analyses in a simple, interactive, and user-friendly interface, allowing users to explore the dataset efficiently. Overall, this project highlights the importance of data preprocessing and visualization in extracting meaningful insights, providing a strong foundation for future machine learning and loan approval prediction models.
    """)
    st.divider()