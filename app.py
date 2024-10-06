from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

my_key_stabilityai = "sk-NyMQ7EKKjBfqJJ43kfnXk5qUel8rPhQ1rcSBHLdI8NVrcbxQ"

def generate_with_SD(prompt):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_key_stabilityai}",
    }

    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            },
            {
                "text": "blurry, bad",
                "weight": -1
            }
        ],
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Ana sayfa route'u ekleyin
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_poster', methods=['POST'])
def generate_poster():
    try:
        prompt = request.form.get('prompt')  # request.get_json yerine request.form kullanılır

        # Poster oluşturma isteği
        result = generate_with_SD(prompt)

        if result and "artifacts" in result:
            image_data = result["artifacts"][0]["base64"]
            return render_template('index.html', image=image_data)
        else:
            return render_template('index.html', error="Poster oluşturulamadı")
    except Exception as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
