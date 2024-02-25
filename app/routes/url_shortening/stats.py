from app.models import dbQuery
from datetime import datetime
from flask import jsonify

def get_access_stats(short_url):
    url_mapping_entry = dbQuery.get_url_mapping_by_short_url(short_url)

    if url_mapping_entry:
        # Get access statistics
        now = datetime.utcnow()
        last_24_hours_stats = dbQuery.get_last_24_hour_access_stats(url_mapping_entry, now)
        past_week_stats = dbQuery.get_past_week_access_stats(url_mapping_entry, now)
        all_time_stats = dbQuery.get_all_time_access_stats(url_mapping_entry)
        return jsonify({
            "last_24_hours_access_stats": last_24_hours_stats,
            "past_week_access_stats": past_week_stats,
            "all_time_access_stats": all_time_stats
        }), 200
    else:
        return jsonify({"Error": f"Short URL {short_url} not found"}), 404