"""Define Available Models"""
from enum import StrEnum


class NexusRavenV2Models(StrEnum):
    """
    Nexus Raven V2 - 13b models

    More info: https://huggingface.co/TheBloke/NexusRaven-V2-13B-GGUF
    """
    Q5_K_M = "models/nexusraven-v2-13b.Q5_K_M.gguf"
