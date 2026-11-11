from pathlib import Path
import sys
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample_news.csv"

st.set_page_config(page_title="Newstensity | Workflow Demo", page_icon="N", layout="wide")
st.title("Newstensity - News Monitoring Workflow")
st.caption("DEMO / SIMULASI: seluruh 500 artikel pada halaman ini sintetis, bukan berita aktual.")

df = pd.read_csv(DATA)
df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce", utc=True)

with st.sidebar:
    st.header("Filter simulasi")
    min_date = df["published_at"].min().date()
    max_date = df["published_at"].max().date()
    date_range = st.date_input("Rentang tanggal", value=(min_date, max_date))
    sources = st.multiselect("Sumber", sorted(df["source"].unique()), default=sorted(df["source"].unique()))
    topics = st.multiselect("Kelompok isu", sorted(df["issue_group_simulation"].unique()), default=sorted(df["issue_group_simulation"].unique()))
    sentiments = st.multiselect("Sentimen simulasi", ["Positif", "Negatif", "Netral"], default=["Positif", "Negatif", "Netral"])

filtered = df.copy()
if isinstance(date_range, tuple) and len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0], tz="UTC"), pd.Timestamp(date_range[1], tz="UTC") + pd.Timedelta(days=1)
    filtered = filtered[(filtered["published_at"] >= start) & (filtered["published_at"] < end)]
if sources:
    filtered = filtered[filtered["source"].isin(sources)]
if topics:
    filtered = filtered[filtered["issue_group_simulation"].isin(topics)]
if sentiments:
    filtered = filtered[filtered["sentiment_simulation"].isin(sentiments)]

c1,c2,c3,c4 = st.columns(4)
c1.metric("Artikel pada filter", f"{len(filtered):,}")
c2.metric("Sumber media simulasi", f"{filtered['source'].nunique():,}")
c3.metric("Kelompok isu", f"{filtered['issue_group_simulation'].nunique():,}")
c4.metric("Rentang data", f"{filtered['published_at'].nunique():,} timestamp")

left,right = st.columns(2)
with left:
    st.subheader("Distribusi sentimen")
    sentiment_order = ["Positif", "Negatif", "Netral"]
    counts = filtered["sentiment_simulation"].value_counts().reindex(sentiment_order, fill_value=0).rename_axis("Sentimen").reset_index(name="Artikel")
    fig = px.pie(counts, names="Sentimen", values="Artikel", hole=0.55)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Volume pemberitaan")
    daily = filtered.assign(tanggal=filtered["published_at"].dt.date).groupby("tanggal").size().reset_index(name="Artikel")
    fig = px.line(daily, x="tanggal", y="Artikel", markers=True)
    st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Kelompok isu")
    topic_counts = filtered["issue_group_simulation"].value_counts().rename_axis("Kelompok isu").reset_index(name="Artikel")
    st.plotly_chart(px.bar(topic_counts, x="Artikel", y="Kelompok isu", orientation="h"), use_container_width=True)
with right:
    st.subheader("Distribusi sumber")
    source_counts = filtered["source"].value_counts().head(10).rename_axis("Sumber").reset_index(name="Artikel")
    st.plotly_chart(px.bar(source_counts, x="Sumber", y="Artikel"), use_container_width=True)

st.subheader("Daftar artikel sintetis")
show_cols = ["published_at", "source", "title", "issue_group_simulation", "sentiment_simulation"]
st.dataframe(filtered[show_cols].sort_values("published_at", ascending=False), use_container_width=True, hide_index=True)

st.info("Catatan interpretasi: label sentimen pada dataset merupakan label kontrol untuk simulasi. Demonstrasi ini tidak mengukur akurasi model dan tidak merepresentasikan opini masyarakat.")
