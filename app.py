import streamlit as st
import numpy as np
from predict import predict_am, predict_bmi, predict_alcohol, predict_expenditure,predict_population



st.title('Life Expectancy Prediction')
st.write('---')
st.write('This is a web app that predicts the life expectancy of a person based on the features provided by the user.The features on which life expectancy depends are:')
st.write('Adult Mortality')
st.write('Body Mass Index')
st.write('Alcohol Consumption Frequency')
st.write('Average Total Expenditure')
st.write('Population')


st.write('---')
st.write('  ')



st.write('Enter the values of the features to predict the life expectancy of a person')



text="<span style='color:red;font-size:20px'>**1) Adult Mortality**</span>"
st.markdown(text, unsafe_allow_html=True)
st.write('Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population')
if st.button('Country wise adult mortality rate'):
    st.write('Find the adult mortality rate of your region here: https://data.worldbank.org/indicator/SP.DYN.AMRT.MA')
am=st.number_input('Enter adult mortality rate of your region', min_value=1, max_value=723, value=1, step=1)



st.write('  ')
st.write('   ')
st.write('   ')



text="<span style='color:red;font-size:20px'>**2) Body Mass Index**</span>"
st.markdown(text, unsafe_allow_html=True)
if st.button('Calculate BMI'):
    st.write('Calculate your BMI here: https://www.calculator.net/bmi-calculator.html')
bmi=st.slider('Enter your body mass index', min_value=0, max_value=70, value=18, step=1)



st.write('  ')
st.write('   ')
st.write('   ')



text="<span style='color:red;font-size:20px'>**3) Alcohol Consumption Frequency**</span>"
st.markdown(text, unsafe_allow_html=True)
st.write('   ')
st.write("Alcohol consumption frequency is the average number of drinks consumed per day by an individual over a lifetime in scale of 1-10.")
options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12","13","14","15","16","17","18","19","20"]
selected_option = st.selectbox("Select an option", options)
selected_option = int(selected_option)




st.write('  ')
st.write('   ')
st.write('   ')



text="<span style='color:red;font-size:20px'>**4) Average Total Expenditure**</span>"
st.markdown(text, unsafe_allow_html=True)
st.text("Average total expenditure is the average amount spent by a person on health per year in USD in scale of 1-20.")
selected_option2 = st.selectbox("Select appropriate option", options)
selected_option2 = int(selected_option2)



st.write('  ')
st.write('   ')
st.write('   ')

text="<span style='color:red;font-size:20px'>**5) Population**</span>"
st.markdown(text, unsafe_allow_html=True)
st.write('Enter the population of your region in lakhs')
population=st.number_input('Enter adult mortality rate of your region', min_value=0,max_value=1293859294,  value=0, step=1)



st.write('   ')
st.write('   ')
st.write('   ')
st.write('   ')
st.write('   ')




if st.button('Predict'):
    am = predict_am([am])
    am=am[0][0]
    print("Adult Mortality")
    print(am)
    bmi=predict_bmi([bmi])
    bmi=bmi[0][0]
    print("BMI")
    print(bmi)
    # print(type(selected_option))
    alcohol=predict_alcohol([selected_option])
    alcohol=alcohol[0][0]
    print("Alcohol")
    print(alcohol)
    expenditure=predict_expenditure([selected_option2])
    expenditure=expenditure[0][0]
    print("Expenditure")
    print(expenditure)
    
    population=predict_population([population])
    
    life=(am+bmi+alcohol+expenditure+population)/5
    print(life)
    st.write("Life Expectancy of the person is")
    st.write(life[0][0])