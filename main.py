# News Bot by Raphaël DENNI aka SlyEyes

# Import
from assets.imports import *

# Variables
load_dotenv()
token = getenv('TOKEN')

# Create the client
client = commands.Bot(intents=discord.Intents.default())

# Load cogs
for file in listdir("./cogs"):
    if file.endswith(".py"):
        client.load_extension("cogs." + file[:-3])

client.run(token)

"""
   Copyright 2022 Raphaël Denni

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
