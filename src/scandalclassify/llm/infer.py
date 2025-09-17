from __future__ import annotations

import os
import json
import time
from typing import List, Dict

import pandas as pd
from openai import OpenAI

from .schema import GROUP_JSON_SCHEMA


def build_system_prompt() -> str:
    return (
        "You are an expert in analyzing Korean news articles for scandals. "
        "Classify each article as '정치', '연예', or 'none' based on title and content."
    )


def call_openai(client: OpenAI, system_prompt: str, user_prompt: str, schema: dict) -> Dict:
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model="gpt-4o",
        response_format={"type": "json_schema", "json_schema": schema},
        temperature=0.0,
    )
    message = chat_completion.choices[0].message
    return json.loads(message.content)


def infer_batch(df: pd.DataFrame, article_indices: List[int], model: str = "gpt-4o") -> List[Dict]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    client = OpenAI(api_key=api_key)

    system_prompt = build_system_prompt()
    lines = []
    for idx in article_indices:
        row = df.loc[idx]
        lines.append(
            f"기사 인덱스: {idx}\n제목: {row.get('title','')}\n내용: {row.get('content','')}\n-----"
        )
    user_prompt = "아래 기사들을 분석하십시오:\n\n" + "\n".join(lines)

    for attempt in range(3):
        try:
            result = call_openai(OpenAI(api_key=api_key), system_prompt, user_prompt, GROUP_JSON_SCHEMA)
            return result.get("results", [])
        except Exception:
            time.sleep(2 * (attempt + 1))
    return []


