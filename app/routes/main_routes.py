from flask import request
from . import main_bp
from app.routes.url_shortening.shorten import shorten_url
from app.routes.url_shortening.redirect import redirect_to_original
from app.routes.url_shortening.stats import get_access_stats
from app.routes.url_shortening.delete import delete_short_url

# API endpoint to shorten a URL
@main_bp.route('/api/v1/shorten', methods=['POST'])
def shorten_url_route():
    data = request.get_json()
    return shorten_url(data)

# API endpoint to redirect to the original URL
@main_bp.route('/api/v1/<short_url>', methods=['GET'])
def redirect_to_original_route(short_url):
    return redirect_to_original(short_url)

# API endpoint to get access statistics for a short URL
@main_bp.route('/api/v1/stats/<short_url>', methods=['GET'])
def get_access_stats_route(short_url):
    return get_access_stats(short_url)

# API endpoint to delete a short URL
@main_bp.route('/delete/<short_url>', methods=['DELETE'])
def delete_short_url_route(short_url):
    return delete_short_url(short_url)
