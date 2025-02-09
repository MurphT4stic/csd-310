from dotenv import dotenv_values

secrets = dotenv_values(".env")

print("Loaded secrets:", secrets)