from django.db import models
class rol (models.model):
        nombre=models.textfield ("nombre")
        

        class vehiculo (models.model):
            placa=models.TextField ("placa")
            categoria=models.TextField ("categoria")
            usuario_id=models.integerfield ("usuario_id")
            hora_fecha=models.TextField ("hora_fecha")
            entrada_y_salida=models.TextField ("entrada_y_salida")
            servicia_id=models.intergerfield ("servicios_id")
                        
