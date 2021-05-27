import pytest
from flask import Flask
from unittest.mock import Mock

from rest_api import rest_api

app = Flask(__name__)


@pytest.fixture
def client():
    if app:
        with app.test_client() as client:
            yield client


def test_add_declaration(client):
    rv = client.post(
        '/add_declaration',
        json={
            'id_declaration': 1,
            'num_version': 1.1,
            'date_creation_initiale': 'date_creation_initiale',
            'emetteur': 'emetteur',
            'type_declaration': 'type_declaration',
            'lieu_extraction': 'lieu_extraction',
            'lieu_prise_en_charge': 'lieu_prise_en_charge',
            'lieu_depot': 'lieu_depot',
            'lieu_enfouissement': 'lieu_enfouissement',
            'tonnage': 42.0,
            'type_dechet': 'type_dechet'
        }
    )
    assert rv.status_code == 201
    expected = [
        {
            'idDeclaration': 1,
            'num_version': 1.1,
        }
    ]
    assert rv.json == expected


def test_get_declaration_by_id(client):
    # add authentification + headers
    rv = client.get(
        '/declaration/1'
    )
    assert rv.status_code == 200

    # representation_declaration = Mock()
    # representation_declaration.id_declaration.return_value = 1
    # representation_declaration.num_version.return_value = 1.1
    # representation_declaration.date_creation_initiale.return_value = 'date_creation_initiale'
    # representation_declaration.emetteur.return_value = 'emetteur'
    # representation_declaration.type_declaration.return_value = 'type_declaration'
    # representation_declaration.lieu_extraction.return_value = 'lieu_extraction'
    # representation_declaration.lieu_prise_en_charge.return_value = 'lieu_prise_en_charge'
    # representation_declaration.lieu_depot.return_value = 'lieu_depot'
    # representation_declaration.lieu_enfouissement.return_value = 'lieu_enfouissement'
    # representation_declaration.tonnage.return_value = 42.0
    # representation_declaration.type_dechet.return_value = 'type_dechet'

    expected = [
        {
            'id_declaration': 1,
            'num_version': 1.1,
            'date_creation_initiale': 'date_creation_initiale',
            'emetteur': 'emetteur',
            'type_declaration': 'type_declaration',
            'lieu_extraction': 'lieu_extraction',
            'lieu_prise_en_charge': 'lieu_prise_en_charge',
            'lieu_depot': 'lieu_depot',
            'lieu_enfouissement': 'lieu_enfouissement',
            'tonnage': 42.0,
            'type_dechet': 'type_dechet'
        }
    ]
    assert rv.json == expected


def test_get_declaration_by_not_found(client):
    # add authentification + headers
    rv = client.get(
        '/declaration/2'
    )
    assert rv.status_code == 404

    # declarationException = Mock()
    # declarationException.side_effect = Exception('UnknownDeclaration: Unable to find a declaration')
    assert rv.json == {
        'message': 'UnknownDeclaration: Unable to find a declaration'
                   'for declaration id 2',
        'type': 'NOT FOUND'
    }
