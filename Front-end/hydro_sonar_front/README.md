
# Telas do Projeto de Controle de Nível de Água - IOT API
Para iniciar o programa, siga estes passos:

1. Você pode executar os arquivos start_program.bat para Windows ou start\_program.sh para linux caso ocorra algum erro na execução desses arquivos poderá fazer o passo a passo a seguir (Esses arquivos estão no diretorio Front-end).

1. **Acesso à Pasta do Projeto:**
   Abra o terminal e navegue até a pasta onde está localizado o projeto. Use o comando `cd` para entrar em cada diretório necessário. Por exemplo:
   ```
   cd Project-IOT
   cd Front-end
   cd hydro_sonar_front
   cd hydrosonar
   ```

2. **Instalação das Dependências:**
   Após acessar a pasta correta do projeto, execute o comando `npm install`. Isso instalará todas as dependências necessárias para o projeto.

   ```
   npm install
   ```

3. **Iniciar o Programa com Expo:**
   Depois de instalar as dependências, inicie o programa usando o Expo. Utilize o comando `npx expo start`.

   ```
   npx expo start
   ```

Estes passos devem permitir que você inicie o programa com sucesso. Certifique-se de estar no diretório correto e de ter todas as dependências necessárias instaladas antes de iniciar o programa.

## Tela Inicial

A tela inicial exibe informações vitais sobre o sistema de controle de nível de água. Aqui estão os elementos principais:

- **Imagem Dinâmica:** Mostra a quantidade de líquido em litros e em porcentagem.
- **Gráfico de Consumo:** Apresenta informações sobre o consumo por hora.
- **Ilustração do Estado da Válvula:** Representa se a válvula está ligada (ON) ou desligada (OFF).
- **Barra de Navegação:** Permite a alternância entre as abas "Alertas" e "Início".



## Tela de Alertas

Nesta tela, os alertas são apresentados em formato de tabela, contendo as seguintes informações:

- **Tipo de Alerta:** Indica o evento ocorrido (Nível de água acima de 80%, acima do limite, possível vazamento ou abaixo de 5%).
- **Data do Alerta:** Informa a data em que o alerta foi acionado.
- **Horário do Alerta:** Apresenta o horário em que o alerta foi acionado.
- **Barra de Navegação:** Similar à tela inicial, essa barra permite a alternância entre as abas "Alertas" e "Início".

