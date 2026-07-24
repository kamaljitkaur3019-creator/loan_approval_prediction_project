import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(page_title="🏦 LOAN APPROVAL ANALYSIS DASHBOARD", layout="wide")
st.sidebar.image("bank_logo.png",width=120)
st.sidebar.title("LOAN APPROVAL ANALYSIS DASHBOARD")
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
        "📊 EDA ANALYSIS",
        "📌 ABOUT",
    ]
)
st.sidebar.divider()
st.sidebar.markdown("### 🔄️ PROJECT WORKFLOW")
st.sidebar.write("📥 Load Dataset")
st.sidebar.write("🔍 Explore Data")
st.sidebar.write("🧹 Clean Data")
st.sidebar.write("📊 Visualize Data")
st.sidebar.write("💡 Generate Insights")
st.sidebar.write("🏁 Final Conclusion")
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
    st.subheader("📖 ABOUT PROJECT")
    st.write("""
    - This project is based on the Loan Approval Dataset collected from Kaggle.
    - The dataset was explored and preprocessed to understand its structure and improve data quality.
    - Various visualizations, including Box Plot, Histogram, Parallel Coordinates, Sunburst, Treemap, Pie Chart, Scatter Plot and Heatmap, were created to analyze patterns and identify important insights related to loan approval.
    - This project provides an interactive dashboard for analyzing loan approval data.
    - Different graphs are used to present the data in a clear and easy-to-understand format.
    - The dashboard helps users quickly explore the dataset and understand important patterns.
    """)
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
    st.subheader("🗂️ DATASET SOURCE")
    st.markdown("""
    This dataset was collected from **Kaggle** for educational purposes. This project uses a publicly available dataset for loan approval analysis. It contains loan applicants data for loan approval analysis.
    - **DATASET NAME:** Loan Approval Prediction Dataset
    - **SOURCE:** Kaggle
    - **LINK:** https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset 
    """)
    st.divider()
    st.info("📌 Use the sidebar to explore the Dataset, Data Exploration, Data Preprocessing and About Section.")
    st.divider()
elif menu == "📂 DATASET":
    st.title("🏦 LOAN APPROVAL ANALYSIS")
    st.divider()
    st.subheader("ℹ️ INTRODUCTION OF PROJECT")
    st.write("""
    - The dataset used in this project was collected from Kaggle for educational and analytical purposes.
    - This project analyzes loan approval data to understand the factors that affect loan approval decisions.
    - The dataset includes applicant details such as income, CIBIL score, education, employment status, loan amount, and assets.
    - Different data visualization techniques are used to identify patterns, trends, and relationships in the dataset.
    - The main goal of this project is to gain useful insights from the data and better understand the loan approval process.
    """)
    st.divider()
    st.subheader("🗂️ LOAN APPROVAL DATASET")
    st.dataframe(df)
    st.write("""
    - Displays the complete loan approval dataset used for analysis.
    - It provides an overview of all records and features available in the dataset.
    """)
    st.divider()
    st.success("Dataset Loaded Successfully ✅")
    st.divider()
    st.title("🔍 DATA EXPLORATION")
    st.info("This section provides a quick overview of the dataset.")
    st.divider()
    st.subheader("🏷️ COLUMNS NAME")
    st.dataframe(pd.DataFrame({"Column Names": df.columns}))
    st.write("""
    - Shows the names of all columns present in the dataset.
    - It helps identify the available features used for analysis and visualization.
    """)
    st.divider()
    st.subheader("🔝 FIRST FIVE ROWS OF DATASET")
    st.dataframe(df.head())
    st.write("""
    - Displays the first five records of the dataset.
    - It provides a quick preview of the data structure and values.
    """)
    st.subheader("🔚 LAST FIVE ROWS OF DATASET")
    st.dataframe(df.tail())
    st.write("""
    - Displays the last five records of the dataset.
    - It helps verify the ending entries and overall data consistency.
    """)
    st.divider()
    st.subheader("📐 SHAPE OF DATASET(ROWS AND COLUMNS)")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
    st.write("""
    - Shows the total number of rows and columns in the dataset.
    - It gives an overview of the dataset size and dimensions.
    """)
    st.divider()
    st.subheader("🧩 DATA TYPES")
    st.dataframe(df.dtypes.reset_index())
    st.write("""
    - Displays the data type of each column, such as integer, float, or object.
    - It helps understand the format of data before preprocessing and analysis.
    """)
    st.divider()
    st.subheader("📉 STATISTICAL INFORMATION")
    st.dataframe(df.describe(include= "all"))
    st.write("""
    - Provides statistical summaries such as count, mean, standard deviation, minimum, and maximum values.
    - It helps understand the overall distribution and characteristics of the dataset.
    """)
    st.divider()
    st.success("✅ Data Exploration Completed Successfully")
    st.divider()
    st.title("🧹 DATA PREPROCESSING")
    st.info("This section shows the preprocessing steps performed on the dataset.")
    st.divider()
    st.subheader("🪄 REMOVING EXTRA SPACES")
    df.columns=df.columns.str.strip()
    df.columns
    st.write("""
    - Removes unnecessary spaces from column names.
    - It ensures consistent column names and prevents errors during analysis.
    """)
    st.divider()
    st.subheader("🚫 MISSING VALUES OF EACH COLUMNS")
    st.dataframe(df.isnull().sum())
    st.write("""
    - Displays the number of missing values in each column.
    - It helps identify incomplete data that may require preprocessing.
    - No missing values were found in the dataset, so no data imputation was required.
    """)
    st.divider()
    st.subheader("♻️ DUPLICATE VALUES")
    duplicates = df.duplicated().sum()
    st.write("Duplicate values:", duplicates)
    st.write("""
    - Shows the total number of duplicate records in the dataset.
    - It helps detect repeated entries that could affect analysis accuracy.
    - No duplicate values were found, so no duplicates were removed.
    """)
    st.divider()
    st.success("✅ Data Preprocessing Completed Successfully")
elif menu == "📊 EDA ANALYSIS":
    st.title("📊 EDA ANALYSIS")
    st.info("This section shows the graphical visualization performed on the dataset.")
    st.divider()
    st.subheader("Income Distribution by Loan Status")
    fig = px.box(df, x="loan_status", y="income_annum",color="education", points="all")
    fig.update_layout(template="plotly_white",xaxis_title="Loan Status",yaxis_title="Income Annum",legend_title="Education")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph compares applicant's annual income for Approved and Rejected loan applications.
    - It shows the income spread (minimum, maximum, median, and quartiles) for each loan status.
    - The colors represent education level, making it easy to compare income distribution across different education groups.
    - It helps identify whether income has an impact on loan approval.
    - It also highlights income variation and outliers, making applicant comparison easier.
    """)
    st.divider()
    st.subheader("Loan Status vs CIBIL Score")
    fig = px.box(df, x="loan_status", y="cibil_score",color="education", points="all")
    fig.update_layout(template="plotly_white",xaxis_title="Loan Status",yaxis_title="CIBIL Score",legend_title="Education")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph compares CIBIL scores of applicants with Approved and Rejected loans.
    - It shows the distribution, median, and outliers of CIBIL scores for each loan status.
    - The colors represent education level, making it easier to compare credit scores across different education groups.
    - It helps determine whether CIBIL score influences loan approval.
    - It also identifies score variations and outliers among applicants.
    """)
    st.divider()
    st.subheader("Distribution of Assets Values and Outliers")
    fig = px.box(df, y=["residential_assets_value","commercial_assets_value","luxury_assets_value","bank_asset_value"],points="all")
    fig.update_layout(template="plotly_white",xaxis_title="Asset types",yaxis_title="Asset value")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph compares the value distribution of residential, commercial, luxury, and bank assets.
    - It shows the median, spread, and range of each asset type.
    - It identifies outliers, indicating applicants with unusually high or low asset values.
    - It helps compare the financial strength of different asset types.
    - It also detects outliers, which are useful for understanding unusual applicant profiles.
    """)
    st.divider()
    st.subheader("Income Distribution")
    fig = px.histogram(df, x="income_annum", color="loan_status", text_auto=True,marginal="box", nbins=20)
    fig.update_layout(template="plotly_white",width=1000, height=500,xaxis_title="Income Annum",legend_title="Loan Status")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows how annual income is distributed among all applicants.
    - The colors compare the number of Approved and Rejected loan applications across different income ranges.
    - The box plot on top highlights the income spread, median, and outliers.
    - It helps understand the overall income pattern of loan applicants.
    - It also shows how loan approval varies across different income levels.
    """)
    st.divider()
    st.subheader("CIBIL Score Distribution")
    fig = px.histogram(df, x="cibil_score", color="loan_status", marginal="box",text_auto=True,nbins=30)
    fig.update_layout(template="plotly_white",width=1000, height=500,xaxis_title="CIBIL Score",legend_title="Loan Status")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows the distribution of CIBIL scores among all loan applicants.
    - The colors compare the Approved and Rejected loan applications across different CIBIL score ranges.
    - The box plot displays the median, spread, and outliers of CIBIL scores.
    - It helps analyze the credit score pattern of applicants.
    - It also shows how loan approval is related to different CIBIL score ranges.
    """)
    st.divider()
    st.subheader("Education vs Loan Status")
    fig = px.histogram(df, x="education", color="loan_status", barmode="group",text_auto=True)
    fig.update_layout(template="plotly_white",xaxis_title="Education level",yaxis_title="Number of Applicants",legend_title="Loan Status")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph compares the number of Approved and Rejected loan applications for each education level.
    - It shows which education group has more applicants.
    - It helps identify whether loan approval differs across education levels.
    - It helps compare loan approval rates between different education groups.
    - It provides insight into the relationship between education and loan status.
    """)
    st.divider()
    st.subheader("Self Employed vs Loan Status")
    fig = px.histogram(df, x="self_employed", color="loan_status", barmode="group",text_auto=True)
    fig.update_layout(template="plotly_white",xaxis_title="Self Employed",yaxis_title="Number of Applicants",legend_title="Loan Status")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph compares the number of Approved and Rejected loan applications for self-employed and non-self-employed applicants.
    - It shows which employment category has more loan applicants.
    - It helps identify whether self-employment status affects loan approval.
    - It helps compare loan approval rates based on employment type.
    - It provides insight into the relationship between self-employment and loan status.
    """)
    st.divider()
    st.subheader("Parallel Coordinations Analysis")
    fig=px.parallel_coordinates(df,dimensions=["income_annum","loan_amount","loan_term","cibil_score"],color="cibil_score",color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(template="plotly_white",coloraxis_colorbar_title="CIBIL Score")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph compares income, loan amount, loan term, and CIBIL score for each applicant in a single view.
    - The line color represents the CIBIL score, making it easy to identify applicants with higher and lower credit scores.
    - It helps detect patterns and relationships between multiple loan-related features at the same time.
    - It helps analyze multiple applicant attributes simultaneously instead of one by one.
    - It makes it easier to identify trends, patterns, and unusual applicant profiles (outliers).
    """)
    st.divider()
    st.subheader("Education, Loan status and Employment")
    fig=px.sunburst(df, path=["education","loan_status","self_employed"])
    fig.update_traces(textinfo="label+percent entry")
    fig.update_layout(template="plotly_white", width=700, height=500,margin=dict(t=50,l=20,r=20,b=20))
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows the hierarchical relationship between education, loan status, and self-employment.
    - It displays the percentage and proportion of applicants in each category.
    - It helps identify which education and employment groups have more approved or rejected loans.
    - It helps visualize multiple categorical variables in a single chart.
    - It makes it easier to understand the distribution and relationship between education, employment, and loan status.
    """)
    st.divider()
    st.subheader("Loan Status Hierarchy")
    fig=px.treemap(df,path=["loan_status","education","self_employed"])
    fig.update_traces(textinfo="label+value")
    fig.update_layout(template="plotly_white",margin=dict(t=50,l=20,r=20,b=20))
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows the hierarchical distribution of applicants by loan status, education, and self-employment.
    - The size of each box represents the number of applicants in that category.
    - It helps identify which education and employment groups have more approved or rejected loans.
    - It provides a clear hierarchical view of the loan applicant data.
    - It helps compare the size and distribution of different applicant groups quickly.
    """)
    st.divider()
    st.subheader("Education Distribution")
    fig = px.pie(df, names="education", hole=0.4)
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(template="plotly_white", width=700, height=500,legend_title="Education")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows the percentage distribution of applicants across different education levels.
    - It identifies which education category has the highest and lowest number of applicants.
    - It provides a quick overview of the composition of the dataset based on education.
    - It helps understand the proportion of applicants in each education group.
    - It makes category comparison simple and visually clear.
    """)
    st.divider()
    st.subheader("Self Employed")
    fig = px.pie(df, names="self_employed",hole=0.4)
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(template="plotly_white", width=700, height=500,legend_title="Eployment Status")
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows the percentage distribution of self-employed and non-self-employed applicants.
    - It identifies which employment category has more applicants.
    - It provides a quick overview of the employment composition of the dataset.
    - It helps understand the proportion of applicants by employment status.
    - It makes it easy to compare self-employed and non-self-employed groups at a glance.
    """)
    st.divider()
    st.subheader("Relationship between Income Annum and Loan Amount")
    fig = px.scatter(df, x="income_annum", y="loan_amount", color="loan_status", size="cibil_score", symbol="education")
    fig.update_layout(template="plotly_white",xaxis_title="Annual Income",yaxis_title="Loan Amount",legend_title="Loan Status",width=1200,height=700)
    fig.update_traces(marker=dict(line=dict(width=1)))
    st.plotly_chart(fig,use_container_width=True)
    st.write("""
    - The graph shows the relationship between annual income and loan amount for each applicant.
    - The color indicates loan status, the bubble size represents CIBIL score, and the symbol represents education level.
    - It helps identify trends, clusters, and unusual applicant profiles (outliers) in the data.
    - It helps analyze how income is related to the loan amount requested.
    - It combines multiple applicant attributes in one graph, making comparison easier.
    """)
    st.divider()
    st.subheader("Relationship between Numerical Features")
    fig,ax=plt.subplots(figsize=(12,8))
    corr=df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True,cmap="coolwarm",ax=ax)
    st.pyplot(fig)
    st.write("""
    - The graph shows the correlation between all numerical variables in the dataset.
    - Warmer colors (red) indicate a stronger positive correlation, while cooler colors (blue) indicate a weaker or negative correlation.
    - It helps identify which features are strongly related and which are not.
    - It helps understand the relationships between numerical features in the dataset.
    - It is useful for finding important variables and detecting multicollinearity before analysis or model building.
    """)
    st.divider()
    st.success("✅ Graphical Visualization Completed Successfully")
    st.divider()
elif menu == "📌 ABOUT":
    st.title("📌 PROJECT CONCLUSION")
    st.write("""
    - This project analyzes the Loan Approval Dataset using Python and Streamlit.
    - Data exploration, preprocessing, and interactive visualizations were used to understand the dataset and identify important patterns.
    - The dashboard presents the analysis in a simple, clear, and user-friendly way, making it easier to understand the factors related to loan approval.
    """)
    st.divider()
    st.subheader("🗂️ DATASET SOURCE")
    st.markdown("""
    This dataset was collected from **Kaggle** for educational purposes. This project uses a publicly available dataset for loan approval analysis. It contains loan applicants data for loan approval analysis.
    - **DATASET NAME:** Loan Approval Prediction Dataset
    - **SOURCE:** Kaggle
    - **LINK:** https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset 
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
    st.subheader("📝 SUMMARY")
    st.write("""
    - This project analyzes loan applicant data using different data visualization techniques.
    - It examines important factors such as income, CIBIL score, education, employment status, loan amount, and assets.
    - The analysis helps identify patterns and relationships that influence loan approval decisions.
    - Various charts and graphs are used to present the data in a clear and easy-to-understand way.
    - Overall, the project provides meaningful insights into the loan approval process and applicant profiles.
    """)
    st.divider()
    st.subheader("🎯 WHY DID WE CHOOSE THIS PROJECT?")
    st.write("""
    - We chose the Loan Approval Analysis project because it is a real-world problem used by banks and financial institutions.
    - It is easy to understand, provides meaningful insights through data analysis, and helps us apply Python, data preprocessing, and data visualization skills in a practical way.
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