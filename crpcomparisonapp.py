import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

def create_categorical_bar_chart(data_series, title):
    # Convert the categorical data to strings
    data_series = data_series.astype(str)

    counts = data_series.value_counts()

    fig, ax = plt.subplots()
    bars = ax.bar(counts.index, counts.values)

    # Add counts on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, round(yval, 2), ha='center', va='bottom')

    plt.title(title)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    return fig

# Streamlit app
def main():
    st.title("CRP-Wise Response Summary Generator")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the data from the uploaded file
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('xlsx') else pd.read_csv(uploaded_file)

        # Specify the output directory for the charts
        output_directory = 'output_charts'

        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Specify the questions you want to plot and their corresponding titles and column names
        questions_to_plot = {
            'Photo in front of the house': ('Photo in front of the house', 'R Photo in front of the house', 'Photo in front of the house'),
    'Type of Residence': ('Type of Residence', 'R Type of Residence', 'Type of Residence'),
    'Owned or Rented': ('Owned or Rented', 'R Owned or Rented', 'Owned or Rented'),
    'Water Stagnation': ('Water Stagnation', 'R Water Stagnation', 'Water Stagnation'),
    'Garbage': ('Garbage', 'R Garbage', 'Garbage'),
    'Water Access': ('Water Access', 'R Water Access', 'Water Access'),
    'Water Storage': ('Water Storage', 'R Water Storage', 'Water Storage'),
    'Water Treatment': ('Water Treatment', 'R Water Treatment', 'Water Treatment'),
    'Toilet': ('Toilet', 'R Toilet', 'Toilet'),
    'Bathroom': ('Bathroom', 'R Bathroom', 'Bathroom'),
    'Soap': ('Soap', 'R Soap', 'Soap'),
    'Animals in the house': ('Animals in the house', 'R Animals in the house', 'Animals in the house'),
    'Type of animals': ('Type of animals','R Type of animals','Type of animals'),
    'Drain': ('Drain','R Drain','Drain'),
    'Photo of  ID card':('Photo of  ID card', 'R Photo of  ID card', 'Photo of  ID card'),
    'Gender': ('Gender', 'R Gender', 'Gender'), 
    'Phone Type': ('Phone Type', 'R Phone Type', 'Phone Type'),
    'Education': ('Education', 'R Education', 'Education'),
    'Occupation': ('Occupation', 'R Occupation', 'Occupation'),
    'Photo Front': ('Photo Front', 'R Photo Front', 'Photo Front'),
    'Photo Profile': ('Photo Profile', 'R Photo Profile', 'Photo Profile'),
    'Swelling L': ('Swelling L', 'R Swelling L', 'Swelling L'),
    'On elevation L': ('On elevation L', 'R On elevation L', 'On elevation L'),
    'Folds L': ('Folds L', 'R Folds L', 'Folds L'),
    'Knobs L': ('Knobs L', 'R Knobs L', 'Knobs L'),
    'Mossy Foot L': ('Mossy Foot L', 'R Mossy Foot L', 'Mossy Foot L'),
    'Interdigital lesion L': ('Interdigital lesion L', 'R Interdigital lesion L', 'Interdigital lesion L'),
    'Swelling R': ('Swelling R', 'R Swelling R', 'Swelling R'),
    'On elevation R': ('On elevation R', 'R On elevation R', 'On elevation R'),
    'Folds R': ('Folds R', 'R Folds R', 'Folds R'),
    'Knobs R': ('Knobs R', 'R Knobs R', 'Knobs R'),
    'Mossy Foot R': ('Mossy Foot R', 'R Mossy Foot R', 'Mossy Foot R'),
    'Interdigital lesion R': ('Interdigital lesion R', 'R Interdigital lesion R', 'Interdigital lesion R'),
    'Unilateral swelling of arms': ('Unilateral swelling of arms', 'R Unilateral swelling of arms', 'Unilateral swelling of arms'),
    'Breast Enlargement': ('Breast Enlargement', 'R Breast Enlargement', 'Breast Enlargement'),
    'Hydrocele': ('Hydrocele', 'R Hydrocele', 'Hydrocele'),
    'Acute attack': ('Acute attack', 'R Acute attack', 'Acute attack'),
    'Oral Abnormality 1': ('Oral Abnormality 1', 'R Oral Abnormality 1 (Colour of teeth condition)', 'Oral Abnormality 1'), 
    'Oral Abnormality 2': ('Oral Abnormality 2', 'R Oral Abnormality 2 (Gum condition)', 'Oral Abnormality 2'),
    'Oral abnormality 3': ('Oral abnormality 3', 'R Oral abnormality 3 (inner lip/ cheek condition)', 'Oral abnormality 3'),
    'Teeth Sensitivity': ('Teeth Sensitivity', 'R Teeth Sensitivity', 'Teeth Sensitivity'),
    'Brushing': ('Brushing', 'R Brushing', 'Brushing'),
    'Mouth': ('Mouth', 'R Mouth', 'Mouth'), 
    'Breath': ('Breath', 'R Breath', 'Breath'), 
    'Eye Image': ('Eye Image', 'R Eye Image', 'Eye Image'), 
    'Eye abnormality 1': ('Eye abnormality 1', 'R Eye abnormality 1 (colour)', 'Eye abnormality 1'), 
    'Eye abnormality 2': ('Eye abnormality 2', 'R Eye abnormality 2 (swelling+ discharge)', 'Eye abnormality 2'), 
    'Eye Exam -Vision': ('Eye Exam -Vision', 'R Eye Exam -Vision', 'Eye Exam -Vision'),
    'Ear images': ('Ear images', 'R Ear images', 'Ear images'),
    'Ear Abnormality 1': ('Ear Abnormality 1', 'R Ear Abnormality 1', 'Ear Abnormality 1'),
    'Ear': ('Ear', 'R Ear', 'Ear'),
    'Nose': ('Nose', 'R Nose', 'Nose'), 
    'Nasal problems': ('Nasal problems', 'R Nasal problems', 'Nasal problems'), 
    'Throat': ('Throat', 'R Throat', 'Throat'), 
    'Tonsils': ('Tonsils', 'R Tonsils', 'Tonsils'),
    'Breathing': ('Breathing','R Breathing', 'Breathing'),
    'Cough': ('Cough','R Cough', 'Cough'), 
    'Loss of Balance_dis orientation': ('Loss of Balance_dis orientation','R Loss of Balance/ dis orientation', 'Loss of Balance_dis orientation'),
    'Face 2 images': ('Face 2 images', 'R Face 2 images', 'Face 2 images'),
    'Facial exam': ('Facial exam','R Facial exam', 'Facial exam'), 
    'Face exam  (Sinus)': ('Face exam  (Sinus)', 'R Face exam  (Sinus)', 'Face exam  (Sinus)'),
    'Face exam (Head ache)': ('Face exam (Head ache)', 'R Face exam (Head ache)', 'Face exam (Head ache)'),
    'Nails Images': ('Nails Images', 'R Nails Images', 'Nails Images'),
    'Skin abnormality 1': ('Skin abnormality 1', 'R Skin abnormality 1', 'Skin abnormality 1'), 
    'Abnormality Locations': ('Abnormality Locations', 'R Abnormality Locations', 'Abnormality Locations'), 
    'Skin abnormality 2 - Growth_Lesion Morphology': ('Skin abnormality 2 - Growth_Lesion Morphology','R Skin abnormality 2 - Growth/Lesion Morphology', 'Skin abnormality 2 - Growth_Lesion Morphology'), 
    'Skin growth locations': ('Skin growth locations','R Skin growth locations', 'Skin growth locations'),
    'Skin abnormality 3': ('Skin abnormality 3','R Skin abnormality 3', 'Skin abnormality 3'), 
    'Skin Texture Locations': ('Skin Texture Locations', 'R Skin Texture Locations', 'Skin Texture Locations'),
    'Skin Abnormality 4 (Rash)': ('Skin Abnormality 4 (Rash)', 'R Skin Abnormality 4 (Rash)', 'Skin Abnormality 4 (Rash)'),
    'Ulcers anywhere in the body': ('Ulcers anywhere in the body','R Ulcers anywhere in the body', 'Ulcers anywhere in the body'),
    'Abnormality Locations': ('Abnormality Locations', 'R Abnormality Locations', 'Abnormality Locations'), 
    'Scar anywhere in the body': ('Scar anywhere in the body', 'R Scar anywhere in the body', 'Scar anywhere in the body'), 
    'Abnormality Locations': ('Abnormality Locations', 'R Abnormality Locations', 'Abnormality Locations'), 
    'Swelling anywhere in the body': ('Swelling anywhere in the body', 'R Swelling anywhere in the body', 'Swelling anywhere in the body'),
    'Abnormality Locations': ('Abnormality Locations', 'R Abnormality Locations', 'Abnormality Locations'),
    'Pain anywhere in the body': ('Pain anywhere in the body', 'R Pain anywhere in the body', 'Pain anywhere in the body'), 
    'Fever': ('Fever', 'R Fever', 'Fever'), 
    'Bowel Movement': ('Bowel Movement', 'R Bowel Movement', 'Bowel Movement'), 
    'Stool': ('Stool','R Stool', 'Stool'), 
    'Diarrhea': ('Diarrhea', 'R Diarrhea', 'Diarrhea'), 
    'Chest': ('Chest', 'R Chest', 'Chest'),
    'Urine': ('Urine', 'R Urine', 'Urine'), 
    'Vomiting_indigestion': ('Vomiting_indigestion', 'R Vomiting/ indigestion', 'Vomiting_indigestion'),
    'Menstruation' : ('Menstruation', 'R Menstruation (adult women only)', 'Menstruation'),
    'Vaginal problems': ('Vaginal problems', 'R Vaginal problems (adult women only)', 'Vaginal problems'), 
    'Do you worry too much daily in the morning': ('Do you worry too much daily in the morning', 'R Do you worry too much daily in the morning', 'Do you worry too much daily in the morning'), 
    'Feel happy': ('Feel happy', 'R Feel happy', 'Feel happy'), 
    'Feel depressed': ('Feel depressed', 'R Feel depressed', 'Feel depressed'), 
    'Do you worry at night affecting your sleep': ('Do you worry at night affecting your sleep', 'R Do you worry at night affecting your sleep', 'Do you worry at night affecting your sleep'), 
    'Trouble with sleep': ('Trouble with sleep', 'R Trouble with sleep', 'Trouble with sleep'), 
    'Feeling useful part of family': ('Feeling useful part of family', 'R Feeling useful part of family', 'Feeling useful part of family'), 
    'Managing finances': ('Managing finances', 'R Managing finances', 'Managing finances'), 
    'Taking any medications': ('Taking any medications', 'R Taking any medications', 'Taking any medications'), 
    'Under treatment for anemia': ('Under treatment for anemia', 'R Under treatment for anemia', 'Under treatment for anemia'), 
    'Under treatment for diabetes': ('Under treatment for diabetes', 'R Under treatment for diabetes', 'Under treatment for diabetes'), 
    'Under treatment for high BP_heart pain': ('Under treatment for high BP_heart pain', 'R Under treatment for high BP/ heart pain', 'Under treatment for high BP_heart pain'), 
    'Under treatment for thyroid': ('Under treatment for thyroid', 'R Under treatment for thyroid', 'Under treatment for thyroid'), 
    'Under treatment for cancer': ('Under treatment for cancer', 'R Under treatment for cancer', 'Under treatment for cancer'), 
    'Any known allergy': ('Any known allergy', 'R Any known allergy', 'Any known allergy'), 
    'Blood group': ('Blood group', 'R Blood group', 'Blood group'), 
    'Prescription': ('Prescription', 'R Prescription', 'Prescription'), 
    'Diagnostic test report': ('Diagnostic test report', 'R Diagnostic test report', 'Diagnostic test report'), 
    'Hospital admission past 1 year': ('Hospital admission past 1 year', 'R Hospital admission past 1 year', 'Hospital admission past 1 year'), 
    'Time taken to reach facility': ('Time taken to reach facility', 'R Time taken to reach facility', 'Time taken to reach facility'), 
    'Health facility visit past 1 year': ('Health facility visit past 1 year','R Health facility visit past 1 year', 'Health facility visit past 1 year'), 
    'Time taken to reach facility 1': ('Time taken to reach facility 1', 'R Time taken to reach facility 1', 'Time taken to reach facility 1'), 
    'Medicines from pharmacy past 1 year': ('Medicines from pharmacy past 1 year', 'R Medicines from pharmacy past 1 year', 'Medicines from pharmacy past 1 year'),
    'Time taken to vsisit facility_pharmacy': ('Time taken to vsisit facility_pharmacy', 'R Time taken to vsisit facility/ pharmacy', 'Time taken to vsisit facility_pharmacy'), 
    'Diagnostic test past 1 year': ('Diagnostic test past 1 year', 'R Diagnostic test past 1 year', 'Diagnostic test past 1 year'), 
    'Time taken to reach facility or pharmacy': ('Time taken to reach facility or pharmacy', 'R Time taken to reach facility or pharmacy', 'Time taken to reach facility or pharmacy'), 
    'Cigarettes per day': ('Cigarettes per day', 'R Cigarettes per day', 'Cigarettes per day'), 
    'Alcohol consumption daily': ('Alcohol consumption daily', 'R Alcohol consumption daily', 'Alcohol consumption daily'), 
    'Caffeine intake per day': ('Caffeine intake per day', 'R Caffeine intake per day', 'Caffeine intake per day'), 
    'Physical activities': ('Physical activities', 'R Physical activities', 'Physical activities'), 
    'Exercise per week': ('Exercise per week', 'R Exercise per week', 'Exercise per week') 
        }

        # Generate PNG for each plot and display in Streamlit
        for question_id, (question, column_name, title) in questions_to_plot.items():
            st.subheader(question)
            st.pyplot(create_categorical_bar_chart(df[column_name], title))

# Run the Streamlit app
if __name__ == '__main__':
    main()







