# Projeto Integração IOT com Mecatrônica

## Integrantes

### Analise e Desenvolvimento de Sistemas (ADS)
- Erick Cassoli
- Felipe Camargo
- Gustavo Oliveira
- Misael Willian
- Rafael Mattos

### Mecatrônica
- Billy
- Falcão

## Link para envio do JSON

[API de Envio de Dados](https://apisenai.pythonanywhere.com/sensor-data/)

## Descrição do Projeto

O projeto consiste em uma API desenvolvida utilizando o Django Rest Framework no ambiente PythonAnywhere. A aplicação é focada no monitoramento e cálculo do volume de água em uma caixa d'água, sendo direcionada a ambientes que demandam controle preciso do armazenamento hídrico, como residências, empresas ou locais de cultivo. No caso específico do cliente, a aplicação será utilizada para monitorar o nível de água em uma caixa d'água em um trailer.

## Funcionalidades Principais

### Nível da Água

A API recebe dados do sensor ultrassônico, processa-os e calcula o volume de água presente na caixa. Utilizando informações como altura, comprimento e largura da caixa d'água, a função realiza os cálculos necessários para determinar a quantidade de litros e a porcentagem de ocupação.

### Detecção de Ativação de Válvula

Além do cálculo do volume, a API identifica se a válvula está acionada, indicando um possível aumento no nível de água na caixa. Analisa leituras anteriores do sensor para detectar se houve um aumento progressivo no nível de água.

### Histórico do Nível da Água

A API armazena informações do nível da água para proporcionar um histórico dos gastos anteriores. O banco de dados utilizado no projeto é o SQLite.

## Instruções de Uso da API

Utilize o método GET no endpoint `sensor-data/` para enviar os dados do sensor. O formato JSON para o envio de dados é o seguinte:

```json
{
  "valor": n
}
```

Atenção: A API foi desenvolvida com base na informação que o sensor envia a distância que ele recebe em centímetros. Qualquer modificação perante a isso deve ser informada.

## Fluxo de Funcionamento

Quando a API recebe os dados do sensor ultrassônico via método POST no endpoint `sensor-data/`, ela utiliza o serializer para validar e salvar os dados. A função `process_sensor_data()` é acionada, realizando cálculos com base nas dimensões da caixa d'água para determinar o volume atual de água, calculando a porcentagem de ocupação e verificando se a válvula está acionada. Os resultados são retornados em formato JSON pelo endpoint `processed-data/`, permitindo o acesso aos dados atualizados sobre o nível de água na caixa.

## Designer (Figma)

### Telas
- Tela de Início
- Tela de Alertas

### Funcionalidades
- A tela de Alertas exibirá notificações referentes à caixa d’água, como nível alto, nível baixo, nível muito baixo e se a válvula está ligada.
- A tela de Início apresentará o nível da água em porcentagem, um gráfico de consumo por hora e uma imagem ilustrativa indicando se a válvula está ligada (on) ou desligada (off).

## Visão Geral

O projeto tem como objetivo oferecer uma solução eficiente e precisa para o monitoramento do volume de água em caixas d'água. Os usuários poderão acompanhar o estado do armazenamento, a quantidade de água disponível e identificar possíveis aumentos no nível de água. O design será desenvolvido em React-Native, com páginas de Alertas e Início, proporcionando uma interface intuitiva e informativa.

## Link para os Repositorios originais
### AVISO:
Os Commits dos integrantes foram todos feitos no repositorio original, todos participaram dos projetos (front e back).

- [API](https://github.com/ErickCassoli/IOT-API.git)
- [Dashboard / Aplicação](https://github.com/GtOliv3r/hydro_sonar_front.git)