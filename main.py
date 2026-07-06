# Importo a funcao do MEU proprio modulo (o arquivo organizar.py)
from organizar import organizar_pasta

# Agora NADA dispara so por importar. Sou EU quem decide a hora de chamar.
print(">>> Cheguei no main.py. Agora sim EU escolho organizar:")
organizar_pasta("pasta_baguncada")
