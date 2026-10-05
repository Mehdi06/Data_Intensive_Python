import unittest
from fastapi.testclient import TestClient
# j'importe l'app de mon fichier parserArchiveGH pour pouvoir tester l'app
from parserArchiveGH import app

client = TestClient(app)

class TestStringMethods(unittest.TestCase):

    
    #def test_upper(self):
     #   self.assertEqual('foo'.upper(), 'FOO')
    #ici je test qu'en allant sur mon app à la page /parse-archiv j'ai bien une page sans erreur (code 200)
    def test_app(self):
        
        response = client.get('/parse-archive')
        #J'assert donc je dis que le code doit répondre 200. Si ce n'est pas le cas, pytest va repondre une erreur.
        assert response.status_code == 200
    #ici je test la longueur de la liste. Mais la variable reponse est une reponse type HTML. Donc je la trans
    #transforme en json, puis je test la longueur.
    def test_longueur(self):
        reponse = client.get('/parse-archive')
        re = reponse.json()

        assert len(re) == 48684