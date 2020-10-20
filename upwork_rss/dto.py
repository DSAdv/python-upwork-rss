from dataclasses import dataclass


@dataclass
class JobPosition:
    title: str
    link: str
    summary: str
    published: str
    posted_on: str
    budget: str = None
    hourly_range: str = None
    category: str = None
    skills: str = None
    country: str = None
    location_requirement: str = None

    @classmethod
    def from_feed(cls, data: dict):
        summary = data.get("summary")

        return cls(
            title=data.get("title"),
            link=data.get("link"),
            summary=summary,
            published=data.get("published"),
            **cls._parse_feed_summary(summary)
        )

    @classmethod
    def _parse_feed_summary(cls, summary: str) -> dict:
        data = summary.split("<br /><b>")
        parsed_data = dict()

        for data_line in data:
            elements = data_line.split("</b>")
            if len(elements) > 1:
                column_name = elements[0].lower().replace(" ", "_")
                parsed_data[column_name] = elements[1].split("\n")[0].strip(": ")

        return parsed_data
