from django.db import models

class tiempo (models.model):
                    precio=models.TextField ("precio")
                    factura_de_salida=models.TextField ("factura_de_salida")
                    hora=models.TextField ("hora")
                    mes=models.TextField ("mes")
                    semana=models.TextField ("semana")

