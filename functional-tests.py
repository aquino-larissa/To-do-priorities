############################## INICIO ####################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVsitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://127.0.0.1:8000/")

    def test_correct_title(self):
        self.setUp()
        assert 'Priority to-do lists' in self.browser.title
        self.tearDown()

    def test_find_element_by_tag_name(self):
        self.setUp()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.tearDown()

    def test_find_element_by_id(self):
        self.setUp()
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Insira um item e a sua prioridade'
        )
        self.tearDown()

    def test_typing(self):
        self.setUp()
        inputbox.send_keys('Comprar anzol')
        self.tearDown()

    #def test_select_priority(self):
      #  self.setUp()

       # self.tearDown()

    def test_refresh_page(self):
        self.setUp()
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1 - Comprar anzol - prioridade alta' for row in rows)
        )
        self.tearDown()

    def tearDown(self):
        self.browser.quit()

# Edith ouviu falar que agora a aplicação online de lista de tarefas
# aceita definir prioridades nas tarefas do tipo baixa, média e alta

# Ela decide verificar a homepage
visitorTest = NewVsitorTest()
#visitorTest.setUp()

# Ela percebe que o título da página e o cabeçalho mencionam
# listas de tarefas com prioridade (priority to-do)
visitorTest.test_correct_title()
visitorTest.test_find_element_by_tag_name()

# Ela é convidada a inserir um item de tarefa e a prioridade da
# mesma imediatamente
visitorTest.test_find_element_by_id()

# Ela digita "Comprar anzol" em uma nova caixa de texto
# e assinala prioridade alta no campo de seleção de prioridades
visitorTest.test_typing()
#visitorTest.test_select_priority()

# Quando ela tecla enter, a página é atualizada, e agora
# a página lista "1 - Comprar anzol - prioridade alta"
# como um item em uma lista de tarefas
visitorTest.test_refresh_page()

# Ainda continua havendo uma caixa de texto convidando-a a
# acrescentar outro item. Ela insere "Comprar cola instantâne"
# e assinala prioridade baixa pois ela ainda tem cola suficiente
# por algum tempo


# A página é atualizada novamente e agora mostra os dois
# itens em sua lista e as respectivas prioridades


# Edith se pergunta se o site lembrará de sua lista. Então
# ela nota que o site gerou um URL único para ela -- há um
# pequeno texto explicativo para isso.


# Ela acessa essa URL -- sua lista de tarefas continua lá.


################################# FIM ####################################

if __name__ == '__main__':
	unittest.main()