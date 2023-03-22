from assets.imports import requests, loads, getenv, embed_msg


async def api_request(interaction, sources, keyword):
    api_key = getenv('API_KEY')

    if api_key is None:
        await embed_msg(
            interaction,
            "API key error",
            "You need to set your API key first !"
        )

        return None

    # Request's URL
    api_url = \
        f"https://newsapi.org/v2/everything" \
        f"?domains={sources}" \
        f"&q={keyword}" \
        f"&sortBy=publishedAt" \
        f"&sortBy=popularity" \
        f"&apiKey={api_key}"

    # Request to News API
    try:
        req = requests.get(api_url)

    except ConnectionError as err:
        await embed_msg(
            interaction,
            "Connection error",
            f"Can't connect to the API ! Verify your API key and try again !\nDetail : \n{err}"
        )

        return None

    else:
        # JSON data to Python dictionary
        content = loads(req.content)

        if content['status'] == 'error' and content['code'] == 'apiKeyInvalid':
            await embed_msg(
                interaction,
                "API key error",
                "Your API key is invalid ! Verify your API key and try again !"
            )

            return None

        # Collect articles' data and send it to Discord
        total_results = str(content['totalResults'])

        return content


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
