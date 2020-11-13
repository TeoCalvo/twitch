# O que são dicionários
meu_dict = { }
meu_dict["nome"] = "Teodoro"
meu_dict["sobrenome"] = "Calvo"
meu_dict["hobbies"] = ["games", "livros tech", "passear", "series"]
meu_dict["nome"] + meu_dict["sobrenome"]
meu_dict['idade'] = 27

novo_dict = { "nome": "Natalia",
                "sobrenome":"Ataide",
                "idade":29,
                "hobbies": ["livros de artesanato", "filmes espanhois", "series espanholas"] }

familia = { "teo": meu_dict,
            "nah":novo_dict }


pessoas = {
    "teo":{
        "nome": "Teodoro",
        "sobrenome": "Calvo",
        "idade": 27,
        "hobbies": ["games", "leitura técnica", "séries"]
    },
    "nah":{
        "nome":"Natalia",
        "sobrenome":"Ataide",
        "idade":29,
        "hobbies": ["costura", "series", "filmes"]
    }
}