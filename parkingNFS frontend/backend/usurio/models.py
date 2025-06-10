from django.db import models

# Create your models here.
class usuarios (models.model):
    nombre=models.TextField ("nombre")
    apellido=models.TextField ("apellido")
    rol_id=models.integerfield ("rol")
    

    class rol (models.model):
        nombre=models.textfield ("nombre")
        

        class vehiculo (models.model):
            placa=models.TextField ("placa")
            categoria=models.TextField ("categoria")
            usuario_id=models.integerfield ("usuario_id")
            hora_fecha=models.TextField ("hora_fecha")
            entrada_y_salida=models.TextField ("entrada_y_salida")
            servicia_id=models.intergerfield ("servicios_id")


            class servicio (models.model):
                nombre=models.TextField ("nombre")
                tipo_de_servicios=models.TextField ("tipo_de_servicio")
                tiempo_de_servicio=models.TextField ("tiempo_de_servicio")
                autolavado=models.TextField ("autolavdo")
                cotos_adicionales=models.TextField ("costos_adicionales")

                class tiempo (models.model):
                    precio=models.TextField ("precio")
                    factura_de_salida=models.TextField ("factura_de_salida")
                    hora=models.TextField ("hora")
                    mes=models.TextField ("mes")
                    semana=models.TextField ("semana")


                    class facturacion (models.TextField):
                        vehiculo_id=models.IntegerField ("vehiculos_id")
                        total_a_pagar=models.TextField ("total_a_pagar")
                         
                        
