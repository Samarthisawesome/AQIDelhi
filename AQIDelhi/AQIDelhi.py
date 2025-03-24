import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "AQIDelhi/delhi_combined.csv"
df = pd.read_csv(file_path)

# Streamlit App
def main():
    st.title("New Delhi AQI Data")
    st.write("AQI of New Delhi from 2020 to 2024.")
    
    # Sidebar
    st.sidebar.header("Options")
    show_data = st.sidebar.checkbox("Show Dataframe")
    show_summary = st.sidebar.checkbox("Show Summary Statistics")
    
    if show_data:
        st.subheader("Dataset Preview")
        st.dataframe(df)
    
    if show_summary:
        st.subheader("Summary Statistics")
        st.write(df.describe())
    
    # Select columns for visualization
    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if numerical_cols:  # Ensure there are numerical columns
        selected_x = st.sidebar.selectbox("Select X-axis:", numerical_cols)
        selected_y = st.sidebar.selectbox("Select Y-axis:", numerical_cols)
        plot_type = st.sidebar.selectbox("Select plot type:", ["scatter", "line", "bar", "histogram", "boxplot"])

        # Plot the graph
        fig, ax = plt.subplots()
        if plot_type == "scatter":
            sns.scatterplot(x=df[selected_x], y=df[selected_y], ax=ax)
        elif plot_type == "line":
            sns.lineplot(x=df[selected_x], y=df[selected_y], ax=ax)
        elif plot_type == "bar":
            sns.barplot(x=df[selected_x], y=df[selected_y], ax=ax)
        elif plot_type == "histogram":
            sns.histplot(df[selected_x], kde=True, ax=ax)
        elif plot_type == "boxplot":
            sns.boxplot(x=df[selected_x], ax=ax)

        st.pyplot(fig)
    else:
        st.warning("No numerical columns found in the dataset.")

if __name__ == "__main__":
    main()
