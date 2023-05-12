# utils.py
import joblib
import os
from sklearn.preprocessing import LabelEncoder


# Définir le chemin vers le dossier contenant les modèles
MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Models')

# Charger les modèles
RandomForestRegressor_model = joblib.load(os.path.join(MODELS_DIR, 'RandomForestRegressor_model.pkl'))
KNeighborsRegressor_model = joblib.load(os.path.join(MODELS_DIR, 'KNeighborsRegressor_model.pkl'))
DecisionTreeRegressor_model = joblib.load(os.path.join(MODELS_DIR, 'DecisionTreeRegressor_model.pkl'))

# Charger les encodeurs de label
LE = joblib.load(os.path.join(MODELS_DIR, 'LE.pkl'))
LE1 = joblib.load(os.path.join(MODELS_DIR, 'LE1.pkl'))
LE2 = joblib.load(os.path.join(MODELS_DIR, 'LE2.pkl'))
LE3 = joblib.load(os.path.join(MODELS_DIR, 'LE3.pkl'))
LE4 = joblib.load(os.path.join(MODELS_DIR, 'LE4.pkl'))
LE6 = joblib.load(os.path.join(MODELS_DIR, 'LE6.pkl'))
LE7 = joblib.load(os.path.join(MODELS_DIR, 'LE7.pkl'))

def predict(form_data):
    Marque = form_data['Marque']
    Modele = form_data['Modele']
    Annee_Modele = form_data['Annee_Modele']
    Type_de_carburant = form_data['Type_de_carburant']
    Puissance_fiscale = form_data['Puissance_fiscale']
    Kilometrage = form_data['Kilometrage']

    car = [
        LE.transform([Marque])[0],
        LE1.transform([Modele])[0],
        Annee_Modele,
        int(Kilometrage.split('-')[0].replace(' ', '')) + int(Kilometrage.split('-')[1].replace(' ', '')) / 2,
        LE2.transform([Type_de_carburant])[0],
        Puissance_fiscale,
        LE3.transform([form_data.get('Boite_de_vitesses', 'Manuelle')])[0],
        form_data.get('Nombre_de_portes', 5),
        LE4.transform([form_data.get('Origine', 'WW au Maroc')])[0],
        LE7.transform([form_data.get('Premiere_main', 'Non')])[0],
        LE6.transform([form_data.get('etat', 'Très bon')])[0],
        form_data.get('Jantes_aluminium', False),
        form_data.get('Airbags', False),
        form_data.get('Climatisation', False),
        form_data.get('Systeme_de_navigation_GPS', False),
        form_data.get('Toit_ouvrant', False),
        form_data.get('Sieges_cuir', False),
        form_data.get('Radar_de_recul', False),
        form_data.get('Camera_de_recul', False),
        form_data.get('Vitres_electriques', False),
        form_data.get('ABS', False),
        form_data.get('ESP', False),
        form_data.get('Regulateur_de_vitesse', False),
        form_data.get('Limiteur_de_vitesse', False),
        form_data.get('CD_MP3_Bluetooth', False),
        form_data.get('Ordinateur_de_bord', False),
        form_data.get('Verrouillage_centralise_a_distance', False)
    ]

    predictions = [
        round(RandomForestRegressor_model.predict([car])[0], 2),
        round(KNeighborsRegressor_model.predict([car])[0], 2),
        round(DecisionTreeRegressor_model.predict([car])[0], 2)
    ]

    return predictions

