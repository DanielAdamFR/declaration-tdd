from flask import Flask

app = Flask(__name__)


@app.route('/declaration/<declaration>')
def add_declaration(date_creation_initiale, emetteur, type_declaration, lieu_extraction, lieu_prise_en_charge, lieu_depot, lieu_enfouissement, tonnage, type_dechet):
    return {"date_creation_initiale": date_creation_initiale, "emetteur": emetteur, "type_declaration": type_declaration, "lieu_extraction": lieu_extraction,"lieu_prise_en_charge": lieu_prise_en_charge,"lieu_depot": lieu_depot,"lieu_enfouissement": lieu_enfouissement,"tonnage": tonnage,"type_dechet": type_dechet}


if __name__ == "__main__":
    app.run()