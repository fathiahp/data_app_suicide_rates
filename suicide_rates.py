# import modules
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# GLOBAL VARIABLE

APP_TITLE = 'Exploratory Data Analysis (EDA) on Suicide Rates'
APP_MESSAGE = """
    *“Suicide is one of the leading causes of death among all American adults and rates are increasing in both men and women” (SSM Health). 
    From a 2017 study, 89% of suicide attempt survivors said their actions were impulsive. 52% of the survivors said they would’ve reconsidered their actions had they received care and support. 
    This dashboard aims to show data regarding suicidal rates that could be further used in terms of suicide prevention.*
    """
USER_QUOTE = [
    "It's a beautiful day! - You",
    "Be happy with the beautiful things that make you, you. - Beyonce",
    "You can't stop the waves, but you can learn to swim. - Jon Kabat Zinn",
    "The point is to pay back kindness but to pass it on - Julia Alvarez",
    "What if you stayed? What beautiful things could be waiting for you? - Anna Akana",
    "Everything is going to be okay in the end. If it is not okay, it's not the end. - Unknown"]
APP_SIDEBAR_TITLE = "Side Panel"
APP_SIDEBAR_MARKDOWN = "Explore the dataset and create your own visualization!"
APP_SIDEBAR_INFO = "[Kaggle Source](https://www.kaggle.com/goyalshalini93/suicide-rate-eda/) | [Dataset](https://www.kaggle.com/goyalshalini93/suicide-rate-eda/data)"

# Simulated data

@st.cache
def load_data():
    data = pd.read_csv(
        'master.csv',
        encoding="ISO-8859-1")
    data = data.rename(columns={'gdp_per_capita ($)': 'gdp_per_capita'})
    data = data.drop_duplicates(keep='first')
    return data

def main():
    st.set_page_config(layout="wide")

    # generate data
    suicide_rate = load_data()

    st.title(APP_TITLE)
    st.selectbox('Choose a happy thought :)', USER_QUOTE)
    st.markdown(APP_MESSAGE)
    st.sidebar.title(APP_SIDEBAR_TITLE)
    st.sidebar.markdown(APP_SIDEBAR_MARKDOWN)

    # showing the original raw data
    if st.sidebar.checkbox("Show Raw Data", False):
        st.header('Dataset')
        data_load_state = st.text('Loading dataset...')
        st.write(suicide_rate)
        data_load_state.text('Loading dataset: completed!')

    # quick explore
    st.sidebar.subheader("Quick Explore")
    st.sidebar.markdown("Tick to explore the dataset.")
    if st.sidebar.checkbox('Basic info'):
        if st.sidebar.checkbox('Dataset Quick Look'):
            st.subheader('Dataset Quick Look:')
            st.write(suicide_rate.head())
        if st.sidebar.checkbox("Show Columns"):
            st.subheader('Show Columns List')
            all_columns = suicide_rate.columns.to_list()
            st.write(all_columns)
        if st.sidebar.checkbox('Statistical Description'):
            st.subheader('Statistical Data Descripition')
            st.write(suicide_rate.describe())
        if st.sidebar.checkbox('Missing Values?'):
            st.subheader('Missing values')
            st.write(suicide_rate.isnull().sum())

    # visualization
    st.sidebar.subheader('Create Visualization')
    st.sidebar.markdown("Tick to create your own visualization.")

    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.info("If error, please adjust column name on side panel.")
        column_count_plot = st.sidebar.selectbox(
            "Choose a column to plot. Try selecting sex ",
            suicide_rate.columns)
        plt.figure(figsize=(8, 6))

        fig = sns.countplot(x=column_count_plot, data=suicide_rate)
        if column_count_plot == 'ï»¿country':
            fig.set(xticklabels=[])
        st.pyplot()

    if st.sidebar.checkbox('Histogram | Distplot'):
        st.subheader('Histogram | Distplot')
        st.info("If error, please adjust column name on side panel.")
        column_dist_plot = st.sidebar.selectbox(
            "Choose a column to plot. Try selecting gdp_per_capita",
            suicide_rate.columns)

        fig = sns.distplot(suicide_rate[column_dist_plot])
        st.pyplot()

    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("If error, please adjust column name on side panel.")
        column_box_plot_x = st.sidebar.selectbox(
            "X (choose a column). Try selecting sex",
            suicide_rate.columns.insert(
                0,
                None))
        column_box_plot_y = st.sidebar.selectbox(
            "Y (choose a column). Try selecting year", suicide_rate.columns)

        fig = sns.boxplot(
            x=column_box_plot_x,
            y=column_box_plot_y,
            data=suicide_rate,
            palette="Set3")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    # dataset info
    st.sidebar.info(APP_SIDEBAR_INFO)

if __name__ == "__main__":
    main()
