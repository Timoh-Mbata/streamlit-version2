import json
import numpy as np
import joblib as jb
import streamlit as st
# loading the model
model  =jb.load(model.joblib)
with open('columns.json','r') as column:
    col = json.load(column)

# Title and welcome message
st.title('Welcome to AccessLink!')
st.subheader('Predicting Financial Inclusion in Africa')

st.write("Fill in the information below to make predictions about financial inclusion:")


# Title and welcome message
st.title('Welcome to AccessLink!')
st.subheader('Predicting Financial Inclusion in Africa')

st.write("Fill in the information below to make predictions about financial inclusion:")

# Dropdowns for user input
country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])
location_type = st.selectbox("Location Type", ["Rural", "Urban"])
cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])
household_size = st.number_input("Household Size", min_value=1, max_value=20, step=1)
age_of_respondent = st.number_input("Age of Respondent", min_value=18, max_value=100, step=1)
gender_of_respondent = st.selectbox("Gender", ["Female", "Male"])
relationship_with_head = st.selectbox("Relationship with Head", ["Head of Household", "Spouse", "Child", "Parent",
                                                                 "Other Relative", "Non-Relative"])
marital_status = st.selectbox("Marital Status", ["Married/Living together", "Widowed", "Single/Never Married",
                                                 "Divorced/Separated", "Don't know"])
education_level = st.selectbox("Education Level", ["Secondary education", "No formal education", "Vocational/Specialised training",
                                                   "Primary education", "Tertiary education", "Other/Don't know/RTA"])
job_type = st.selectbox("Job Type", ["Self employed", "Government Dependent", "Formally employed Private", "Informally employed",
                                     "Formally employed Government", "Farming and Fishing", "Remittance Dependent",
                                     "Other Income", "Don't Know/Refuse to answer", "No Income"])
EPI = st.number_input("Economic Potential Index (EPI)", min_value=0.0, max_value=1.0, step=0.01)
SSI = st.number_input("Social Security Index (SSI)", min_value=0.0, max_value=1.0, step=0.01)
SOCIAL_ECONOMIC_STATUS = st.number_input("Social Economic Status", min_value=0, max_value=10, step=1)

# Age group logic based on the input age
if age_of_respondent <= 18:
    age_group = 0
elif 19 <= age_of_respondent <= 34:
    age_group = 1
elif 35 <= age_of_respondent <= 63:
    age_group = 2
else:
    age_group = 3

# Label encoding logic - Categorical feature mappings to numerical
country_mapping = {"Kenya": 0, "Rwanda": 1, "Tanzania": 2, "Uganda": 3}
location_type_mapping = {"Rural": 0, "Urban": 1}
cellphone_access_mapping = {"Yes": 1, "No": 0}
gender_mapping = {"Female": 0, "Male": 1}
relationship_mapping = {
    "Head of Household": 0, "Spouse": 1, "Child": 2, "Parent": 3,
    "Other Relative": 4, "Non-Relative": 5
}
marital_status_mapping = {
    "Married/Living together": 0, "Widowed": 1, "Single/Never Married": 2,
    "Divorced/Separated": 3, "Don't know": 4
}
education_level_mapping = {
    "Secondary education": 0, "No formal education": 1, "Vocational/Specialised training": 2,
    "Primary education": 3, "Tertiary education": 4, "Other/Don't know/RTA": 5
}
job_type_mapping = {
    "Self employed": 0, "Government Dependent": 1, "Formally employed Private": 2,
    "Informally employed": 3, "Formally employed Government": 4, "Farming and Fishing": 5,
    "Remittance Dependent": 6, "Other Income": 7, "Don't Know/Refuse to answer": 8, "No Income": 9
}

# Convert categorical inputs to numerical
country_encoded = country_mapping[country]
location_type_encoded = location_type_mapping[location_type]
cellphone_access_encoded = cellphone_access_mapping[cellphone_access]
gender_encoded = gender_mapping[gender_of_respondent]
relationship_encoded = relationship_mapping[relationship_with_head]
marital_status_encoded = marital_status_mapping[marital_status]
education_level_encoded = education_level_mapping[education_level]
job_type_encoded = job_type_mapping[job_type]

# Prepare the input data with the transformed values
input_data = np.array([[country_encoded, location_type_encoded, cellphone_access_encoded, household_size,
                        gender_encoded, marital_status_encoded, education_level_encoded, job_type_encoded,
                        EPI, SSI, SOCIAL_ECONOMIC_STATUS, age_group]])

# Button to make prediction
if st.button('Predict'):
    # Perform prediction using your model
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction == 1:
        st.success("This individual is likely to have or use a bank account.")
    else:
        st.warning("This individual is unlikely to have or use a bank account.")
