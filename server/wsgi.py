from application import create_app
app = create_app()

#db = SQLAlchemy(app)
if __name__ == "__main__":
    app.run(host='192.168.1.69', port = 5000)
