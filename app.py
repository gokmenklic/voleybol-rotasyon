
import streamlit as st

st.set_page_config(page_title="Voleybol Takip ve Rotasyon Asistanı", layout="wide")

st.title("🏐 Voleybol Takip ve Rotasyon Asistanı")

# Oyuncu Bilgileri Girişi
st.sidebar.header("Oyuncu Kadrosu")
player_data = []

for i in range(1, 13):
    with st.sidebar.expander(f"{i}. Oyuncu"):
        name = st.text_input(f"Oyuncu {i} Adı", key=f"name_{i}")
        number = st.number_input(f"Forma Numarası", min_value=1, max_value=99, key=f"num_{i}")
        position = st.selectbox("Mevki", ["Pasör", "Smaçör", "Orta", "Libero", "Pasör Çaprazı"], key=f"pos_{i}")
        note = st.text_area("Antrenör Notu", key=f"note_{i}")
        player_data.append({"ad": name, "numara": number, "mevki": position, "not": note})

st.subheader("📋 Sahadaki Oyuncular")
court = st.columns(6)
for i in range(6):
    with court[i]:
        st.markdown(f"### Pozisyon {i+1}")
        st.write(f"**{player_data[i]['ad']}**")
        st.write(f"#{player_data[i]['numara']} - {player_data[i]['mevki']}")

st.subheader("📦 Yedek Oyuncular")
bench = st.columns(6)
for i in range(6, 11):
    with bench[i-6]:
        st.write(f"**{player_data[i]['ad']}**")
        st.write(f"#{player_data[i]['numara']} - {player_data[i]['mevki']}")

st.subheader("🛡️ Libero")
st.write(f"**{player_data[11]['ad']}**")
st.write(f"#{player_data[11]['numara']} - {player_data[11]['mevki']}")

# 1 tur döndürme işlemi
if st.button("🔄 1 Tur Rotasyon Yap"):
    player_data[:6] = [player_data[5]] + player_data[:5]
    st.success("1 tur rotasyon tamamlandı. Sayfayı yenileyerek sonucu görebilirsin.")
