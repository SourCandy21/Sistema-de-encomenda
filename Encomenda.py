class Encomenda:
  def __int__(self, codigo, destino, remente):
    self.codigo = codigo
    self.destino = destino
    self.remente = remente
    self.status = "Pendente"

  def entregar(self):
    self.status = "Entregue"

  def detalhes(self):
    return f"Código: {self.codigo}\nDestino: {self.destino}\nRemente: {self.remente}\nStatus: {self.status}"

class Pacote(Encomenda):
  def __init__(self, codigo, destino, remente, peso, dimensoes):
    super().__init__(codigo, destino, remente)
    self.peso = peso
    self.dimensoes = dimensoes

  def caucular_frete(self):
    return self.peso * 0.5 + sum(self.dimensoes) * 0.1

class Carta(Encomenda):
  def __int__(self, codigo, destino, remente, tipo):
    super().__init__(codigo, destino, remente)
    self.tipo = tipo

  def definir_prioridade(self):
    if self.tipo == "urgente":
      return "Alta"
    else:
      return "Normal"

class RemessaGrande(Encomenda):
  def __init__(self, codigo, destino, remente, volume, tipo_conteudo):
    super().__init__(codigo, destino, remente)
    self.volume = volume
    self.tipo_conteudo = tipo_conteudo

  def agendar_entregar(self, data_entrega):
    self.status = f"Entregue em {data_entrega}"

carta_urgente = Carta("C001", "São Paulo", "Empresa X", "urgente")
print(carta_urgente.definir_prioridade())
print("Prioridade:", carta_urgente.definir_prioridade())