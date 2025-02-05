import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("First Streamlit App")
    st.write("Here you can do EDA on any dataset")
    upload_file = st.sidebar.file_uploader('Upload your file',type=['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            
            else:
                data = pd.read_excel(upload_file)
            
            st.sidebar.success('File uploaded successfully')

            st.subheader('Data Preview')
            st.dataframe(data.head())

            st.subheader('Basic Information')
            st.write('Shape of the data:', data.shape)
            st.write('Columns in the data:', data.columns)
            st.write('Missing values:', data.isnull().sum())

            st.subheader('Data Statistics')
            st.write(data.describe())
            

            st.subheader('Data Visualization')
            fig = plt.figure(figsize=(10, 6))
            sns.countplot(x='age',data=data,hue='sex',palette='dark')
            st.pyplot(fig)

        

        except Exception as e:
            st.sidebar.error(f'Error: {e}')



if __name__ == '__main__':
    main()
        