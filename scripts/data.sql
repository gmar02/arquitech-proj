-- DADOS DA TABELA DE USUÁRIO 
-- A: Autor
-- L: Leitor
INSERT OR IGNORE INTO usuario (id, nome, senha, perfil) VALUES 
    (1, "Guilherme", "123456", "A"),
    (2, "Victor", "123456", "L");

-- DADOS DA TABELA DE POST
INSERT OR IGNORE INTO post (id, titulo, subtitulo, corpo, modelo3d, id_autor)
VALUES 
    (1, 'Título do Post 1', 'Subtítulo do Post 1', 'Conteúdo do primeiro post.', NULL, 1),
    (2, 'Título do Post 2', 'Subtítulo do Post 2', 'Conteúdo do segundo post.', NULL, 1),
    (3, 'Título do Post 3', 'Subtítulo do Post 3', 'Conteúdo do terceiro post.', NULL, 1),
    (4, 'Título do Post 4', 'Subtítulo do Post 4', 'Conteúdo do quarto post.', NULL, 1);
