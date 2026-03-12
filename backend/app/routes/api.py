from datetime import datetime

import requests
from flask import Blueprint, current_app, jsonify, request
from flask_jwt_extended import jwt_required


api_bp = Blueprint("api", __name__)


def _nasa_get(path, params=None):
    base_url = current_app.config["NASA_BASE_URL"].rstrip("/")
    api_key = current_app.config["NASA_API_KEY"]

    query = {"api_key": api_key}
    if params:
        query.update(params)

    url = f"{base_url}{path}"
    response = requests.get(url, params=query, timeout=20)
    response.raise_for_status()
    return response.json()


@api_bp.get("/apod")
@jwt_required()
def apod():
    try:
        data = _nasa_get("/planetary/apod")
    except requests.RequestException:
        return jsonify({"error": "Falha ao consultar APOD"}), 502
    return jsonify(
        {
            "title": data.get("title"),
            "date": data.get("date"),
            "explanation": data.get("explanation"),
            "media_type": data.get("media_type"),
            "url": data.get("url"),
            "hdurl": data.get("hdurl"),
            "copyright": data.get("copyright"),
        }
    )


@api_bp.get("/mars-rover")
@jwt_required()
def mars_rover():
    sol = request.args.get("sol", "1000")
    camera = request.args.get("camera")

    params = {"sol": sol}
    if camera:
        params["camera"] = camera

    try:
        data = _nasa_get("/mars-photos/api/v1/rovers/curiosity/photos", params=params)
    except requests.RequestException:
        return jsonify({"error": "Falha ao consultar Mars Rover"}), 502
    photos = data.get("photos", [])

    # Return a trimmed list to keep payload small
    trimmed = [
        {
            "id": photo.get("id"),
            "img_src": photo.get("img_src"),
            "earth_date": photo.get("earth_date"),
            "camera": (photo.get("camera") or {}).get("full_name"),
            "rover": (photo.get("rover") or {}).get("name"),
        }
        for photo in photos[:24]
    ]

    return jsonify({"photos": trimmed, "count": len(trimmed)})


@api_bp.get("/epic")
@jwt_required()
def epic():
    epic_base = current_app.config["EPIC_BASE_URL"].rstrip("/")
    api_key = current_app.config["NASA_API_KEY"]

    try:
        response = requests.get(
            f"{epic_base}/api/natural",
            params={"api_key": api_key},
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        return jsonify({"error": "Falha ao consultar EPIC"}), 502

    if not data:
        return jsonify({"images": []})

    latest = data[0]
    date_str = latest.get("date")
    image = latest.get("image")

    if not date_str or not image:
        return jsonify({"images": []})

    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    archive_path = date.strftime("%Y/%m/%d")

    image_url = (
        f"{epic_base}/archive/natural/{archive_path}/png/{image}.png"
        f"?api_key={api_key}"
    )

    return jsonify(
        {
            "images": [
                {
                    "date": date_str,
                    "caption": latest.get("caption"),
                    "image": image,
                    "url": image_url,
                }
            ]
        }
    )
