from App import CreateAppFlask

AppCreateFlask = CreateAppFlask()

if __name__ == "__main__":
    AppCreateFlask.run(debug=True, host="0.0.0.0", port="5000")



