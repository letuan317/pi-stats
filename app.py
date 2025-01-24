from flask import Flask, jsonify

from modules import system

app = Flask(__name__)


def get_pi_stats():
    cpu_usage = system.get_cpu_usage()
    ram_usage = system.get_ram_usage()
    temperature = system.get_temperature()
    # Prepare stats dictionary
    stats = {
        "cpu_usage": f"{cpu_usage}%",
        "ram_usage": f"{ram_usage}%",
        "temperature": f"{round(temperature)}°C"
    }

    return stats


@app.route('/stats', methods=['GET'])
def stats_api():
    stats = get_pi_stats()
    return jsonify(stats)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
