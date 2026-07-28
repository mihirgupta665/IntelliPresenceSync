from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIo(audio_bytes), sr=16000)
        wav = preprocess_wav(audio) # removes the noises and normalises the audio

        embedding = encoder.embed_utterance(wav)
        return embedding.tolist() # 256 D vector although image had only 128 Dimensions

    except Exception as e:
        st.error("Error occured while Recognizing Voice.")
        return None


def identify_speaker(new_embedding, candidates_dictionary, threshold=0.65):
    if new_embedding is None or not candidates_dictionary:
        return None, 0.0

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dictionary.items():
        if stored_embedding:
            similarity = np.dot(new_embedding, stored_embedding)
            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score
    

