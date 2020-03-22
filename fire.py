"""
FIRE🔥
Model - This file contains classes that interact with the GOSH FHIR backend in order to retrieve
and analyse anonymous patient data

The file is titled fire as it uses the FHIR standard, albeit, through an API
"""

from fhir_parser import FHIR
from earth import *
from math import ceil, floor


class FireData:
    def __init__(self):
        fhir = FHIR(endpoint='https://fhir.compositegrid.com:5001/api/')
        self.patients = fhir.get_all_patients()

    def get_marital_data(self):
        marital_status = {}
        for patient in self.patients:
            if str(patient.marital_status) in marital_status:
                marital_status[str(patient.marital_status)] += 1
            else:
                marital_status[str(patient.marital_status)] = 1
        return marital_status

    def get_data_totals(self, field):
        data = {}
        for patient in self.patients:
            data_type = self.get_data_type(field, patient)
            if data_type in data:
                data[data_type] += 1
            else:
                data[data_type] = 1
        return data

    def get_data_type(self, field, patient):
        if field == NAME:
            return patient.name
        if field == GENDER:
            return patient.gender
        if field == BIRTHDAY or field == AGE:
            return self.get_age_range(patient)
        if field == MARITAL:
            return str(patient.marital_status)
        if field == MULTIPLE_BIRTH:
            return patient.multiple_birth

    @staticmethod
    def get_age_range(patient):
        age = patient.age()
        return str(int(floor(age / 10.0)) * 10) + "-" + str(int(ceil(age / 10.0)) * 10)
