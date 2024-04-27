import joblib



def predict_am(adult_mortality):
    lr = joblib.load('model0.sav')
    return lr.predict([adult_mortality]) 


def predict_bmi(bmi):
    lr = joblib.load('model1.sav')
    return lr.predict([bmi])


def predict_alcohol(alcohol):
    lr = joblib.load('model2.sav')
    return lr.predict([alcohol])


def predict_expenditure(expenditure):
    lr = joblib.load('model3.sav')
    return lr.predict([expenditure])

def predict_population(population):
    lr = joblib.load('model4.sav')
    return lr.predict([population])