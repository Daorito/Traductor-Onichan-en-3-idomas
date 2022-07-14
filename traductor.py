#Importamos de la libreria google trans la funcion de traductor

from googletrans import Translator

translator = Translator()

#Programa para todas las traduciones

textoDeSalidaEN = translator.translate('Onichan', dest='en')
textoDeSalidaRU = translator.translate('Onichan', dest='ru')
textoDeSalidaFR = translator.translate('Onichan', dest='fr')

#Esto es para que las traduccionés salgan en pantalla

print("--------ONICHAN EN INGLÉS:--------")
print(textoDeSalidaEN)
print("--------ONICHAN EN RUSO:--------")
print(textoDeSalidaRU)
print("--------ONICHAN EN FRANCÉS:--------")
print(textoDeSalidaFR)
