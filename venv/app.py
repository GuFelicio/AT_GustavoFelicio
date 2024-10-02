import streamlit as st
from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

# Título do Dashboard
st.title('Análise de Partidas de Futebol - StatsBomb ⚽')

# Função para carregar competições
@st.cache_data
def load_competitions():
    return sb.competitions()

# Função para carregar temporadas de uma competição
@st.cache_data
def load_seasons(competition_id):
    return sb.seasons(competition_id)

# Função para carregar partidas de uma temporada
@st.cache_data
def load_matches(competition_id, season_id):
    return sb.matches(competition_id=competition_id, season_id=season_id)

# Função para carregar eventos de uma partida
@st.cache_data
def load_match_events(match_id):
    return sb.events(match_id=match_id)

# Carregar as competições
competitions = load_competitions()

# Verificar se há competições disponíveis
if competitions.empty:
    st.error("Nenhuma competição disponível.")
else:
    # Seleção de competição
    competition_name = st.sidebar.selectbox(
        'Selecione a Competição', competitions['competition_name']
    )

    competition_id = competitions[competitions['competition_name'] == competition_name]['competition_id'].values[0]

    # Carregar temporadas baseadas na competição
    seasons = load_seasons(competition_id)

    # Seleção de temporada
    season_name = st.sidebar.selectbox(
        'Selecione a Temporada', seasons['season_name']
    )

    season_id = seasons[seasons['season_name'] == season_name]['season_id'].values[0]

    # Carregar as partidas da temporada
    matches = load_matches(competition_id, season_id)

    # Seleção de partida
    match = st.sidebar.selectbox(
        'Selecione a Partida', matches['home_team'] + ' vs ' + matches['away_team']
    )

    match_id = matches[
        (matches['home_team'] + ' vs ' + matches['away_team']) == match
    ]['match_id'].values[0]

    # Carregar eventos da partida
    events = load_match_events(match_id)

    # Verificar se há eventos na partida
    if events.empty:
        st.error("Nenhum evento disponível para esta partida.")
    else:
        # Exibir informações da partida selecionada
        st.subheader(f"Informações da Partida: {match}")
        st.write(f"Competição: {competition_name}")
        st.write(f"Temporada: {season_name}")

        # Estatísticas básicas da partida
        goals = events[events['type'] == 'Goal']
        passes = events[events['type'] == 'Pass']
        shots = events[events['type'] == 'Shot']

        st.write(f"Gols na Partida: {len(goals)}")
        st.write(f"Total de Passes: {len(passes)}")
        st.write(f"Total de Chutes: {len(shots)}")

        # Exibir DataFrame de eventos
        st.write("Eventos da Partida:")
        st.dataframe(events[['minute', 'type', 'player', 'team']])

        # Visualização: Mapa de Passes
        st.subheader('Mapa de Passes')
        pitch = Pitch()
        fig, ax = plt.subplots(figsize=(10, 7))
        pitch.draw(ax=ax)
        for i, row in passes.iterrows():
            pitch.arrows(row['location'][0], row['location'][1], row['pass_end_location'][0], row['pass_end_location'][1],
                         width=2, headwidth=3, color='blue', ax=ax)
        st.pyplot(fig)

        # Visualização: Mapa de Chutes
        st.subheader('Mapa de Chutes')
        fig, ax = plt.subplots(figsize=(10, 7))
        pitch.draw(ax=ax)
        for i, row in shots.iterrows():
            pitch.scatter(row['location'][0], row['location'][1], s=100, color='red', ax=ax)
        st.pyplot(fig)

        # Download dos dados da partida
        st.sidebar.download_button(
            label="Baixar dados da partida",
            data=events.to_csv(index=False),
            file_name=f"{match}_events.csv",
            mime='text/csv'
        )
