from django import forms

class Booking_with_doctor(forms.Forms):
    docID = forms.HiddenField()
    patientID = forms.HiddenField()
    

