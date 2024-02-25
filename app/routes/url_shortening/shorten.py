from flask import request, jsonify
from app.models import dbQuery
from app.config import Config
import binascii

def generate_short_code(original_url):
    # Convert the URL to bytes
    url_bytes = original_url.encode('utf-8')

    # Calculate the CRC32 checksum
    crc32_checksum = binascii.crc32(url_bytes)

    # Convert the checksum to a positive integer
    positive_crc32 = crc32_checksum & 0xFFFFFFFF

    # Convert the integer to a string representation
    short_code = format(positive_crc32, 'x')

    return short_code

def shorten_url(data):
    data = request.get_json()
    original_url = data.get('long_url')

    # Check if the URL is valid (add more validation as needed)
    if not original_url:
        return jsonify({"Error": "Invalid request. long_url is required in the request body."}), 400

    # Check if the URL is already shortened
    url_mapping_entry = dbQuery.check_original_url_exist(original_url)
    if url_mapping_entry:
        return jsonify({"short_url": f"{Config.RUNNING_HOST}/api/v1/{url_mapping_entry.short_url}"}), 200

    # Generate a unique short code
    generated_short_url = generate_short_code(original_url)

    # Create a new ShortURL entry
    dbQuery.add_url_mapping(original_url=original_url, short_url=generated_short_url)

    return jsonify({"short_url": f"{Config.RUNNING_HOST}/api/v1/{generated_short_url}"}), 201