"""Offline data handling."""

from data_store import offline_cache


def cache_offline_data(user_id: int, data: dict) -> None:
    """Cache data for offline use."""
    offline_cache.setdefault(user_id, {}).update(data)


def sync_offline_data(user_id: int) -> dict:
    """Return cached data and clear it to simulate sync."""
    data = offline_cache.get(user_id, {})
    offline_cache[user_id] = {}
    return data
