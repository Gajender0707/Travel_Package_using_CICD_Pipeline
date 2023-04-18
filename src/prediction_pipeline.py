import pandas as pd
import numpy as np

class Dataframe:

    def __init__(self,age,typeofcontact,citytier,durationofpitch,occupation,gender,
                      numberofpersonvisiting,numberoffollowups,productpitched,prefferedpropertystar,
                      maritalstatus,numberoftrips,passport, pitchsatisfactionscore,owncar,
                      numberofchildrenvisiting,designation,monthlyincome):
        
        self.age=age
        self.typeofcontact=typeofcontact
        self.citytier=citytier
        self.durationofpitch=durationofpitch
        self.occupation=occupation
        self.gender=gender
        self.numberofpersonvisiting=numberofpersonvisiting
        self.numberoffollowups=numberoffollowups
        self.productpitched=productpitched
        self.prefferedpropertystar=prefferedpropertystar
        self.maritalstatus=maritalstatus
        self.numberoftrips=numberoftrips
        self.passport=passport
        self.pitchsatisfactionscore=pitchsatisfactionscore
        self.owncar=owncar
        self.numberofchildrenvisiting=numberofchildrenvisiting
        self.designation=designation
        self.monthlyincome=monthlyincome
    
    def get_values_as_dataframe(self):
        
        custom_data_points={
            "Age":[self.age],
            "TypeofContact":[self.typeofcontact],
            "CityTier":[self.citytier],
            "DurationOfPitch":[self.durationofpitch],
            "Occupation":[self.occupation],
            "Gender":[self.gender],
            "NumberOfPersonVisiting":[self.numberofpersonvisiting],
            "NumberOfFollowups":[self.numberoffollowups],
            "ProductPitched":[self.productpitched],
            "PreferredPropertyStar":[self.prefferedpropertystar],
            "MaritalStatus":[self.maritalstatus],
            "NumberOfTrips":[self.numberoftrips],
            "Passport":[self.passport],
            "PitchSatisfactionScore":[self.pitchsatisfactionscore],
            "OwnCar":[self.owncar],
            "NumberOfChildrenVisiting":[self.numberofchildrenvisiting],
            "Designation":[self.designation],
            "MonthlyIncome":[self.monthlyincome]
        }

        df=pd.DataFrame(custom_data_points)
        return df




