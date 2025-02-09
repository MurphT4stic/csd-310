import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Load .env file
secrets = dotenv_values(".env")

# Debugging step: print loaded secrets
print("Loaded secrets:", secrets)

# Ensure required keys exist
required_keys = ["USER", "PASSWORD", "HOST", "DATABASE"]
for key in required_keys:
    if key not in secrets:
        raise KeyError(f"Missing {key} in .env file")

# Database configuration
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]
    ))

    input("\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
