[![Tests](https://github.com/shane-chris-barker/bop_brain/actions/workflows/test.yml/badge.svg)](https://github.com/shane-chris-barker/bop_brain/actions/workflows/test.yml)
# 🧠 Bop Brain
**Bop Brain** is the decision module for **Bop**, a work-in-progress Raspberry Pi-powered robot pet project.

This is **one of three core repositories**:
- [bop_sense](https://github.com/shane-chris-barker/bop_sense) - Listens to the world (mic, camera, sensors) and places AMQP or MQTT messages into a queue.

- ***bop_brain*** - Responsible for processing the messages produced by `bop_sense` and making decisions based on their content before dispatching the related events.

- [bop_body](https://github.com/shane-chris-barker/bop_body) - Subscribes to events produced by `bop_brain` and then take an action (motors, display, feedback etc.)

> ⚠️ **Note**: This is an early, rough WIP and very much an experiment. Things will change, break, and improve rapidly. 

>I'm also very new to Python, so there are bound to be mistakes..

I will add more information here as the project progresses.

---
## ✅️ What Bop Brain Can Do Right Now
- Starts MQTT broker with 2 topics - One for incoming events, One for outgoing events.
- Process text strings, map them to events and dispatch them into an events MQTT queue
- Receive Base64 encoded images but not do anything with them

## 🛠️ Planned Features

- Recognise a face trained via an ONNX model (You can train your own face using my [face trainer repo](https://github.com/shane-chris-barker/face-recognition-trainer))
- Configurable hardware abstraction
- Pi-specific startup optimizations
- Diagrams of Bop and the Raspberry Pi configuration

---

## 🧪 Testing

I am adding tests as I go. Run them via:

```bash
pytest --cov-report=term-missing
```
## 🚀 Getting Started
Clone this repo

Create a `.env.dev` file based on `.env.example`

Install dependencies:
```
sh setup.sh
```
Run the app
```
python main.py

```

## 🧾 Environment

The MQTT broker can be also be run using the provided `docker-compose.yml`

## 📡 Communication Types
Supports consuming with:

**AMQP** (e.g. RabbitMQ) - Coming Soon

**MQTT** (e.g. Mosquitto)

**Mock publisher** (for local dev/testing) - Coming Soon

