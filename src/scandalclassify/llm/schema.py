GROUP_JSON_SCHEMA = {
    "name": "group_article_analysis",
    "schema": {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "integer"},
                        "scandal_type": {"type": "string"},
                    },
                    "required": ["article_id", "scandal_type"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["results"],
        "additionalProperties": False,
    },
    "strict": True,
}


