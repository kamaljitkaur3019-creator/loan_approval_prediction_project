import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(page_title="🏦 LOAN APPROVAL ANALYSIS DASHBOARD", layout="wide")
st.sidebar.image("bank_logo.png",width=120)
st.sidebar.title("LOAN APPROVAL ANALYSIS DASHBOARD")
st.divider()
@st.cache_data
def load_data():
    df=pd.read_csv("loan_approval_dataset.csv")
    df.columns=df.columns.str.strip()
    return df
df = load_data()
st.sidebar.divider()
menu = st.sidebar.selectbox(
    "SELECT SECTION",
    [
        "🏠 HOME",
        "📂 DATASET",
        "🔍 DATA EXPLORATION",
        "🧹 DATA PREPROCESSING",
        "📊 VISUALIZATION",
        "📌 CONCLUSION",
        "ℹ️ ABOUT"
    ]
)
st.sidebar.divider()
st.sidebar.markdown("### 🔄️ PROJECT WORKFLOW")
st.sidebar.write("📥 Load Dataset")
st.sidebar.write("🔍 Explore Data")
st.sidebar.write("🧹 Clean Data")
st.sidebar.write("📊 Visualize Data")
st.sidebar.write("💡 Generate Insights And Final Conclusion")
st.sidebar.write("✅ About The Project")
st.sidebar.divider()
if menu == "🏠 HOME":
    st.title("🏦 LOAN APPROVAL ANALYSIS DASHBOARD")
    st.markdown(
        """
        Welcome to the **LOAN APPROVAL ANALYSIS DASHBOARD**.
        This dashboard provides a complete analysis of the Loan Approval Dataset using data exploration, data preprocessing and graphical visualization.
        """
    )
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📄 TOTAL RECORDS", df.shape[0])
    with col2:
        st.metric("📋 TOTAL COLUMNS", df.shape[1])
    with col3:
        st.metric("❌ MISSING VALUES", df.isnull().sum().sum())
    st.divider()
    st.subheader("🎯 PROJECT OBJECTIVES")
    st.markdown("""
    - Analyze the LOAN APPROVAL DATASET USIBNG Python and Streamlit.
    - Perform data exploration and data preprocessing for better data understanding.
    - Visualize key insights through an interactive Streamlit Dashboard. 
    """)
    st.markdown("---")
    st.write("🛠️ TECHNOLOGIES USED")
    st.write("- Python")
    st.write("- Pandas")
    st.write("- NumPy")
    st.write("- Plotly")
    st.write("- Seaborn")
    st.write("- Matplotlib")
    st.write("- Streamlit")
    st.markdown("---")
    st.info("📌 Use the sidebar to explore the Dataset, Data Exploration, Data Preprocessing and About Section.")
elif menu == "📂 DATASET":
    st.title("LOAN APPROVAL DATASET")
    st.dataframe(df)
    st.success("Dataset Loaded Successfully ✅")
    st.divider()
elif menu == "🔍 DATA EXPLORATION":
    st.title("🔍 DATA EXPLORATION")
    st.info("This section provides a quick overview of the dataset.")
    st.subheader("COLUMNS NAME")
    st.dataframe(pd.DataFrame({"Column Names": df.columns}), use_container_width=True)
    st.divider()
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
    st.subheader("STATISTICAL INFORMATION")
    st.dataframe(df.describe(include= "all"))
    st.divider()
    st.success("✅ Data Exploration Completed Successfully")
elif menu == "🧹 DATA PREPROCESSING":
    st.title("🧹 DATA PREPROCESSING")
    st.info("This section shows the preprocessing steps performed on the dataset.")
    st.subheader("REMOVING EXTRA SPACES")
    df.columns=df.columns.str.strip()
    df.columns
    st.divider()
    st.subheader("MISSING VALUES OF EACH COLUMNS")
    st.dataframe(df.isnull().sum())
    st.divider()
    st.subheader("DUPLICATE VALUES")
    duplicates = df.duplicated().sum()
    st.write("Duplicate values:", duplicates)
    st.divider()
    st.success("✅ Data Preprocessing Completed Successfully")
elif menu == "📊 VISUALIZATION":
    st.title("📊 VISUALIZATION")
    st.info("This section shows the graphical visualization performed on the dataset.")
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
    st.subheader("PARALLEL COORDINATES")
    fig=px.parallel_coordinates(df,dimensions=["income_annum","loan_amount","loan_term","cibil_score"],color="cibil_score",color_continuous_scale=px.colors.sequential.Viridis,title="Parallel Coordinations Analysis")
    fig.update_layout(title_x=0.5,template="plotly_white",coloraxis_colorbar_title="CIBIL Score")
    st.plotly_chart(fig,use_container_width=True)
    st.divider()
    st.subheader("SUNBURST GRAPH")
    fig=px.sunburst(df, path=["education","loan_status","self_employed"],title="Education, Loan status and Employment")
    fig.update_traces(textinfo="label+percent entry")
    fig.update_layout(title_x=0.5, template="plotly_white", width=700, height=500,margin=dict(t=50,l=20,r=20,b=20))
    st.plotly_chart(fig,use_container_width=True)
    st.divider()
    st.subheader("TREEMAP")
    fig=px.treemap(df,path=["loan_status","education","self_employed"],title="Loan Status Hierarchy")
    fig.update_traces(textinfo="label+value")
    fig.update_layout(title_x=0.5,template="plotly_white",margin=dict(t=50,l=20,r=20,b=20))
    st.plotly_chart(fig,use_container_width=True)
    st.divider()
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
    st.subheader("SCATTER GRAPH")
    fig = px.scatter(df, x="income_annum", y="loan_amount", color="loan_status", size="cibil_score", symbol="education", title="Relationship between income annum and loan amount")
    fig.update_layout( title_x=0.5,template="plotly_white",xaxis_title="Annual Income",yaxis_title="Loan Amount",legend_title="Loan Status",width=1200,height=700)
    fig.update_traces(marker=dict(line=dict(width=1)))
    st.plotly_chart(fig,use_container_width=True)
    st.divider()
    st.subheader("HEATMAP GRAPH")
    fig,ax=plt.subplots(figsize=(12,8))
    corr=df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True,cmap="coolwarm",ax=ax)
    st.pyplot(fig)
    st.divider()
    st.success("✅ Graphical Visualization Completed Successfully")
    st.divider()
elif menu == "📌 CONCLUSION":
    st.title("📌 PROJECT CONCLUSION")
    st.write("""
    This project analyzes the Loan Approval Dataset using Python and Streamlit.
    Data exploration, preprocessing, and interactive visualizations were used to understand the dataset and identify important patterns.
    The dashboard presents the analysis in a simple, clear, and user-friendly way, making it easier to understand the factors related to loan approval.
    """)
    st.divider()
    st.subheader("💡 KEY FINDING")
    st.markdown("""
    - Applicants with higher CIBIL scores have a greater chance of loan approval.
    - Higher annual income is generally associated with better loan approval chances.
    - Education and self-employment status influence loan approval patterns.
    - Interactive visualizations make it easier to identify trends and understand the dataset.
    """)
    st.divider()
    st.success("✅ Project completed successfully with meaningful insights")
    st.divider()
elif menu == "ℹ️ ABOUT":
    st.title("ℹ️ ABOUT")
    st.write("""
    This project is based on the Loan Approval Dataset collected from Kaggle.
    The dataset was explored and preprocessed to understand its structure and improve data quality.
    Various visualizations, including Box Plot, Histogram, Parallel Coordinates, Sunburst, Treemap, Pie Chart, Scatter Plot and Heatmap, were created to analyze patterns and identify important insights related to loan approval.
    This project provides an interactive dashboard for analyzing loan approval data.
    Different graphs are used to present the data in a clear and easy-to-understand format.
    The dashboard helps users quickly explore the dataset and understand important patterns.
    """)
    st.divider()
    st.subheader("🎯 WHY DID WE CHOOSE THIS PROJECT?")
    st.write("""
    We chose the Loan Approval Analysis project because it is a real-world problem used by banks and financial institutions.
    It is easy to understand, provides meaningful insights through data analysis, and helps us apply Python, data preprocessing, and data visualization skills in a practical way.
    """)
    st.divider()
    st.subheader("🚀 FUTURE SCOPE")
    st.markdown("""
    - This project can be extended by adding machine learning models to predict loan approval automatically.
    - It can be integrated with bank systems to support faster and more accurate loan decisions.
    - More features and real-time data can be added to improve the analysis and make the dashboard more useful.
    """)
    st.divider()
    st.subheader("✅ BENEFITS OF THIS PROJECT")
    st.markdown("""
    - It helps understand the factors that affect loan approval.
    - It presents complex data in a simple and interactive dashboard.
    - It supports better analysis and decision-making through visualizations.
    - It improves data analysis and visualization skills using Python and Streamlit.
    """)
    st.divider()
    st.success("✅ Loan Approval Analysis Dashboard Completed Successfully")
    st.divider()