from django.contrib import admin
from .models import Demande,Avis,Competance,Solution,Article,Prediction,PredictionChurn
import csv
from django.http import HttpResponse

class PredictionAdmin(admin.ModelAdmin):

    def export_to_csv(seld,request,queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="predictions.csv"'

        writer = csv.writer(response)
        writer.writerow([
    'Marque', 'Modele', 'Annee_Modele', 'Type_de_carburant',
    'Puissance_fiscale', 'Kilometrage', 'etat', 'Boite_de_vitesses',
    'Nombre_de_portes', 'Origine', 'Premiere_main', 'Jantes_aluminium',
    'Airbags', 'Climatisation', 'Systeme_de_navigation_GPS', 'Toit_ouvrant',
    'Sieges_cuir', 'Radar_de_recul', 'Camera_de_recul', 'Vitres_electriques',
    'ABS', 'ESP', 'Regulateur_de_vitesse', 'Limiteur_de_vitesse',
    'CD_MP3_Bluetooth', 'Ordinateur_de_bord',
    'Verrouillage_centralise_a_distance', 'price_model1', 'price_model2',
    'price_model3'
])
        
        for prediction in queryset:
            writer.writerow([
        prediction.Marque, prediction.Modele, prediction.Annee_Modele,
        prediction.Type_de_carburant, prediction.Puissance_fiscale,
        prediction.Kilometrage, prediction.etat, prediction.Boite_de_vitesses,
        prediction.Nombre_de_portes, prediction.Origine, prediction.Premiere_main,
        prediction.Jantes_aluminium, prediction.Airbags,
        prediction.Climatisation, prediction.Systeme_de_navigation_GPS,
        prediction.Toit_ouvrant, prediction.Sieges_cuir,
        prediction.Radar_de_recul, prediction.Camera_de_recul,
        prediction.Vitres_electriques, prediction.ABS, prediction.ESP,
        prediction.Regulateur_de_vitesse, prediction.Limiteur_de_vitesse,
        prediction.CD_MP3_Bluetooth, prediction.Ordinateur_de_bord,
        prediction.Verrouillage_centralise_a_distance,
        prediction.price_model1, prediction.price_model2, prediction.price_model3
    ])
        return response
    
    export_to_csv.short_description = 'Export to CSV'

    actions = [export_to_csv]



class PredictionChurnAdmin(admin.ModelAdmin):
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="predictions_churn.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'TotalCharges', 'tenure', 'Contract_Month_to_month',
            'InternetService_Fiber_optic', 'PaymentMethod_Electronic_check',
            'TechSupport_No', 'OnlineSecurity_No', 'SeniorCitizen',
            'PaperlessBilling_Yes', 'StreamingTV_Yes', 'StreamingMovies_Yes',
            'Contract_Two_year', 'InternetService_DSL', 'MultipleLines_No',
            'PaperlessBilling_No', 'PaymentMethod_Credit_card', 'TechSupport_Yes',
            'OnlineSecurity_Yes', 'PhoneService_Yes', 'Dependents_Yes',
            'prediction_lr', 'prediction_rf', 'prediction_svm', 'created_at'
        ])

        for prediction in queryset:
            writer.writerow([
                prediction.TotalCharges, prediction.tenure, prediction.Contract_Month_to_month,
                prediction.InternetService_Fiber_optic, prediction.PaymentMethod_Electronic_check,
                prediction.TechSupport_No, prediction.OnlineSecurity_No, prediction.SeniorCitizen,
                prediction.PaperlessBilling_Yes, prediction.StreamingTV_Yes, prediction.StreamingMovies_Yes,
                prediction.Contract_Two_year, prediction.InternetService_DSL, prediction.MultipleLines_No,
                prediction.PaperlessBilling_No, prediction.PaymentMethod_Credit_card, prediction.TechSupport_Yes,
                prediction.OnlineSecurity_Yes, prediction.PhoneService_Yes, prediction.Dependents_Yes,
                prediction.prediction_lr, prediction.prediction_rf, prediction.prediction_svm, prediction.created_at
            ])

        return response

    export_to_csv.short_description = 'Export to CSV'

    actions = [export_to_csv]


# Register your models here.
admin.site.register(Demande)
admin.site.register(Avis)
admin.site.register(Competance)
admin.site.register(Solution)
admin.site.register(Article)
admin.site.register(Prediction,PredictionAdmin)
admin.site.register(PredictionChurn,PredictionChurnAdmin)

    
