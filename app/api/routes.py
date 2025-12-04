from flask import request, jsonify
from flask_login import login_required
from app.crawler import fetch_baidu_news
from . import bp

@bp.route('/news', methods=['GET'])
@login_required
def news():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"status": "error", "message": "keyword required", "data": []}), 400
    data = fetch_baidu_news(keyword)
    return jsonify({"status": "ok", "count": len(data), "data": data})
