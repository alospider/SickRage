# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions. The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.   How to use this API documentation ----------------   You may browse the API routes without authentication, but if you wish to send requests to the API and see response data, then you must authenticate. 1. Obtain a JWT token by `POST`ing  to the `/login` route in the `Authentication` section with your API key and credentials. 1. Paste the JWT token from the response into the \"JWT Token\" field at the top of the page and click the 'Add Token' button.   You will now be able to use the remaining routes to send requests to the API and get a response.   Language Selection ----------------   Language selection is done via the `Accept-Language` header. At the moment, you may only pass one language abbreviation in the header at a time. Valid language abbreviations can be found at the `/languages` route..   Authentication ----------------   Authentication to use the API is similar to the How-to section above. Users must `POST` to the `/login` route with their API key and credentials in the following format in order to obtain a JWT token.  `{\"apikey\":\"APIKEY\",\"username\":\"USERNAME\",\"userkey\":\"USERKEY\"}`  Note that the username and key are ONLY required for the `/user` routes. The user's key is labled `Account Identifier` in the account section of the main site. The token is then used in all subsequent requests by providing it in the `Authorization` header. The header will look like: `Authorization: Bearer <yourJWTtoken>`. Currently, the token expires after 24 hours. You can `GET` the `/refresh_token` route to extend that expiration date.   Versioning ----------------   You may request a different version of the API by including an `Accept` header in your request with the following format: `Accept:application/vnd.thetvdb.v$VERSION`. This documentation automatically uses the version seen at the top and bottom of the page.

    OpenAPI spec version: 2.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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

from __future__ import absolute_import

# import models into model package
from .auth import Auth
from .basic_episode import BasicEpisode
from .conflict import Conflict
from .episode import Episode
from .episode_data_query_params import EpisodeDataQueryParams
from .episode_record_data import EpisodeRecordData
from .filter_keys import FilterKeys
from .json_errors import JSONErrors
from .language import Language
from .language_data import LanguageData
from .links import Links
from .not_authorized import NotAuthorized
from .not_found import NotFound
from .series import Series
from .series_actors import SeriesActors
from .series_actors_data import SeriesActorsData
from .series_data import SeriesData
from .series_episodes import SeriesEpisodes
from .series_episodes_query import SeriesEpisodesQuery
from .series_episodes_query_params import SeriesEpisodesQueryParams
from .series_episodes_summary import SeriesEpisodesSummary
from .series_image_query_result import SeriesImageQueryResult
from .series_image_query_result_ratings_info import SeriesImageQueryResultRatingsInfo
from .series_image_query_results import SeriesImageQueryResults
from .series_images_count import SeriesImagesCount
from .series_images_counts import SeriesImagesCounts
from .series_images_query_param import SeriesImagesQueryParam
from .series_images_query_params import SeriesImagesQueryParams
from .series_search_data import SeriesSearchData
from .token import Token
from .update import Update
from .update_data import UpdateData
from .update_data_query_params import UpdateDataQueryParams
from .user import User
from .user_data import UserData
from .user_favorites import UserFavorites
from .user_favorites_data import UserFavoritesData
from .user_ratings import UserRatings
from .user_ratings_data import UserRatingsData
from .user_ratings_data_no_links import UserRatingsDataNoLinks
from .user_ratings_data_no_links_empty_array import UserRatingsDataNoLinksEmptyArray
from .user_ratings_query_params import UserRatingsQueryParams
