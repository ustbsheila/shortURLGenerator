from app.models import dbQuery
from flask import jsonify

def delete_short_url(short_url):
    url_mapping_entry = dbQuery.get_url_mapping_by_short_url(short_url)

    if url_mapping_entry:
        dbQuery.delete_url_mapping(url_mapping_entry)
        return jsonify({"Message": f"Short URL {short_url} deleted successfully."}), 200
    else:
        return jsonify({"Error": f"Short URL {short_url} not found!"}), 404