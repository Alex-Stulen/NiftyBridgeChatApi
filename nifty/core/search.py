from langchain.vectorstores import Redis


def similarity_search(query: str, redis: Redis) -> list[str]:
    results = redis.similarity_search_limit_score(query=query, k=4, score_threshold=0.2)
    return [result.page_content for result in results]
