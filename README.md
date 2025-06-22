[![Tests](https://github.com/shane-chris-barker/bop_brain/actions/workflows/test.yml/badge.svg)](https://github.com/shane-chris-barker/bop_brain/actions/workflows/test.yml)
# 🧠 Bop Brain
**Bop Brain** is the decision module for **Bop**, a work-in-progress Raspberry Pi-powered robot pet project.

This is **one of three core repositories**:
- [bop_sense](https://github.com/shane-chris-barker/bop_sense) - Listens to the world (mic, camera, sensors) and places AMQP or MQTT messages into a queue.

- ***bop_brain*** - Responsible for processing the messages produced by `bop_sense` and making decisions based on their content before dispatching the related events.

- `bop_body` - Does not exist yet but will subscribe to events produced by `bop_brain` and then take an action (motors, display, feedback etc)

> ⚠️ **Note**: This is an early, rough WIP and very much an experiment. Things will change, break, and improve rapidly. 

>I'm also very new to Python, so there are bound to be mistakes..

I will add more information here as the project progresses.

---

## 🛠️ Planned Features

- Map voice commands sent via AMQP or MQTT to events and dispatch them to an AMQP or MQTT queue
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


## 🧾 Environment

Currently uses Docker as an MQTT broker - I'll add AMQP support and also native options via configuration as I go, to avoid running Docker on the bop_brain Pi

## 📡 Communication Types
Supports and consuming with:

**AMQP** (e.g. RabbitMQ) - Coming Soon

**MQTT** (e.g. Mosquitto)

**Mock publisher** (for local dev/testing) - Coming Soon

