
from django.forms import ModelForm,TextInput,EmailInput,Select
from .models import Persona,Mascota

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su nombre'}),
            'apellido':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese sus apellidos'}),
            'genero':TextInput(attrs={'class':'form-controli', 'placeholder':'Genero (Masculino o Femenino)'}),
            'identificacion':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su identificacion'}),
            'correo':EmailInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su correo electronico'}),
            'telefono':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su telefono fijo'}),
            'mobil':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su celular','value':''}),
            'direccion':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su direccion','value':''}),
            'ciudad':TextInput(attrs={'class':'form-controli', 'placeholder':'Ingrese su ciudad','value':''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'persona':Select(attrs={'class':'form-controli',}),
            'nombre':TextInput(attrs={'class':'form-controli' ,'placeholder':'Nombre' }),
            'apellidos':TextInput(attrs={'class':'form-controli' ,'placeholder':'Apellidos' }),
            'especie':TextInput(attrs={'class':'form-controli' ,'placeholder':'Especie' }),
            'color':TextInput(attrs={'class':'form-controli' ,'placeholder':'Color' }),
            'edad':TextInput(attrs={'class':'form-controli' ,'placeholder':'Edad' }),
            'decendencia':TextInput(attrs={'class':'form-controli','placeholder':'Ha tenido decendencia?'}),
            'enfermedades':TextInput(attrs={'class':'form-controli','placeholder':'Ha tenido enfermedades?'}),
            'cirugias':TextInput(attrs={'class':'form-controli','placeholder':'Ha tenido cirugias?'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
