import sklearn
import pandas as pd 
import numpy as np
import pickle 
from collections import Counter

with open('pickle_model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)
knn_clf = pickle_model
totals = ['20 to 24 years of age Female Asian', '20 to 24 years of age Female Black', '20 to 24 years of age Female First Nations', 
'20 to 24 years of age Female Hawaiian or Pacific Islander', '20 to 24 years of age Female Two or more races', 
'20 to 24 years of age Female White', '20 to 24 years of age Male Asian', '20 to 24 years of age Male Black', 
'20 to 24 years of age Male First Nations', '20 to 24 years of age Male Hawaiian or Pacific Islander', 
'20 to 24 years of age Male Two or more races', '20 to 24 years of age Male White', '25 to 29 years of age Female Asian', 
'25 to 29 years of age Female Black', '25 to 29 years of age Female First Nations', 
'25 to 29 years of age Female Hawaiian or Pacific Islander', '25 to 29 years of age Female Two or more races',
'25 to 29 years of age Female White', '25 to 29 years of age Male Asian', '25 to 29 years of age Male Black',
'25 to 29 years of age Male First Nations', '25 to 29 years of age Male Hawaiian or Pacific Islander', 
'25 to 29 years of age Male Two or more races', '25 to 29 years of age Male White', '30 to 34 years of age Female Asian', 
'30 to 34 years of age Female Black', '30 to 34 years of age Female First Nations', '30 to 34 years of age Female Hawaiian or Pacific Islander',
'30 to 34 years of age Female Two or more races', '30 to 34 years of age Female White', '30 to 34 years of age Male Asian',
'30 to 34 years of age Male Black', '30 to 34 years of age Male First Nations', '30 to 34 years of age Male Hawaiian or Pacific Islander', 
'30 to 34 years of age Male Two or more races', '30 to 34 years of age Male White', '35 to 39 years of age Female Asian', 
'35 to 39 years of age Female Black', '35 to 39 years of age Female First Nations', '35 to 39 years of age Female Hawaiian or Pacific Islander', 
'35 to 39 years of age Female Two or more races', '35 to 39 years of age Female White', '35 to 39 years of age Male Asian', 
'35 to 39 years of age Male Black', '35 to 39 years of age Male First Nations', '35 to 39 years of age Male Hawaiian or Pacific Islander', 
'35 to 39 years of age Male Two or more races', '35 to 39 years of age Male White', '40 to 44 years of age Female Asian', 
'40 to 44 years of age Female Black', '40 to 44 years of age Female First Nations', 
'40 to 44 years of age Female Hawaiian or Pacific Islander', '40 to 44 years of age Female Two or more races', 
'40 to 44 years of age Female White', '40 to 44 years of age Male Asian', '40 to 44 years of age Male Black', 
'40 to 44 years of age Male First Nations', '40 to 44 years of age Male Hawaiian or Pacific Islander', 
'40 to 44 years of age Male Two or more races', '40 to 44 years of age Male White', '45 to 49 years of age Female Asian', 
'45 to 49 years of age Female Black', '45 to 49 years of age Female First Nations', '45 to 49 years of age Female Hawaiian or Pacific Islander', '45 to 49 years of age Female Two or more races', '45 to 49 years of age Female White', '45 to 49 years of age Male Asian', '45 to 49 years of age Male Black', '45 to 49 years of age Male First Nations', '45 to 49 years of age Male Hawaiian or Pacific Islander', '45 to 49 years of age Male Two or more races', '45 to 49 years of age Male White', '50 to 54 years of age Female Asian', '50 to 54 years of age Female Black', '50 to 54 years of age Female First Nations', '50 to 54 years of age Female Hawaiian or Pacific Islander', '50 to 54 years of age Female Two or more races', '50 to 54 years of age Female White', '50 to 54 years of age Male Asian', '50 to 54 years of age Male Black', '50 to 54 years of age Male First Nations', '50 to 54 years of age Male Hawaiian or Pacific Islander', '50 to 54 years of age Male Two or more races', '50 to 54 years of age Male White', '55 to 59 years of age Female Asian', '55 to 59 years of age Female Black', '55 to 59 years of age Female First Nations', '55 to 59 years of age Female Hawaiian or Pacific Islander', '55 to 59 years of age Female Two or more races', '55 to 59 years of age Female White', '55 to 59 years of age Male Asian', '55 to 59 years of age Male Black', '55 to 59 years of age Male First Nations', '55 to 59 years of age Male Hawaiian or Pacific Islander', '55 to 59 years of age Male Two or more races', '55 to 59 years of age Male White', '60 to 64 years of age Female Asian', '60 to 64 years of age Female Black', '60 to 64 years of age Female First Nations', '60 to 64 years of age Female Hawaiian or Pacific Islander', '60 to 64 years of age Female Two or more races', '60 to 64 years of age Female White', '60 to 64 years of age Male Asian', '60 to 64 years of age Male Black', '60 to 64 years of age Male First Nations', '60 to 64 years of age Male Hawaiian or Pacific Islander', '60 to 64 years of age Male Two or more races', '60 to 64 years of age Male White', '65 to 69 years of age Female Asian', '65 to 69 years of age Female Black', '65 to 69 years of age Female First Nations', '65 to 69 years of age Female Hawaiian or Pacific Islander', '65 to 69 years of age Female Two or more races', '65 to 69 years of age Female White', '65 to 69 years of age Male Asian', '65 to 69 years of age Male Black', '65 to 69 years of age Male First Nations', '65 to 69 years of age Male Hawaiian or Pacific Islander', '65 to 69 years of age Male Two or more races', '65 to 69 years of age Male White', '70 to 74 years of age Female Asian', '70 to 74 years of age Female Black', '70 to 74 years of age Female First Nations', '70 to 74 years of age Female Hawaiian or Pacific Islander', '70 to 74 years of age Female Two or more races', '70 to 74 years of age Female White', '70 to 74 years of age Male Asian', '70 to 74 years of age Male Black', '70 to 74 years of age Male First Nations', '70 to 74 years of age Male Hawaiian or Pacific Islander', '70 to 74 years of age Male Two or more races', '70 to 74 years of age Male White', '75 to 79 years of age Female Asian', '75 to 79 years of age Female Black', '75 to 79 years of age Female First Nations', '75 to 79 years of age Female Hawaiian or Pacific Islander', '75 to 79 years of age Female Two or more races', '75 to 79 years of age Female White', '75 to 79 years of age Male Asian', '75 to 79 years of age Male Black', '75 to 79 years of age Male First Nations', '75 to 79 years of age Male Hawaiian or Pacific Islander', '75 to 79 years of age Male Two or more races', '75 to 79 years of age Male White', '80 to 84 years of age Female Asian', '80 to 84 years of age Female Black', '80 to 84 years of age Female First Nations', '80 to 84 years of age Female Hawaiian or Pacific Islander', '80 to 84 years of age Female Two or more races', '80 to 84 years of age Female White', '80 to 84 years of age Male Asian', '80 to 84 years of age Male Black', '80 to 84 years of age Male First Nations', '80 to 84 years of age Male Hawaiian or Pacific Islander', '80 to 84 years of age Male Two or more races', '80 to 84 years of age Male White', '85 years of age and over Female Asian', '85 years of age and over Female Black', '85 years of age and over Female First Nations', '85 years of age and over Female Hawaiian or Pacific Islander', '85 years of age and over Female Two or more races', '85 years of age and over Female White', '85 years of age and over Male Asian', '85 years of age and over Male Black', '85 years of age and over Male First Nations', '85 years of age and over Male Hawaiian or Pacific Islander', '85 years of age and over Male Two or more races', '85 years of age and over Male White']

def words(pred):
    if np.argmax(pred) == 0:
        liq_choice = 'brandy'
    elif np.argmax(pred) == 1:
        liq_choice = 'distilled'
    elif np.argmax(pred) == 2:
        liq_choice = 'gin'
    elif np.argmax(pred) == 3:
        liq_choice = 'liqueur'
    elif np.argmax(pred) == 4:
        liq_choice = 'rum'
    elif np.argmax(pred) == 5:
        liq_choice = 'schnapps'
    elif np.argmax(pred) == 6:
        liq_choice = 'tequila'
    elif np.argmax(pred) == 7:
        liq_choice = 'vodka'
    elif np.argmax(pred) == 8:
        liq_choice = 'whiskey'
        
    return liq_choice
# input number of people on team and a vector of their demographics
def liquor_list(n,dem):
    pred = knn_clf.predict([dem])
    choices = np.chararray(n, itemsize = 15)
    
    for x in range(n):
        choices[x] = words(pred)
        pred[0][np.argmax(pred[0][:])] = pred[0][np.argmax(pred[0][:])] - 1/n
    return choices

def get_answers(team):
    people_vec = []
    dic = {key: index for index, key in enumerate(totals)} # makes a dict of the indexes {"30 to 32 ... " : 2}
    final_vec= [0]*len(dic) #vector of 0,s
    for members in team :
        least_dig = members['age'] % 10  # 2
        sig_dig = members['age'] - least_dig  #30
      
        
        if (least_dig < 5 ) : #fals in the less than 5 cat
            
            age = str(sig_dig) + " to " + str(sig_dig + 4 ) + " years of age "
            gender = members['sex']
            race = members['race']
            people_vec.append(age + gender + " " + race )
            
        else: # fals in greater than 5 
            age = str(sig_dig + 5) + " to " + str(sig_dig + 9 ) + " years of age "
            gender = members['sex']
            race = members['race']
            people_vec.append(age + gender + " " + race )
    
    for people in people_vec:
        final_vec[dic[people]] = 1
    return liquor_list(len(team),final_vec)
