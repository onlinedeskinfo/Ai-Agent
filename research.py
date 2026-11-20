import requests
from bs4 import BeautifulSoup

def research_topic(topic):
    print(f"Researching: {topic}")

    url = "https://en.wikipedia.org/wiki/" + topic.replace(" ", "_")

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        research = []

        for p in paragraphs:
            text = p.get_text(" ", strip=True)
            if len(text) > 100:
                research.append(text)

        return "\n\n".join(research[:15])

    except Exception as e:
        return f"Research error: {e}"
