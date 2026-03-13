from duckduckgo_search import DDGS

def search_web(query):
    """
    Performs a real-time web search using DuckDuckGo.
    """
    try:
        results = []

        with DDGS() as ddgs:
            # Using text search for the query
            for r in ddgs.text(query, max_results=3):
                results.append(r["body"])

        return "\n---\n".join(results)

    except Exception as e:
        print("Web search error:", e)
        return ""
