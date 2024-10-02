
📊 Football Analytics Dashboard
Este projeto é um dashboard interativo desenvolvido com Streamlit, StatsBombPy, mplsoccer e outras bibliotecas de visualização. O objetivo do projeto é responder a uma pergunta específica relacionada ao futebol ⚽, utilizando dados reais para fornecer insights detalhados e visualizações dinâmicas.

📝 Objetivo
O dashboard permite que os usuários selecionem competições, temporadas, e partidas específicas para analisar estatísticas e eventos. As visualizações incluem mapas de passes, mapas de chutes e métricas detalhadas sobre os jogos, jogadores e equipes.

📂 Estrutura do Projeto
app.py: Arquivo principal do dashboard, responsável por carregar os dados e renderizar a interface com as visualizações.
requirements.txt: Contém todas as dependências necessárias para rodar o projeto.
data/: Pasta opcional onde podem ser armazenados recursos como imagens e outros arquivos estáticos.
🔧 Como Rodar o Projeto Localmente
1. Clone este repositório
bash
Copiar código
git clone https://github.com/seu-usuario/football-dashboard.git
cd football-dashboard
2. Crie e ative um ambiente virtual
No Windows:

bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
No macOS/Linux:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
Execute o seguinte comando para instalar todas as bibliotecas listadas no arquivo requirements.txt:

bash
Copiar código
pip install -r requirements.txt
4. Execute o dashboard
Para iniciar o dashboard no navegador, execute o seguinte comando no terminal:

bash
Copiar código
streamlit run app.py
O Streamlit abrirá uma janela no navegador, onde você poderá interagir com o dashboard.

📊 Funcionalidades Principais
Seleção de competições e temporadas: Escolha entre várias competições e temporadas disponíveis.
Análise de partidas e jogadores: Filtre os dados por partidas e jogadores específicos.
Visualizações interativas: Mapa de passes e mapa de chutes gerados automaticamente com base nos dados de uma partida específica.
Métricas detalhadas: Exibe informações detalhadas sobre gols, passes e outros eventos da partida.
🔨 Tecnologias Utilizadas
Streamlit: Framework para construção de dashboards interativos.
StatsBombPy: Biblioteca Python para acessar a API da StatsBomb.
mplsoccer: Biblioteca para criar visualizações de dados de futebol.
Matplotlib: Criação de gráficos e visualizações.
Pandas: Manipulação de dados.
🛠️ Como Contribuir
Faça um fork deste repositório.
Crie um branch com uma nova feature ou correção de bug:
bash
Copiar código
git checkout -b minha-feature
Faça suas alterações e commite:
bash
Copiar código
git commit -m "Adiciona nova feature"
Envie seu branch para o repositório:
bash
Copiar código
git push origin minha-feature
Abra um pull request.
🚀 Publicação
Este projeto pode ser publicado no Streamlit Community Cloud para fácil acesso. Basta seguir as instruções em Streamlit Community Cloud.