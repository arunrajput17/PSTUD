####Store environmental variables in text file
##Don't hardcode
##Don't check sensitive values into source control
## .env file
# DATABASE = Sample_Connection_String


# app.py
from dotenv import load_dotenv
load_dotenv()
import os

password = os.getenv('PASSWORD')

print(password)


##Final Notes
# Don't hardcode sensitive information **EVER**
# Use dotenv for a simple solution
#Add .env to .gitignore
# Consider full encryption options
# Azure Key Vault