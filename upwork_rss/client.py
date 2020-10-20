import feedparser

from urllib.parse import urlencode
from upwork_rss.dto import JobPosition


class UpworkRSS:
    _jobs_rss_url: str = "https://www.upwork.com/ab/feed/jobs/rss"

    class SortParam:
        newest = "recency"
        relevance = "relevance+desc"
        client_spend = "client_total_charge+desc"
        client_rating = "client_rating+desc"

    def __init__(self, security_token: str):
        self.security_token = security_token

    def search(self,
               query: str = None,
               *skill_ids: int,
               offset: int = 0,
               limit: int = 25,
               sort_by: str = SortParam.newest):
        params = {
            "paging": f"{offset};{limit}",
            "securityToken": self.security_token,
            "api_params": 1,
            "query": query if query else "",
            "ontology_skill_uid": ",".join(map(str, skill_ids)) if skill_ids else "",
            "sort": sort_by
         }
        url = f"{self._jobs_rss_url}?{urlencode(params)}"

        return list(map(JobPosition.from_feed,
                        feedparser.parse(url).get("entries")))

