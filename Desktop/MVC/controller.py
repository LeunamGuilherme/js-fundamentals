from dal import PessoaDAL
from model import Pessoa

class PessoaController:
    @classmethod
    def Cadastrar(cls, nome, idade, cpf):
        # 1. Valida os dados antes de instanciar e salvar
        if len(nome) > 2 and (0 < idade < 200) and len(str(cpf)) == 11:
            try:
                pessoa = Pessoa(nome, idade, cpf)
                PessoaDAL.salvar(pessoa)
                return True
            except Exception:
                return False
        else:
            return False