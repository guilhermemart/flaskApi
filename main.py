from flask import Flask, make_response, request
import mysql.connector
import service, server

app = server.setup_router()

if __name__ == '__main__':
    app.run(debug=True)
