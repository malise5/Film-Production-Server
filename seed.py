from app import app
from model import db, Production

# db.init_app(app)

print("============Seeding models Please wait===================")

with app.app_context():
    Production.query.delete()
    production = []

    p1 = Production(title="Helmet", genre="Drama", director="Kudez", budget=200000,
                    description="lorem the la ponteno el marada siekhero", image="https://i.stack.imgur.com/69dhp.png", ongoing=True)

    production.append(p1)

    p2 = Production(title="Harry Potter", genre="Drama", director="Kudez", budget=45200000,
                    description="lorem the la ponteno el marada siekhero", image="https://i.stack.imgur.com/69dhp.png", ongoing=False)

    production.append(p2)

    p3 = Production(title="Tarzan", genre="Adventure", director="Malise", budget=860000,
                    description="lorem the la ponteno el marada siekhero", image="https://i.stack.imgur.com/69dhp.png", ongoing=True)

    production.append(p3)

    p4 = Production(title="Toy Story", genre="Animation", director="Mandazi", budget=596874130,
                    description="lorem the la ponteno el marada siekhero", image="https://i.stack.imgur.com/69dhp.png", ongoing=False)

    production.append(p4)

    db.session.add_all(production)
    db.session.commit()

print("============Done seeding===================")
