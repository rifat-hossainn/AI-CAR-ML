ai-car-ml-project/
│
├── README.md
│
├── data/
│   ├── raw_log.csv              # ESP32 থেকে collected raw data
│   ├── labeled_data.csv         # ML training dataset (with labels)
│
├── models/
│   ├── ensemble_model.pkl       # trained ML model (Python only)
│   └── rules.txt                # extracted decision rules for ESP32
│
├── src/
│   ├── preprocess.py            # raw data cleaning + labeling
│   ├── train.py                 # ML model training (ensemble)
│   └── export_rules.py         # decision tree → rules conversion
│
├── esp32/
│   └── ai_car.ino              # ESP32 Arduino main code
│
└── docs/
    ├── architecture.md         # system design explanation
    └── dataset_format.md       # dataset structure details




    # 🚗 AI Car with Machine Learning (ESP32 + Python)

This project is an intelligent autonomous car system using ESP32 and Machine Learning.

## Features
- Obstacle detection using ultrasonic sensor
- Motion analysis using MPU6050 (jerk detection)
- Machine Learning (Decision Tree + KNN + Naive Bayes)
- Ensemble model for prediction
- Real-time web dashboard
- Near-miss event logging

## Tech Stack
- ESP32 (Arduino C++)
- Python (Scikit-learn)
- HTML + Chart.js
