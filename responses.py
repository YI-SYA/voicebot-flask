def get_response(user_input):
    user_input = user_input.lower()

    if "halo" in user_input:
        return "Halo juga! Ada yang bisa saya bantu?"
    elif "cuaca" in user_input:
        return "Cuaca hari ini cerah, semoga harimu juga cerah!"
    elif "siapa kamu" in user_input:
        return "Saya adalah asisten pintar buatanmu."
    else:
        return "Maaf, saya belum mengerti pertanyaan itu."
