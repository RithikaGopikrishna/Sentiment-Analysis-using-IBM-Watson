from newsapi.newsapi_client import NewsApiClient
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

authenticator = IAMAuthenticator('cIcEmIFE4K73r7kGwzxbR_M-x1peReu3DM9o0WfgcdlO')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
newsapi=NewsApiClient(api_key="c650b6441dd24b2991ec29a1fd13e76c")
natural_language_understanding.set_service_url('https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/9d7674b4-e3b9-483d-8d45-be07ba05fc72')
news=newsapi.get_everything(q='Politics',language='en')
for i in news['articles']:
    response=natural_language_understanding.analyze(
        url=i['url'],features=Features(sentiment=SentimentOptions(document=True,targets=None))).get_result()
    print(json.dumps(response, indent=2))
