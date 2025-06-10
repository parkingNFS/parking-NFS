from django.db import models
class servicio (models.model):
                nombre=models.TextField ("nombre")
                tipo_de_servicios=models.TextField ("tipo_de_servicio")
                tiempo_de_servicio=models.TextField ("tiempo_de_servicio")
                autolavado=models.TextField ("autolavdo")
                cotos_adicionales=models.TextField ("costos_adicionales")

                        
