import server

app = server.setup_router()

if __name__ == '__main__':
    app.run(debug=True)
