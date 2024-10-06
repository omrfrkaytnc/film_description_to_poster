# Movie Poster Generator

This Flask application generates custom posters from movie descriptions using Stability AI's image generation API.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Information](#api-information)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project allows users to input movie descriptions and generate posters using the Stability AI API. It's a Generative AI project that utilizes image generation models to create unique posters based on the given prompts.

## Features
- Generate high-quality posters from movie descriptions.
- Uses Stability AI's Stable Diffusion model for text-to-image generation.
- Flask-powered backend with a simple web interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-poster-generator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd movie-poster-generator
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set your Stability AI API key in the `my_key_stabilityai` variable.

## Usage

1. Run the Flask application:
    ```bash
    flask run
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

3. Enter a movie description in the input box and click 'Generate Poster' to see the results.

## API Information
This project uses the [Stability AI API](https://platform.stability.ai/docs) to generate images from text prompts. The `generate_with_SD` function sends a request to the API and processes the response.

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Film Afişi Oluşturucu

Bu Flask uygulaması, film açıklamalarından Stability AI'nın görsel üretim API'si ile özel posterler oluşturur.

## İçindekiler
- [Giriş](#giriş)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [API Bilgileri](#api-bilgileri)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Giriş
Bu proje, kullanıcıların film açıklamalarını girerek Stability AI API'si kullanarak poster oluşturmasını sağlar. Generative AI tabanlı bu proje, verilen girdilere dayalı olarak görsel üretim modellerini kullanır.

## Özellikler
- Film açıklamalarından yüksek kaliteli posterler oluşturun.
- Stability AI'nin Stable Diffusion modelini kullanır.
- Flask tabanlı backend ve basit bir web arayüzü sunar.

## Kurulum

1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/your-username/movie-poster-generator.git
    ```

2. Proje dizinine geçin:
    ```bash
    cd movie-poster-generator
    ```

3. Sanal ortam oluşturun ve aktif edin:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows'da: .venv\Scripts\activate
    ```

4. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

5. Stability AI API anahtarınızı `my_key_stabilityai` değişkenine ekleyin.

## Kullanım

1. Flask uygulamasını başlatın:
    ```bash
    flask run
    ```

2. Tarayıcınızdan şu adrese gidin:
    ```
    http://127.0.0.1:5000/
    ```

3. Film açıklamasını kutuya girin ve 'Afişi Oluştur' butonuna tıklayın.

## API Bilgileri
Bu proje, metin girdilerinden görsel oluşturmak için [Stability AI API](https://platform.stability.ai/docs) kullanır. `generate_with_SD` fonksiyonu, API'ye bir istek gönderir ve gelen yanıtı işler.

## Katkıda Bulunma
Katkılarınızı bekliyoruz! Eğer katkıda bulunmak isterseniz, lütfen depoyu fork edin ve bir pull request gönderin.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.
