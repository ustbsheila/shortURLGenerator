from app.models import dbQuery
from flask import jsonify, redirect

def redirect_to_original(short_url):
    url_mapping_entry = dbQuery.get_url_mapping_by_short_url(short_url)

    if url_mapping_entry:
        # Log the access
        dbQuery.add_access_log(url_mapping_entry)

        return redirect(url_mapping_entry.original_url)
    else:
        return jsonify({"Error:": f"short URL {short_url} not found!"}), 404
