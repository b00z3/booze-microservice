import sklearn
import pandas as pd
import numpy as np
import pickle


with open('pickle_model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

knn_clf = pickle_model

def words(pred):
    liq = pred[-4:]
    price = pred[:4]
    if np.argmax(liq) == 0:
        liq_choice = 'beer'
    elif np.argmax(liq) == 1:
        liq_choice = 'wine'
    elif np.argmax(liq) == 2:
        liq_choice = 'spirits'
    else:
        liq_choice = 'refreshments'
        
    if price[np.argmax(liq)] > 0.66:
        price_point = 'expensive'
    elif price[np.argmax(liq)] > 0.33:
        price_point = 'average priced'
    else:
        price_point = 'cheap'
        
    return (liq_choice,price_point)

def avg(team):
    age=0
    gender = 0
    married = 0
    for n in team:
        age = (age) + (n['age']-19)/(100-19)
        gender = gender + ismale(n['gender'])
        married = married + n['married']
    print(age)
    age = age/len(team)
    gender = gender/len(team)
    married = married/len(team)
    return [age, gender, married]

def halfwaypoint(num):
    if num > 0.66:
        return 0.833
    elif num > 0.33:
        return 0.5
    else:
        return 0.167

def ismale(male):
    if male == 'Male':
        return 1
    else:
        return 0


def get_answers(team):
    pred = knn_clf.predict([avg(team)])
    beer_count = 0
    wine_count = 0
    spirits_count = 0
    refresh_count = 0
    count = 0
    for x in range(len(team)):
            choice, pricepoint = words(pred[0])

            if words(pred[0])[0] == 'beer':
                beer_count = beer_count + 1
                count = beer_count
            elif words(pred[0])[0] == 'wine':
                wine_count = wine_count + 1
                count = wine_count
            elif words(pred[0])[0] == 'spirits':
                spirits_count = spirits_count + 1
                cunt = spirits_count
            else:
                refresh_count = refresh_count + 1 
                count = refresh_count

            new_team_size = len(team) - count
            highest_price_index = np.argmax(pred[0][4:])

            pred[0][highest_price_index] = (
                new_team_size
                * pred[0][highest_price_index]
                - halfwaypoint(pred[0][highest_price_index])
            )/(new_team_size - 1)

            pred[0][np.argmax(pred[0][4:])+4] = pred[0][np.argmax(pred[0][4:])+4]-1/len(team)

    drink_tuples = zip(['beer(s)', 'wine(s)', 'spirit(s)'],[beer_count, wine_count, spirits_count])
    res = []
    for name, c in drink_tuples:
        if c > 0:
            
               res.append('You should buy {serve} serving(s) of {types}'.format(serve=c, types=name))
            
    return res
