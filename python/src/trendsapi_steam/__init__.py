"""trendsapi-steam - Trends API client with source preset to `steam`.

One API key still unlocks every other source. Pass source= to override.

Get a free API key: https://trendsapi.ai/#get-key
"""

from trendsapi import (
    AsyncTrendsAPI as _AsyncTrendsAPI,
    TrendsAPI as _TrendsAPI,
    TrendsAPIError,
)

__version__ = "1.0.0"
DEFAULT_SOURCE = "steam"
DEFAULT_FEED = "Steam Most Played"
__all__ = [
    "TrendsAPI",
    "AsyncTrendsAPI",
    "TrendsAPIError",
    "DEFAULT_SOURCE",
    "DEFAULT_FEED",
    "__version__",
]


class TrendsAPI(_TrendsAPI):
    """Sync client. Keyword-first helpers default to `steam`."""

    def get_time_series(self, keyword, source=DEFAULT_SOURCE, data_mode=None):
        return super().get_time_series(source=source, keyword=keyword, data_mode=data_mode)

    def get_trends(self, keyword, source=DEFAULT_SOURCE, data_mode=None):
        return self.get_time_series(keyword=keyword, source=source, data_mode=data_mode)

    def get_growth(self, keyword, percent_growth=None, source=DEFAULT_SOURCE, data_mode=None):
        return super().get_growth(
            source=source,
            keyword=keyword,
            percent_growth=percent_growth,
            data_mode=data_mode,
        )

    def get_live(self, limit=None, offset=None, category=None):
        return self.get_top_trends(type=DEFAULT_FEED, limit=limit, offset=offset, category=category)


class AsyncTrendsAPI(_AsyncTrendsAPI):
    """Async client. Keyword-first helpers default to `steam`."""

    async def get_time_series(self, keyword, source=DEFAULT_SOURCE, data_mode=None):
        return await super().get_time_series(source=source, keyword=keyword, data_mode=data_mode)

    async def get_trends(self, keyword, source=DEFAULT_SOURCE, data_mode=None):
        return await self.get_time_series(keyword=keyword, source=source, data_mode=data_mode)

    async def get_growth(self, keyword, percent_growth=None, source=DEFAULT_SOURCE, data_mode=None):
        return await super().get_growth(
            source=source,
            keyword=keyword,
            percent_growth=percent_growth,
            data_mode=data_mode,
        )

    async def get_live(self, limit=None, offset=None, category=None):
        return await self.get_top_trends(type=DEFAULT_FEED, limit=limit, offset=offset, category=category)

