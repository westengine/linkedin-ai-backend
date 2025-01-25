# project/server/main/views.py


from flask import Blueprint, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv() # Load environment variables
main_blueprint = Blueprint("main", __name__)

api_key=os.getenv("DEEPSEEK_API_KEY")
base_url="https://api.deepseek.com"
client = OpenAI(api_key=api_key, base_url=base_url)

@main_blueprint.route('/analyze-profile', methods=['POST'])
def analyze_profile():
    data = request.json
    profile_url = data.get('profile_url')
    if not profile_url:
        return jsonify({"error": "Profile URL is required"}), 400
    
    # Simulate LinkedIn profile data
    profile_data = {
        "headline": "Software Engineer at Tech Corp",
        "summary": "Passionate about AI and building scalable systems.",
        "skills": ["Python", "Flask", "React"]
    }

    # GEnerate audit report using GPT-4
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{
            "role": "user",
            "content": f"Analyze this LinkedIN profile: {profile_data}. Give 5 actionable tips to improve visibility."
        }]
    )
    return jsonify({"analysis": response.choices[0].message.content})