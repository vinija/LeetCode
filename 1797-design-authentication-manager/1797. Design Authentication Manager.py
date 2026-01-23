from typing import Dict


class AuthenticationManager:
    """
    Manages authentication tokens with time-based expiration.
    """

    def __init__(self, timeToLive: int) -> None:
        """
        Initialize the authentication manager.

        :param timeToLive: Lifetime of each token in seconds.
        """
        if timeToLive <= 0:
            raise ValueError("timeToLive must be a positive integer")

        self._time_to_live: int = timeToLive
        self._expiry_by_token: Dict[str, int] = {}

    def _cleanup_expired(self, currentTime: int) -> None:
        """
        Lazily remove all tokens that are expired at currentTime.

        Expiration rule:
        A token with expiry time t is expired if currentTime >= t.
        """
        if currentTime < 0:
            raise ValueError("currentTime must be non-negative")

        expired_tokens = [
            token_id
            for token_id, expiry_time in self._expiry_by_token.items()
            if currentTime >= expiry_time
        ]

        for token_id in expired_tokens:
            del self._expiry_by_token[token_id]

    def generate(self, tokenId: str, currentTime: int) -> None:
        """
        Generate a new token with tokenId at currentTime.

        If the token already exists, its expiry is overwritten.
        """
        if not tokenId:
            raise ValueError("tokenId must be a non-empty string")

        self._cleanup_expired(currentTime)
        self._expiry_by_token[tokenId] = currentTime + self._time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        """
        Renew an unexpired token by extending its expiry.

        If the token does not exist or is expired, do nothing.
        """
        if not tokenId:
            raise ValueError("tokenId must be a non-empty string")

        self._cleanup_expired(currentTime)

        if tokenId in self._expiry_by_token:
            self._expiry_by_token[tokenId] = currentTime + self._time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        """
        Return the number of unexpired tokens at currentTime.
        """
        self._cleanup_expired(currentTime)
        return len(self._expiry_by_token)
