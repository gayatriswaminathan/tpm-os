"""
Model-agnostic LLM layer for TPM OS.

The CLI never talks to a specific vendor. It asks get_provider() for whatever
is available and calls .complete(system, user). Resolution order:

  1. ANTHROPIC_API_KEY  -> Claude
  2. OPENAI_API_KEY     -> OpenAI
  3. neither            -> OfflineProvider (deterministic, no network)

The offline provider means the tool runs end-to-end for anyone who clones it,
with no API key and no dependencies installed.
"""

import os


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model="claude-sonnet-4-6"):
        import anthropic  # lazy import so the SDK is optional
        self.client = anthropic.Anthropic()
        self.model = model

    def complete(self, system: str, user: str) -> str:
        msg = self.client.messages.create(
            model=self.model,
            max_tokens=1200,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return msg.content[0].text


class OpenAIProvider:
    name = "openai"

    def __init__(self, model="gpt-4o"):
        from openai import OpenAI  # lazy import
        self.client = OpenAI()
        self.model = model

    def complete(self, system: str, user: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp.choices[0].message.content


class OfflineProvider:
    """
    Deterministic fallback. Doesn't call any model — it renders a clean exec
    update directly from the structured context so the demo always produces a
    sensible result. Real runs (with an API key) go through the LLM instead.
    """

    name = "offline"

    def complete(self, system: str, user: str) -> str:
        return (
            "[offline mode — no API key found; rendered from structured data]\n\n"
            "Set ANTHROPIC_API_KEY or OPENAI_API_KEY to generate a fully "
            "LLM-written summary. The structured context below was assembled "
            "by the adapters and would be sent to the model:\n\n" + user
        )


def get_provider():
    if os.getenv("ANTHROPIC_API_KEY"):
        return AnthropicProvider()
    if os.getenv("OPENAI_API_KEY"):
        return OpenAIProvider()
    return OfflineProvider()
