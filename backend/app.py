from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/briefing')
def briefing():
    return jsonify({
        "match": "Brazil vs Argentina",
        "narrative": "A classic South American rivalry.",
        "prediction": {
            "scoreline": "Brazil 2 - 1 Argentina",
            "winner": "Brazil",
            "confidence": "Narrow home victory expected.",
            "key_factors": [
                "Brazil's home form",
                "Argentina's midfield depth",
                "Set pieces"
            ]
        },
        "what_to_watch": [
            "Vinicius Jr pace on the left",
            "De Paul's press"
        ],
        "key_players": [
            {"name": "Vinicius Jr", "reason": "Pace and creativity"},
            {"name": "Lionel Messi", "reason": "Vision and set pieces"}
        ],
        "form": {"home": "WWDWW", "away": "WDWLW"},
        "h2h": [
            {"date": "2023-11-21", "home": "Brazil", "away": "Argentina", "score": "1-0"}
        ],
        "season_stats": {
            "home": {"wins": 8, "losses": 2, "draws": 2, "goals_scored": 22, "goals_conceded": 9},
            "away": {"wins": 9, "losses": 1, "draws": 2, "goals_scored": 25, "goals_conceded": 7}
        },
        "sources": ["football-data.org", "wikipedia.org", "IBM Granite via Langflow"]
    })

if __name__ == '__main__':
    app.run(debug=True)