SELECT descricao_cargo, descricao_cor_raca, count( distinct numero_sequencial) as qtde_raca
FROM ABT_CLUSTERING
WHERE descricao_cor_raca IN ({racas})
GROUP BY descricao_cargo, descricao_cor_raca